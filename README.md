# airflow-dev
Local development environment for creating and testing Airflow DAGs

#### Table of Contents
* [Requirements](#requirements)
* [Project structure](#project-structure)
* [Running the environment](#running-the-environment)
* [Running tests locally](#running-tests-locally)


## Requirements

- docker
- docker-compose

## Project structure

- `docker-compose.yml` - configuration file for the docker-compose
- `dags` - will contain all our dags
- `lib` - will contain all our custom code
- `test` - will contain our pytests
- `.env `- file with environment variables that we wish to include the containers

## Running the environment

```bash
docker-compose up -d
docker-compose exec -T webserver airflow initdb # Only once
```

Let's open the (http://localhost:8080)


## Running tests locally

```
docker-compose exec -T webserver pytest
```




