# Stripe Shop

  Для разработки использован стартовый темплейт django-cookiecutter и немного доработан.

## TODO

- Деплой
- Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме.
- Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items
- Реализовать не Stripe Session, а Stripe Payment Intent.

## Реализовано

---

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


## Deployment

---

### First steps

1. Создать желаемый VPS

2. Подключить домен к VPS

   1. Обновить указатели домена `ns.*`
   2. Добавить запись `CNAME` (если потребуется)

3. Подключиться по SSH (putty или консоль)
   1. `ssh user@host-ip`

### Setup VPS

1. Обновить linux/ubuntu сервер

   - `sudo apt update && sudo apt upgrade -y`

2. Обновить часовой пояс

   1. Проверить текущее время
      - `timedatectl`
   2. Доступные пояса
      - `timedatectl list-timezones`
   3. Задать часовой пояс
      - `sudo timedatectl set-timezone Europe/Moscow`

3. Установить Supervisor
   - `sudo apt-get -y install supervisor`
   - `sudo systemctl enable supervisor`
   - `sudo systemctl start supervisor`

4. Установить python, pip, git, venv
   - `sudo apt install python3.10`
   - `sudo apt install python3-pip`
   - `apt install python3.10-venv`
   - `sudo apt install git`
   -
   - `sudo apt install python3.10 python3-pip git -y`

5. Установить Docker
   - Инструкция [Docker ubuntu](https://docs.docker.com/engine/install/ubuntu/)
   - На джино это упрощенно, через Пакеты приложений + опцию iptables
   - Проверка: `docker run hello-world`

6. Создать нового пользователя
   - `adduser USER` - находится в home/USER
   - `gpasswd -a USER sudo` - добавить sudo права
   - `su - USER` - сменить пользователя

7. Создать ssh ключи
   - `ssh-keygen`
   - Добавить публичный ключ vps в github ssh `{repo}/settings/keys/new`


### Setup Project

1. Инициализация git и Пулл проекта
   - `mkdir PROJECT`
   - `cd PROJECT`
   - `git init`
   - `git remote add origin git@github.com:DmitryPi/stripe-test.git`
   - `git pull origin main`

2. Установка и настройка venv или [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) (Если потребуется)

   1. venv
      - `apt install python3.10-venv`
      - `python3 -m venv venv`
      - `chmod +x venv/bin/activate` - предоставить права
      - `venv/bin/activate`
   2. virtualenvwrapper
      - `pip install virtualenvwrapper`
      - `export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.10`
      - `export WORKON_HOME=~/Envs`
      - `export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv`
      - `source /usr/local/bin/virtualenvwrapper.sh`

2. Добавить переменные production в `.envs/.prod`

3. Билд docker проекта

   1. Билд
      - `docker-compose -f production.yml build`
   2. Миграция бд
      - `docker-compose -f production.yml run --rm django python manage.py migrate`
   3. Создать суперюзера
      - `docker-compose -f production.yml run --rm django python manage.py createsuperuser`
   4. Запуск
      - `docker-compose -f production.yml up`
   5. Ребилд
      - `docker-compose -f production.yml up --build`

4. Проверить логин/регистрацию

5. Проверить mailgun/sentry

6. supervisord
   1. Установка
      `pip install supervisor`
   2. Старт
      - `supervisord`
   3. Стоп
      - `supervisorctl stop all`
      - `sudo unlink /tmp/supervisor.sock` или `sudo unlink /var/run/supervisor.sock`
   4. Дополнительные команды
      - `supervisorctl status`

### Полезные команды:

    # containers status
    docker-compose -f production.yml ps

    # containers logs
    docker-compose -f production.yml logs

    # remove unused(dangling) images
    docker image prune

    # django shell run
    docker-compose -f production.yml run --rm django python manage.py shell

    # django dump db data
    docker-compose -f production.yml run --rm django bash
    python -Xutf8 manage.py dumpdata {app}.{Model -o data.json
      # Открыть вторую консоль, сохраняя сессию в старой
      docker cp 5f5cecd3798e:/app/data.json ./data.json

    # If you want to scale application
    # ❗ Don’t try to scale postgres, celerybeat, or traefik
    docker-compose -f production.yml up --scale django=4
    docker-compose -f production.yml up --scale celeryworker=2

### Возможные ошибки:

1. ACME certificate failure

   - Возможен конфликт хост сервиса, если он предоставляет функцию ssl сертификации
   - Let's encrypt рейт лимит достигнут (5 в неделю) - [проверить](https://crt.sh/)

2. ERR_TOO_MANY_REDIRECTS

   - Происходит из-за рекурсии портов 80<-->443(http-https)

3. Traefik 404 error

   - Конфликт ssl-сертификатов или отсутствие выделенного IP
      - Анализ: изменить лог-левел на DEBUG в traefik.yml
      - Решение: убрать tls настройки из traefik.yml, купить выделенный ip

4. Django POST 403 csrf - Origin checking failed
   - В production.py обновить CSRF_TRUSTED_ORIGINS
