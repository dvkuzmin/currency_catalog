# Сервис-справочник курса валют

## Базовые технологии проекта

- Python 3.11
- Django 5.0
- 
## Инструкция по развертыванию тестового проекта

### Настройка проекта

Склонируйте репозиторий:

```bash
git clone https://github.com/dvkuzmin/currency_catalog.git
```

Создайте виртуальное окружение, затем выполните команду:

```bash
pip install -r requirements.txt
```


В корне репозитория выполните команду:

```bash
python ./manage.py load_currency_data
```


В корне репозитория выполните команду:

```bash
python ./manage.py load_currency_data
```


#### Создание миграций, применять только при разработке:

```bash
python ./manage.py makemigrations
```

#### Применение миграций:

```bash
python ./manage.py migrate
```

#### Создание суперпользователя

```bash
python ./manage.py createsuperuser
```

#### Запуск сервера приложения

```bash
python ./manage.py runserver
```

### HTTP API

- /show_rates/ - Get-запрос на получение календаря
- show_rates/?date=2024-05-15 - Get-запрос на получение курса валют в выбранную дату
