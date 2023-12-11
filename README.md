# DJANGO проект

Этот проект представляет собой простое REST API для управления задачами. Каждая задача имеет заголовок, описание, статус (выполнено/не выполнено) и дату создания.

## Установка

1. Клонировать репозиторий:

   ```bash
   git clone https://github.com/yourusername/your-task-manager.git
   cd your-task-manager

2. Установить зависимости:
    ```bash
    pip install -r requirements.txt
   
3. Выполнить миграции:
    ```bash
    python manage.py migrate
4. Запустить сервер:
    ```bash
   python manage.py runserver

## Использование
   
1. Использовать средство для отправки запросов (например: Insomnia)
2. Выполнить запрос на нужный Endpoint.

### Документация к API  файле DOCUMENTATION.md

###### SECRET_KEY не стал скрывать, чтобы вам было легче запустить проект
   