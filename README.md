# Stripe Shop

  Для разработки использован стартовый темплейт django-cookiecutter и немного доработан.


## TODO



## Установка

---

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