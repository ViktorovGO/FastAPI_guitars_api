# FastAPI Guitars API

Этот проект представляет собой REST API для управления коллекцией гитар и их брендов, построенный с использованием FastAPI.

## Возможности

- Создание, чтение, обновление и удаление записей о гитарах и их брендах
- Парсинг акустических гитар с сайта muztorg.ru и их запись в БД
- Swagger UI для документации API

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/yourusername/FastAPI_guitars_api.git
    ```
2. Перейдите в директорию проекта:
    ```bash
    cd FastAPI_guitars_api
    ```
3. Запустите docker-compose
    ```bash
    docker-compose up -d
    ```

## Использование

1. Откройте браузер и перейдите по адресу http://127.0.0.1:8000/docs, чтобы получить доступ к Swagger UI.

## Обновление данных

1. Парсинг с сайта muztorg.ru
    ```bash
    python src/scripts/get_guitars.py
    ```
2. Запись полученных данных в БД
    ```bash
    python src/scripts/guitars_to_db.py
    ```

## Вклад

Приветствуются любые вклады! Пожалуйста, откройте issue или отправьте pull request.

## Лицензия

Этот проект лицензирован по лицензии MIT.