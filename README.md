# Stripe Shop

  Для разработки использован стартовый темплейт django-cookiecutter и немного доработан.

  Обработка оплаты в payments/
  Модели товаров и заказов в shop/products/
  Написаны тесты
  Использован докер
  Модели добавлены в админ


## TODO



## Установка

---

1. Без докера
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
  - Запустить сервер
    - `python manage.py runserver`

2. С докером
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
  - Запустить докер
    - docker-compose -f local.yml up --build



### Полезные команды:

    # containers status
    docker-compose -f local.yml ps

    # containers logs
    docker-compose -f local.yml logs

    # remove unused(dangling) images
    docker image prune

    # django shell run
    docker-compose -f local.yml run --rm django python manage.py shell

    # django dump db data
    docker-compose -f production.yml run --rm django bash
    python -Xutf8 manage.py dumpdata {app}.{Model -o data.json
      # Открыть вторую консоль, сохраняя сессию в старой
      docker cp 5f5cecd3798e:/app/data.json ./data.json

    # If you want to scale application
    # ❗ Don’t try to scale postgres, celerybeat, or traefik
    docker-compose -f production.yml up --scale django=4
    docker-compose -f production.yml up --scale celeryworker=2
