# Stripe Shop

  Для разработки использован стартовый темплейт django-cookiecutter и немного доработан.

## TODO

- Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме.
- Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items
- Реализовать не Stripe Session, а Stripe Payment Intent.

## Реализовано

---

  - Настроить деплой
  - Обработка checkout оплаты в payments/ + тестирование
  - Модели товаров и заказов в shop/products/ + тестирование
  - Использован докер
  - Использованы переменные окружения
  - Модели добавлены в админ
  - Конвертация прайса в соответствии с выбором пользователя

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
