# Django News App

A Django back-end for publishing and retrieving news articles through a REST API. Uses the django admin
interface for creating, updating and publishing news articles and a [Django REST framework](https://www.django-rest-framework.org) based API.


## Usage

Clone the repo:

`
    git clone https://github.com/kudasav/django-news-app
`

Create a .env file with the following [environment variables](#environment-variables) in the root directory of the application

Run the following commands to set up the application:

Install the required packeges:

`
    pip instll -r requirements.txt
`

Create an admin user account:

`
    python manage.py createsuperuser
`

Start the development server:

`
    python manage.py runserver
`


## Environment variables

Before starting the development server the following environment variables must be created in a .env
file in the root directory of the project.

| Variable      | Description    |
| ------------- |:-------------- |
SECRET_KEY      | A secret key for securely signing and encrypting data, must be a minimum of 50 characters in length |
ALLOWED_HOSTS   | Comma separated values for the django ALLOWED_HOSTS setting. e.g. "localhost,127.0.0.1" |

Environment variables for deploying the application using docker containers.

| Variable        | Description    |
| -------------   |:-------------- |
VIRTUAL_HOST      | The domain name to assign to the application.|
LETSENCRYPT_EMAIL | The email address to assign to the [letsencrypt-nginx-proxy-companion](https://hub.docker.com/r/jrcs/letsencrypt-nginx-proxy-companion)               |

## API Documentation

The api documentation and Swagger/OpenAPI 2.0 specification for the REST API can be accessed from the /docs/ url of the application. 

The documentation is auto genarated using [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/readme.html#installation)

## Deployment

The application can be deployed using [Docker](https://www.docker.com)

The dockerfile and docker compose files can be found in the root folder of the application.