# Django Blog project

## Goals

* A functioning app made with Django framework, connecting to an SQL database with ORM.
* A functioning blog with the most important basic features, and some unnecessary but nice ones.
* An app that uses several important features of Bootstrap v5.
* A boilerplate whose parts can be used in future Django apps to get started quickly.
* An app that can be used with Docker, docker-compose and perhaps with Kubernetes.


## Features

- Django 3.0+
- PostgreSQL database support with psycopg2.
- GraphQL support with graphene-django.
- Docker and Docker Compose support, separate environment for Dev and Prod instances, and linting.
- Nginx support.
- Authentication and user profiles with custom fields (including profile photo upload).
- Blog posts can be written in Markdown and displayed as HTML.
- Custom authentication/registration templates.
- Send email when password change requested.
- Count blog posts read number and possibility to upvote posts.
- Collect statistics with a REST API (e.g. daily).
- Customized Django Admin interface.
- RSS and sitemap.
- Sending email at registration.
- Load data from json.

## Installation and setup

### How to setup virtual environment

```bash
$ mkdir ~/django && cd ~/django

# install virtual env
$ pip3 install virtualenv

# create new virtual env
$ virtualenv django_app

# start virtualenv
$ source django_app/bin/activate
```

### How to get code from GitHub

```bash
$ cd ~/django
$ git clone https://github.com/Attila-Sasvari/django_blog.git
$ cd django_blog
```

### How to install without Docker

```bash
$ cd ~/django/django_blog

# activate virtual env
$ source django_app/bin/activate

# install dependencies
$ pip3 install -r requirements.txt

# one time actions to setup database and static files
$ python manage.py makemigrations
$ python manage.py migrate --noinput
$ python manage.py collectstatic --no-input --clear

# execute only if you want two default user and one blog post
$ python manage.py loaddata fixtures_pretty.json

# create super user account
$ python manage.py createsuperuser

# run the app
$ python manage.py runserver
```

### How to install Dev environemtn with Docker and Docker Compose

```bash
$ cd ~/django/django_blog
$ docker-compose -f docker-compose.yml up -d --build

# one time actions to setup database and static files
$ docker-compose -f docker-compose.yml exec web python manage.py makemigrations
$ docker-compose -f docker-compose.yml exec web python manage.py migrate --noinput
$ docker-compose -f docker-compose.yml exec web python manage.py collectstatic --no-input --clear

# execute only if you want two default user and one blog post
$ docker-compose -f docker-compose.yml exec web python manage.py loaddata fixtures_pretty.json
```

Notes:
- For production environment, use the same commands, but instead of `docker-compose.yml`, use `docker-compose.prod.yml`.
- If you need an admin and an other staff users in the database, as well as a blog post, execute the `python manage.py loaddata fixtures_pretty.json` as mentioned above. The user `admin` the following password assigned: `admin123`. No need to say that you should change that.


### How to connect to the database

```bash
$ docker-compose exec db psql --username=hello_django --dbname=hello_django_dev

```

### How to check logs when run with Docker Compose

```bash
$ docker-compose -f docker-compose.yml logs

# logs of the web container
$ docker-compose logs django_blog_web_1

# logs of the db container
$ docker-compose logs django_blog_db_1
```

This setup was inspired by [this article](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/).

### Environment variables

If Docker is used, then `.env.dev` is used for Dev environment, `.env.prod` along with `.env.prod.db` are used for Prod environment.

If Docker is not used, then the default SQLite database is created (instead of PostgreSQL) with default values.

### Removing resources with Docker

```bash
# stop all running container
docker stop $(docker ps -a -q)

# remove all containers
docker rm -f $(docker ps -a -q)

# remove image
docker rmi <container_name_or_id>

# remove everything
docker system prune -a
```

### Deployment

So far no deployment has been done on any of the major cloud providers, so here is a list of articles talking about different deployment workflows.

- https://testdriven.io/blog/production-django-deployments-on-heroku/
- https://testdriven.io/blog/django-digitalocean-app-platform/
- https://testdriven.io/blog/deploying-django-to-ecs-with-terraform/
- https://testdriven.io/blog/django-docker-https-aws/
- https://testdriven.io/blog/deploying-django-to-ec2-with-docker-and-gitlab/
- https://testdriven.io/blog/deploying-django-to-digitalocean-with-docker-and-github-actions/


## TODO

Below is a big list of potential features to implement in the future.

### Design updates

* Vue frontend that gets data from Django app through GraphQL or REST API. Prerequisite:
    - add more REST API or GraphQL endpoints.
* Further customize the admin page. Some idea:
    - Custom icon and colors.

### APIs

* Additional GraphQL APIs.
* Some meaningful REST APIs: https://testdriven.io/blog/drf-serializers/

### Database

* Redis integration to cache data:
    - https://realpython.com/caching-in-django-with-redis/
    - https://testdriven.io/blog/django-caching/

### Async

* Async views: https://testdriven.io/blog/django-async-views/

### Authentication

* Social media login: https://testdriven.io/blog/django-social-auth/

### Periodic tasks

* Celery:
    - https://testdriven.io/blog/celery-database-transactions/
    - https://testdriven.io/blog/django-celery-periodic-tasks/
    - https://testdriven.io/blog/django-and-celery/


### Additional functionalities

* Stripe:
    - https://testdriven.io/blog/django-stripe-tutorial/
    - https://testdriven.io/blog/django-stripe-subscriptions/
* Charts for dashboard: https://testdriven.io/blog/django-charts/
* Use Makefile: https://docker-handbook.farhan.dev/containerizing-a-multi-container-javascript-application#writing-management-scripts
* Enhance Docker Compose files: https://docker-handbook.farhan.dev/composing-projects-using-docker-compose
* Implement basic Kubernetes setup: https://www.freecodecamp.org/news/the-kubernetes-handbook/


### Documentation

* https://testdriven.io/blog/documenting-python/


## License

The MIT License (MIT)

Copyright 2021 Attila Sasv??ri

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.