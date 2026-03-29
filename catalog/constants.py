COURSES = [
    {
        'id': 1,
        'title': 'Введение в Python',
        'description': 'Основы программирования на Python.',
        'author_id': 1,
        'slug': 'python-basics'
    },
    {
        'id': 2,
        'title': 'Машинное обучение для начинающих',
        'description': 'Погружение в мир машинного обучения.',
        'author_id': 2,
        'slug': 'ml-for-beginners'
    },
    {
        'id': 3,
        'title': 'Веб-разработка на Django',
        'description': 'Создание веб-приложений с фреймворком Django.',
        'author_id': 1,
        'slug': 'django-web-dev'
    },
]

AUTHORS = [
    {
        'id': 1,
        'name': 'Иван Сидоров',
        'bio': 'Опытный Python-разработчик и преподаватель.',
        'courses_taught': [1, 3]
    },
    {
        'id': 2,
        'name': 'Лариса Петрова',
        'bio': 'Специалист по машинному обучению и анализу данных.',
        'courses_taught': [2]
    },
]

def get_course_by_id(course_id):
    for course in COURSES:
        if course['id'] == course_id:
            return course
    return None

def get_course_by_slug(course_slug):
    for course in COURSES:
        if course['slug'] == course_slug:
            return course
    return None

def get_author_by_id(author_id):
    for author in AUTHORS:
        if author['id'] == author_id:
            return author
    return None
