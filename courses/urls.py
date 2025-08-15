from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='courses'),
    path('create/', views.create_course, name='create_course'),
    path('create-category/', views.create_category, name='create_category'),
    path('update/<slug:course_slug>/', views.update_course, name='update_course'),
    path('delete/<slug:course_slug>/', views.delete_course, name='delete_course'),
    path('<slug:category_slug>/', views.course_list, name='courses_by_category'),
    path('<slug:category_slug>/<slug:course_slug>/', views.course_detail, name='course_detail'),
]