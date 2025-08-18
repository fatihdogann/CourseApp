from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from .models import Course, Category, Tag
from .forms import CourseForm

def course_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    courses = Course.objects.all()
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        courses = courses.filter(category=category)
    
    page = request.GET.get('page', 1)
    paginator = Paginator(courses, 6)
    
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)
    
    context = {
        'courses': courses,
        'categories': categories,
        'category': category,
        'total_courses': courses.paginator.count,
    }
    
    return render(request, 'courses/courses.html', context)

def course_detail(request, category_slug, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    tags = Tag.objects.filter(tag_courses__course=course)
    related_courses = Course.objects.filter(category=course.category).exclude(id=course.id)[:3]
    
    context = {
        'course': course,
        'tags': tags,
        'related_courses': related_courses
    }
    
    return render(request, 'courses/course.html', context)

@login_required
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.teacher = request.user
            
            slug = course.name.lower()
            replacements = {
                'ı': 'i', 'ğ': 'g', 'ü': 'u', 'ş': 's', 'ö': 'o', 'ç': 'c',
                'İ': 'i', 'Ğ': 'g', 'Ü': 'u', 'Ş': 's', 'Ö': 'o', 'Ç': 'c'
            }
            for old, new in replacements.items():
                slug = slug.replace(old, new)
            
            import re
            slug = re.sub(r'[^a-z0-9]', '-', slug)
            slug = re.sub(r'-+', '-', slug)
            slug = slug.strip('-')
            
            course.slug = slug
            course.available = True
            course.save()
            
            messages.success(request, 'Kurs başarıyla oluşturuldu!')
            return redirect('course_detail', category_slug=course.category.slug, course_slug=course.slug)
    else:
        form = CourseForm()
    
    return render(request, 'courses/create_course.html', {'form': form})

@login_required
def update_course(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug, teacher=request.user)
    
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            updated_course = form.save()
            messages.success(request, 'Kurs başarıyla güncellendi!')
            return redirect('course_detail', category_slug=updated_course.category.slug, course_slug=updated_course.slug)
    else:
        form = CourseForm(instance=course)
    
    context = {
        'form': form,
        'course': course
    }
    
    return render(request, 'courses/update_course.html', context)

@login_required
def delete_course(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug, teacher=request.user)
    
    if request.method == 'POST':
        category_slug = course.category.slug
        course.delete()
        messages.success(request, 'Kurs başarıyla silindi!')
        return redirect('courses_by_category', category_slug=category_slug)
    
    return render(request, 'courses/delete_course.html', {'course': course})

def courses_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    courses = Course.objects.filter(course_tags__tag=tag)
    
    page = request.GET.get('page', 1)
    paginator = Paginator(courses, 6)
    
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)
    
    categories = Category.objects.all()
    
    context = {
        'courses': courses,
        'categories': categories,
        'tag': tag,
        'total_courses': courses.paginator.count,
    }
    
    return render(request, 'courses/courses_by_tag.html', context)

@login_required
def teacher_dashboard(request):
    teacher_courses = Course.objects.filter(teacher=request.user)
    
    context = {
        'courses': teacher_courses,
        'total_courses': teacher_courses.count(),
    }
    
    return render(request, 'courses/teacher_dashboard.html', context)

@login_required
def create_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            category, created = Category.objects.get_or_create(
                name=name,
                defaults={'slug': name.lower().replace(' ', '-')}
            )
            if created:
                messages.success(request, f'"{name}" kategorisi başarıyla oluşturuldu!')
            else:
                messages.info(request, f'"{name}" kategorisi zaten mevcut.')
            return JsonResponse({'status': 'success', 'id': category.id, 'name': category.name})
        else:
            return JsonResponse({'status': 'error', 'message': 'Kategori adı boş olamaz.'})
    return JsonResponse({'status': 'error', 'message': 'Geçersiz istek.'})