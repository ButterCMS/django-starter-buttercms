# Django Starter ButterCMS

Django starter project using ButterCMS. The project uses the sample content that is automatically created when you
create your free trial account on ButterCMS.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/pydanny/cookiecutter-django/)

## 1) Installation

Create a virtual environment and install project requirements.

```bash
$ python3 -m venv butterenv
$ source butterenv/bin/activate
$ pip install -r requirements/local.txt
```

### 2) Set ButterCMS API Token

Get [your free ButterCMS API token](https://buttercms.com/join/). To fetch your ButterCMS content, add your API token as an environment variable. Set `BUTTERCMS_API_TOKEN=<Your API Token>` in `.env`. .

To fetch your ButterCMS content, add your API token as an environment variable. You can find it in your ButterCMS [account settings](https://buttercms.com/settings/). If you don't already have a ButterCMS account, [get one for free](https://buttercms.com/join/).


```bash
$ echo 'BUTTERCMS_API_TOKEN=your_token' >> .env
```

### 3) Run Django Local Development Server

```bash
$ python manage.py runserver
```

Your starter is live [http://127.0.0.1:8000/](http://127.0.0.1:8000/) !