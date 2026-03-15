from django.urls import path, re_path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),

    # Список курсов
    path('courses/', views.course_list, name='courses'),

    # Страница отдельного курса
    re_path(r'course/(?P<course_slug>[\w-]+)/$', views.course_detail, name='course_detail'),

    # Список авторов
    path('authors/', views.author_list, name='authors'),

    # Страница отдельного автора
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),

    # Страница info
    path('info/', views.info_page, name='info'),
]