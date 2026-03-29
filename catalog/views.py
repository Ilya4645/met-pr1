from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.template import RequestContext
from .constants import COURSES, AUTHORS, get_course_by_id, get_author_by_id, get_course_by_slug
import os

def index(request):
    """Главная страница."""
    context = {
        'title': 'Главная страница',
        'courses': COURSES[:3],
        'authors': AUTHORS[:2]
    }
    return render(request, 'catalog/index.html', context)


def course_list(request):
    """Список всех курсов."""
    context = {
        'title': 'Список курсов',
        'courses': COURSES
    }
    return render(request, 'catalog/courses.html', context)


def course_detail(request, course_slug):
    """Страница отдельного курса."""
    course = get_course_by_slug(course_slug)
    if not course:
        pass

    author = get_author_by_id(course['author_id']) if course else None

    context = {
        'title': f"Курс: {course['title']}" if course else 'Курс не найден',
        'course': course,
        'author': author
    }
    if not course:
        return render(request, 'catalog/course_detail.html', context, status=404)

    return render(request, 'catalog/course_detail.html', context)


def author_list(request):
    """Список всех авторов."""
    context = {
        'title': 'Список авторов',
        'authors': AUTHORS
    }
    return render(request, 'catalog/authors.html', context)


def author_detail(request, author_id):
    """Страница отдельного автора."""
    author = get_author_by_id(author_id)

    if not author:
        return HttpResponseNotFound("<h1>Автор не найден</h1>")

    authors_courses = []
    for course_id in author.get('courses_taught', []):
        course = get_course_by_id(course_id)
        if course:
            authors_courses.append(course)

    context = {
        'title': f"Автор: {author['name']}",
        'author': author,
        'courses': authors_courses
    }
    return render(request, 'catalog/author_detail.html', context)


def info_page(request):
    """Информационная страница."""
    context = {
        'title': 'Информация о сайте'
    }
    return render(request, 'catalog/info.html', context)

def page_not_found_view(request, exception):
    return render(request, 'catalog/not_found.html', status=404)