from django.contrib import admin
from .models import Category, Course, Tag, CourseTag

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'available', 'date')
    list_filter = ('category', 'available')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

class CourseTagAdmin(admin.ModelAdmin):
    list_display = ('course', 'tag')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(CourseTag, CourseTagAdmin)