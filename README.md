<!-- Before starting to use this template, find and replace occurences of ABC with your repo name (case sensitive) -->
<!-- Inspired from: https://github.com/mindwebs/nodets-api-template-->

<div align="center">
  <h1>Project ABC</h1>
  <h3>One line description of ABC</a></h3>
</div>

## Contents

-   [Contents](#contents)
-   [Description](#description)
    -   [What's the problem we are trying to solve?](#whats-the-problem-we-are-trying-to-solve)
    -   [How can ABC help?](#how-can-abc-help)
    -   [The idea](#the-idea)
-   [Project structure](#project-structure)
-   [Project roadmap](#project-roadmap)
-   [Getting started](#getting-started)
    -   [Prerequisites](#prerequisites)
        -   [Softwares needed](#softwares-needed)
        -   [Knowledge needed](#knowledge-needed)
    -   [Installing](#installing)
-   [Future Scope](#future-scope)
-   [Built with](#built-with)
-   [Contributing](#contributing)
-   [Authors](#authors)

## Description

\_

### What's the problem we are trying to solve?

\_

### How can ABC help?

\_

### The idea

\_

## Project structure

The current project structure is as follows:

```
  ├── .github/                    scripts and configs for github templating and workflows
  ├── app/
      ├── models/                 Pydantic validation models go here
      ├── routes/                 Routes or endpoint definitions go here, routes make calls to controllers
          ├── predict.py          Router for model predict functions
      ├── predict/                Specify Abstract classes for models and predict functions here
      ├── dependencies.py         Add dependencies
      ├── utils.py                utility or helper functions go here
      ├── main.py                 Entry point for our server
  ├── tests/                      directory for endpoint testing
      ├── conftest.py             Add pytest fixtures
  ├── .env                        environment variables used in the project (can be later bifurcated into prod and dev)
  ├── .gitignore                  stores files and directories to be ignored in commits
  ├── docker-compose.prod.yml     config file to define containers (for prod)
  ├── docker-compose.yml          config file to define containers
  ├── Dockerfile                  Docker commands to create the docker image go here
  ├── README.md                   details and instructions about the project go here
  ├── .pre-commit-config.yaml     Specifies pre-commit hooks and linters for code sanctity
  └── requirements.txt            file for keeping track of python dependencies
```

## Project roadmap

\_

## Getting started

\_

### Prerequisites

#### Softwares needed

\_

#### Knowledge needed

\_

### Installing

\_

## Future Scope

\_

## Built with

**Backend:**

-   [FastAPI](https://fastapi.tiangolo.com/lo/) - An async web framework for python.
-   [Uvicorn](https://www.uvicorn.org/) - An ASGI web server, for python.
-   [Docker](https//docker.com)

## Contributing

Please read [contributing.md](https://github.com/mindwebs/.github/contributing.md) for details on our code committing guidelines.

## Authors

<a href="https://mwv.one">
  <img src="https://avatars.githubusercontent.com/u/56452701?s=200&v=4" />
</a>
