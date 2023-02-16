# Stripe Shop

  Для разработки использован стартовый темплейт django-cookiecutter и немного доработан.

  Реализовано:
    - Обработка checkout оплаты в payments/ + тестирование
      - + тесты
    - Модели товаров и заказов в shop/products/
      - + тесты
    - Использован докер
    - Модели добавлены в админ


## TODO

- Модель Order и сохранение результата

## Установка

---

## Без докера
  - Создать виртуальное окружение
  - Закоментить hiredis в requirements/base.txt
  - pip install -r requirements/local.txt
  - Добавить .env или переименовать example.env
    - Обновить DATABASE_URL
    - Обновить STRIPE_PUBLIC_KEY
    - Обновить STRIPE_SECRET_KEY
  - Провести миграции
    - `python manage.py migrate`
  - Создать суперюзера
    - `python manage.py createsuperuser`
  - Создание тестовых данных
    - Создать
      - `python manage.py runscript create_items`
    - Удалить
      - `python manage.py runscript delete_items`
  - Проверить выполнение тестов
    - `pytest`
  - Запустить сервер
    - `python manage.py runserver`

## С докером
  - Обновить stripe ключи в `.env/.local/.django`
  - Провести миграции (если потребуется)
    - `docker-compose -f local.yml run --rm django python manage.py migrate`
  - Создать суперюзера
    - `docker-compose -f local.yml run --rm django python manage.py createsuperuser`
  - Создание тестовых данных
    - Создать
      - `docker-compose -f local.yml run --rm django python manage.py runscript create_items`
    - Удалить
      - `docker-compose -f local.yml run --rm django python manage.py runscript delete_items`
  - Проверить выполнение тестов
    - `docker-compose -f local.yml run --rm django pytest`
  - Запустить докер
    - `docker-compose -f local.yml up --build`
