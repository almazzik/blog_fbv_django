
Проект Блог на Django 5

Проект написан в рамках обучающего курса, представления на основе функций (FBV)

- Посты
- Авторизация, регистрация
- Представления ввиде функций
- Блог api DRF
- Bootstrap 5

# Установка

### 1) Создать виртуальное окружение

### 2) Установить зависимости

    pip install -r requirements.txt

### 3) Выполнить миграции

## 3) Ввести свои данные в настройках PostgreSQL в settings.py

        'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'yoursite_blog',
        'USER': 'yoursite_user',
        'PASSWORD': 'yoursite_password',
        'HOST': 'localhost',
        'PORT': '5432', 
### 4) Выполнить миграции

### 5) Создать суперпользователя

    python manage.py createsuperuser

# Старт

    python manage.py runserver

