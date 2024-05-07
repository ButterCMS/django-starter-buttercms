# Django + ButterCMS Starter Project

> [!IMPORTANT]
> We officially support Python versions 3.8 to 3.12.

Live demo: [https://django-starter-buttercms-demo.herokuapp.com/](https://django-starter-buttercms-demo.herokuapp.com/)

This Django starter project fully integrates with dynamic sample content from your ButterCMS account, including main menu, pages, blog posts, categories, and tags, and all with a beautiful, custom theme with already-implemented search functionality. All of the included sample content is automatically created in your account dashboard when you 
[sign up for a free trial](https://buttercms.com/join/) of ButterCMS.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/pydanny/cookiecutter-django/)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/ButterCMS/django-starter-buttercms/&env[BUTTERCMS_API_TOKEN]=check%20https://buttercms.com/settings)

## 1) Installation

First, create a virtual environment and install dependencies by running the 
below commands.

```bash
$ git clone https://github.com/ButterCMS/django-starter-buttercms.git
$ cd django-starter-buttercms
$ python3 -m venv butterenv && source butterenv/bin/activate
$ pip install --upgrade pip && pip install -r requirements.txt
```

### 2) Set ButterCMS API Token

To fetch your ButterCMS content, add your API token as an environment variable. 

```bash
$ echo 'BUTTERCMS_API_TOKEN=your_token' >> .env
```

### 3) Run Django Local Development Server

To view the app in the browser, you'll need to run the local development server:

```bash
$ python manage.py runserver
```

Congratulations! Your starter project is now live at: [http://localhost:8000/](http://localhost:8000/)

### 4) Deploy on Heroku

Our starter app can be deployed to Heroku with the click of a button:

1. Create a Heroku account at https://signup.heroku.com.
2. Click the button below and fill in an app name and your Butter API token. Then click "deploy".

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/ButterCMS/django-starter-buttercms/&env[BUTTERCMS_API_TOKEN]=check%20https://buttercms.com/settings)

### 5.) Previewing and Draft Changes

Your starter app allows you to preview draft changes made to content in your
ButterCMS.com account by default; to see draft changes, add '?preview=1' to the end of any 
URL (e.g., http://localhost:8000/?preview=1)
