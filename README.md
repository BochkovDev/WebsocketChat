# WebsocketChat
# Реализация сервиса обмена сообщениями с уведомлениями через Telegram

## Описание проекта

Данный проект представляет собой сервис для обмена сообщениями, реализованный с использованием **FastAPI**. Пользователи могут регистрироваться, аутентифицироваться, отправлять сообщения друг другу, а также получать уведомления о новых сообщениях через **Telegram-бота**. 

## Основные функции

- **Регистрация и аутентификация пользователей**: Возможность регистрации новых пользователей и аутентификация при работе с API.
- **Отправка и получение сообщений**: Пользователи могут отправлять сообщения друг другу и получать новые сообщения в реальном времени.
- **Сохранение истории сообщений**: Все сообщения сохраняются в базе данных, с возможностью получения истории переписки.
- **Уведомления через Telegram-бота**: Бот уведомляет пользователя о новом сообщении, если он офлайн.
- **Веб-интерфейс**: Простая веб-страница для взаимодействия с сервисом.

## Технологии

- Язык программирования: Python 3.12
- Фреймворк: FastAPI
- База данных: PostgreSQL
- Кэширование и хранение сессий: Redis
- ORM: SQLAlchemy
- Миграции: Alembic
- Фоновые задачи: Celery
- Контейнеризация: Docker
- Сервер: Nginx

## Структура проекта

```plaintext
.
├── alembic.ini
├── app
│   ├── bot
│   │   ├── dao.py
│   │   ├── __init__.py
│   │   └── models.py
│   ├── chat
│   │   ├── dao.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── router.py
│   │   ├── schemas.py
│   │   └── utils.py
│   ├── core
│   │   ├── celery.py
│   │   ├── __init__.py
│   │   ├── jinja2.py
│   │   └── settings.py
│   ├── dao
│   │   ├── base.py
│   │   └── __init__.py
│   ├── db
│   │   ├── database.py
│   │   ├── __init__.py
│   │   └── sessions.py
│   ├── __init__.py
│   ├── main_bot.py
│   ├── main.py
│   ├── media
│   ├── migrations
│   │   ├── env.py
│   │   ├── README
│   │   ├── script.py.mako
│   ├── services
│   │   ├── __init__.py
│   │   ├── tasks.py
│   │   └── telegram_notification.py
│   ├── static
│   │   ├── css
│   │   │   ├── auth.css
│   │   │   └── chat.css
│   │   └── js
│   │       ├── auth.js
│   │       └── chat.js
│   ├── templates
│   │   ├── auth.html
│   │   └── chat.html
│   └── users
│       ├── auth.py
│       ├── dao.py
│       ├── dependencies.py
│       ├── exceptions.py
│       ├── __init__.py
│       ├── models.py
│       ├── router.py
│       ├── schemas.py
│       └── utils.py
├── docker
│   ├── app
│   │   ├── Dockerfile
│   │   └── server-entrypoint.sh
│   └── nginx
│       ├── default.conf
│       ├── Dockerfile
│       └── nginx.conf
├── docker-compose.yaml
├── README.md
└── requirements.txt

## Установка

1. **Клонируйте репозиторий**:
   ```bash
   git clone git@github.com:BochkovDev/WebsocketChat.git
   cd WebsocketChat
   ```

2. **Настройте окружение `.env/` по свою систему или оставьте как есть**:
   ```plaintext
   SECRET_KEY=your_secret_key
   AUTH_ALGORITHM=your_algorithm
   ACCESS_TOKEN_EXPIRE_MINUTES=your_expiry_time
   ```
   
3. **Настройте Docker и Docker Compose**:
   Убедитесь, что у вас установлены Docker и Docker Compose. Затем запустите проект с помощью Docker:
   ```bash
   docker compose up --build
   ```
   
4. **Создайте базу данных**:
   ```bash
   docker exec -it chitchat.db psql -U postgres(`.env/.env.db:USER`)
   postgres(your_db_user)=# CREATE DATABASE chitchat(`.env/.env.db:NAME`)
   postgres(your_db_user)=# \l --- Проверьте создания базы данных
   ```

## Запуск

После настройки и установки вы можете запустить приложение, используя Docker Compose. Откройте браузер и перейдите по адресу:
```
http://localhost:8000
```
