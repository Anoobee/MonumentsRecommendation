# MonumentRecommendation

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

This is a rule based recommendation system for monuments

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for
│                         monumentrecommendation and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── monumentrecommendation   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes monumentrecommendation a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling
    │   ├── __init__.py
    │   ├── predict.py          <- Code to run model inference with trained models
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```
# Getting Started

This guide will help you set up the Monument Recommendation System on your local machine.

## Prerequisites

Make sure you have the following installed:

- Docker
- Docker Compose

## Clone the Repository

```bash
git clone https://github.com/Anoobee/MonumentsRecommendation
cd MonumentsRecommendation
```

## Set Up Environment Variables

Create a `.env` file in the root of the project with the following contents:

```bash
MYSQL_DATABASE=monuments
MYSQL_USER=user
MYSQL_PASSWORD=password
MYSQL_ROOT_PASSWORD=rootpassword
```

## Start the Services

Use Docker Compose to start all services:

```bash
docker compose up
```

Run in detached mode:

```bash
docker compose up -d
```

## Access the Services

- FastAPI API: [http://localhost:8000](http://localhost:8000/)
- Swagger Docs: http://localhost:8000/docs
- MkDocs Documentation: [http://localhost:8001](http://localhost:8001/)

## Stop the Services

```bash
docker compose down
```


--------
