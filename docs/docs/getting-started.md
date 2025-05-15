# Getting Started

This guide will help you set up the Monument Recommendation System on your local machine.

## Prerequisites

Make sure you have the following installed:

* Docker
* Docker Compose

## Clone the Repository

```bash
git clone https://github.com/username/monumentrecommendation.git
cd monumentrecommendation
```

## Set Up Environment Variables

Create a `.env` file in the root of the project with the following contents:

```
MYSQL_DATABASE=monuments
MYSQL_USER=user
MYSQL_PASSWORD=password
MYSQL_ROOT_PASSWORD=rootpassword
```

## Start the Services

Use Docker Compose to start all services:

```bash
docker-compose up
```

Run in detached mode:

```bash
docker-compose up -d
```

## Access the Services

* FastAPI API: [http://localhost:8000](http://localhost:8000)
* Swagger Docs: [http://localhost:8000/docs](http://localhost:8000/docs)
* MkDocs Documentation: [http://localhost:8001](http://localhost:8001)

## Stop the Services

```bash
docker-compose down
```

To also remove volumes:

```bash
docker-compose down -v
```
