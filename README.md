# Django Starter ButterCMS

Django starter project using ButterCMS. The project uses the sample content that is automatically created when you
create your free trial account on ButterCMS.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/pydanny/cookiecutter-django/)

## Installation

Prepare a virtual environment and install the project requirements.

```bash
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements/local.txt
```

### Set API Token

To fetch your ButterCMS content, add your API token as an environment variable. Set `BUTTERCMS_API_TOKEN=<Your API Token>` in `.env`. Get [your free API token](https://buttercms.com/join/).

```bash
$ echo 'BUTTERCMS_API_TOKEN=your_token' >> .env
```

### Run the local server

```bash
$ python manage.py runserver
```

Your starter is live: [http://localhost:8000](http://localhost:8000) !