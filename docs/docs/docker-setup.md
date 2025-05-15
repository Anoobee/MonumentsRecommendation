# Docker Setup

The project uses Docker and Docker Compose for easy deployment and development.

## Prerequisites

* Docker
* Docker Compose

## Configuration

1. Create a `.env` file in the project root with the following content:

```
MYSQL_DATABASE=monuments
MYSQL_USER=user
MYSQL_PASSWORD=password
MYSQL_ROOT_PASSWORD=rootpassword
```

## Running the Services

Start all services (database, API, and documentation):

```bash
docker-compose up
```

To run in detached mode:

```bash
docker-compose up -d
```

## Accessing Services

* FastAPI application: [http://localhost:8000](http://localhost:8000)
* API documentation (Swagger UI): [http://localhost:8000/docs](http://localhost:8000/docs)
* Project documentation (MkDocs): [http://localhost:8001](http://localhost:8001)

## Building Images

If you need to rebuild the images:

```bash
docker-compose build
```

## Stopping Services

Stop all services:

```bash
docker-compose down
```

To stop and remove volumes:

```bash
docker-compose down -v
```
