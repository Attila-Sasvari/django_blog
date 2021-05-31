# Commands

Create resource

## From Dockerfile

```
# build image from Dockerfile
docker build . -t django-webapp -f ./Dockerfile
docker build -f ./Dockerfile -t django_blog:latest .

# start container from image
docker run -di -p 8000:8000 django-webapp
```

## From docker compose

```

docker-compose -f docker-compose.yml up -d --build
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear

# bring down
docker-compose -f docker-compose.prod.yml down -v

# check logs
docker-compose -f docker-compose.prod.yml logs -f

# connect to postgresql
docker-compose exec db psql --username=django_traefik --dbname=django_traefik
```

## Stop and remove resource

```
# stop all running container
docker stop $(docker ps -a -q)
# remove all containers
docker rm -f $(docker ps -a -q)
# remove image
docker rmi <container_name_or_id>
# remove everything
docker system prune
```


# Links

[https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes](https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes)




  677  docker build -f ./Dockerfile -t hello_django:latest .
  678  docker-compose ps
  679  docker-compose ps -a
  680  docker logs
  681  docker logs django_blog_web_1
  682  docker build -f ./Dockerfile -t hello_django:latest .
  683  docker ps
  684  docker ps -a
  685  docker-compose exec web python manage.py migrate --noinput
  686  docker ps -a
  687  docker-compose up django_blog_web_1
  688  docker compose up django_blog_web_1
  689  docker compose start django_blog_web_1
  690  docker compose start bf4954c928d4
  691  history
  692  docker-compose up -d --build
  693  docker-compose up -d --build
  694  docker compose ps
  695  docker ps
  696  docker-compose exec web python manage.py migrate --noinput
  697  winpty docker-compose exec web python manage.py migrate --noinput
  698  docker-compose exec db psql --username=hello_django --dbname=hello_django_dev
  699  winpty docker-compose exec db psql --username=hello_django --dbname=hello_django_dev
  700  docker volume inspect django-on-docker_postgres_data
  701  docker volume
  702  docker volume ls
  703  docker volume inspect django_blog_postgres_data
  704  \q
  705  history | grep log
  706  docker logs django_blog_web_1
  707  docker ps
  708  docker-compose exec web python manage.py flush --no-input
  709  winpty docker-compose exec web python manage.py flush --no-input
  710  winpty docker-compose exec web python manage.py migrate
  711  history
