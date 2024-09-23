# courses/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('student_page/', views.student_page, name='student_page'),
    path('profile/', views.profile_page, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('delete/student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('delete/lesson/<int:lesson_id>/', views.delete_lesson, name='delete_lesson'),
    path('delete/module/<int:module_id>/', views.delete_module, name='delete_module'),
    path('create_quiz/', views.create_quiz, name='create_quiz'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
]

