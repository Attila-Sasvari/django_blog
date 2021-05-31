# pull the official docker image
FROM python:3.9.5-slim

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update && \
    apt-get install -y netcat && \
    apt-get install -y --no-install-recommends gcc

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .

EXPOSE 8000 

ENTRYPOINT ["/app/entrypoint.sh"]