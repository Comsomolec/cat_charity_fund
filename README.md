# QR_Kot

## Цель
Данный проект является учебным и создан в рамках обучения на курсе Python-Backend.
Работа с фреймворком FastAPI.

## Описание и справка по использованию
Проект представляет готовое приложение/шаблон для Благотворительного фонда.
Позволяет открывать новые благотворительные проекты.
Принимать и распределять пожертвования.

## Используемые Технологии
- Python
- FastAPI
- Sqlalchemy
- pydantic
- JWT

## Документация
Для просмотра документации
* Скачайте файл openapi.json из корневой директории проекта
* <a href="https://redocly.github.io/redoc/" target="_blank">Зайдите на сайт</a>
* Вверху страницы есть кнопка Upload a file, нажмите её и загрузите скачанный файл


## Как запустить проект
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Comsomolec/cat_charity_fund.git
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создаем в корневой директории проекта .env файл и заполняем согласно шаблону env-example из проекта

```
touch .env
```

### Создаем базу данных

Создание базы

```
alembic init --template async alembic
```

Первая миграция
```
alembic revision --autogenerate -m "First migration"
```

Применение изменений (перед запуском проверьте файл миграции в папке ../alembic/versions)
```
alembic upgrade head
```

### Запуск
```
uvicorn app.main:app --reload
```