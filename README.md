# Django Blog project

This project was made to have a functioning Django app with some of the most basic (and some unnecessary but nice) features. The most important goal was to have a boileplate code which can be used later on for new apps in order to get things done quickly.

## Features

- Django 3.0+
- PostgreSQL database support with psycopg2.
- GraphQL support with graphene-django.
- Docker and Docker compose support.
- Nginx support.
- Custom User profiles.
- Blog posts can be written in Markdown.
- Blog posts read number and possibility to upvote.

## How to install without Docker

```bash
$ django-admin.py startproject \
  --template=https://github.com/jpadilla/django-project-template/archive/master.zip \
  --name=Procfile \
  --extension=py,md,env \
  project_name
$ mv example.env .env
$ pipenv install --dev
```

## How to install with Docker and Docker Compose

```bash
$ django-admin.py startproject \
  --template=https://github.com/jpadilla/django-project-template/archive/master.zip \
  --name=Procfile \
  --extension=py,md,env \
  project_name
$ mv example.env .env
$ pipenv install --dev
```

## Environment variables

These are common between environments. The `ENVIRONMENT` variable loads the correct settings, possible values are: `DEVELOPMENT`, `STAGING`, `PRODUCTION`.

```
ENVIRONMENT='DEVELOPMENT'
DJANGO_SECRET_KEY='dont-tell-eve'
DJANGO_DEBUG='yes'
```

These settings(and their default values) are only used on staging and production environments.

```
DJANGO_SESSION_COOKIE_SECURE='yes'
DJANGO_SECURE_BROWSER_XSS_FILTER='yes'
DJANGO_SECURE_CONTENT_TYPE_NOSNIFF='yes'
DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS='yes'
DJANGO_SECURE_HSTS_SECONDS=31536000
DJANGO_SECURE_REDIRECT_EXEMPT=''
DJANGO_SECURE_SSL_HOST=''
DJANGO_SECURE_SSL_REDIRECT='yes'
DJANGO_SECURE_PROXY_SSL_HEADER='HTTP_X_FORWARDED_PROTO,https'
```

## Deployment

## TODO

### Design

* Nicer design to the pages
* Possibly a Vue frontend next to the existing (low prio)
* Custom Admin page (low prio)

### APIs

* Additional GraphQL APIs
* Some meaningful REST APIs: https://testdriven.io/blog/drf-serializers/

### Database

* Remote DB (PostgreSQL) integration
* Redis integration

### Containerize

* Use Docker and Docker Compose: https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

### Async

* Async views: https://testdriven.io/blog/django-async-views/

### Deployment

* Where to host and how to deploy:
    - https://testdriven.io/blog/production-django-deployments-on-heroku/
    - https://testdriven.io/blog/django-digitalocean-app-platform/
    - https://testdriven.io/blog/deploying-django-to-ecs-with-terraform/
    - https://testdriven.io/blog/django-docker-https-aws/
    - https://testdriven.io/blog/deploying-django-to-ec2-with-docker-and-gitlab/
    - https://testdriven.io/blog/deploying-django-to-digitalocean-with-docker-and-github-actions/
* How to make backups

### Authentication

* Social media login: https://testdriven.io/blog/django-social-auth/
* Extend user profile: https://testdriven.io/blog/django-custom-user-model/

### RSS

* https://www.tutorialspoint.com/django/django_rss.htm

### Periodic tasks

* Celery:
    - https://testdriven.io/blog/celery-database-transactions/
    - https://testdriven.io/blog/django-celery-periodic-tasks/
    - https://testdriven.io/blog/django-and-celery/

### Additional functionalities

* Sending emails (High Prio)
* Cookies: https://www.tutorialspoint.com/django/django_cookies_handling.htm (High Prio)
* Caching:
    - https://www.tutorialspoint.com/django/django_caching.htm (High Prio)
    - https://testdriven.io/blog/django-caching/
* Stripe:
    - https://testdriven.io/blog/django-stripe-tutorial/
    - https://testdriven.io/blog/django-stripe-subscriptions/
* Paging or Load more (High Prio)
* Charts: https://testdriven.io/blog/django-charts/

### Documentation

* https://testdriven.io/blog/documenting-python/


# License

The MIT License (MIT)

Copyright (c) 2012-2017 José Padilla

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.