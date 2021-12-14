# Django + ButterCMS Starter Project

This Django starter project fully integrates with dynamic sample content from your ButterCMS account, including main menu, pages, blog posts, categories, and tags, and all with a beautiful, custom theme with already-implemented search functionality. All of the included sample content is automatically created in your account dashboard when you 
[sign up for a free trial](https://buttercms.com/join/) of ButterCMS.


[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/pydanny/cookiecutter-django/)


## 1) Installation

First, create a virtual environment and install dependencies by running the 
below commands. *(Note: This project requires pip wheel. Depending on
your version of pip, wheel may not be included; therefore, the command to install wheel is given below.)*

```bash
$ git clone https://github.com/ButterCMS/django-starter-buttercms.git
$ python3 -m venv butterenv
$ source butterenv/bin/activate
$ pip install wheel
$ pip install -r requirements/local.txt
```

### 2) Set Database Environmental Variable

Because all of your data is fetched from Butter, there's no need for a database
at this time (although you can of course set one up later!). For now, set the
DATABASE_URL environmental variable to skip Django database creation and checks.

```bash
$ echo 'DATABASE_URL=sqlite:///database.sqlite' >> .env
```

### 3) Set ButterCMS API Token

To fetch your ButterCMS content, add your API token as an environment variable. 

```bash
$ echo 'BUTTERCMS_API_TOKEN=your_token' >> .env
```

### 4) Run Django Local Development Server

To view the app in the browser, you'll need to run the local development server:

```bash
$ python manage.py runserver
```

## 5. Deploy on Heroku

Your starter app can be deployed to a host like Heroku
in just a few steps:


1. Create a Heroku account at https://signup.heroku.com
2. Download [the CLI](https://devcenter.heroku.com/articles/heroku-cli):

Ubuntu 16+:
```bash
$ curl https://cli-assets.heroku.com/install.sh | sh
```

MacOS:
```bash
$ brew tap heroku/brew && brew install heroku

```
3. Heroku create
$ heroku config:set DISABLE_COLLECTSTATIC=1
$ heroku config:set DJANGO_SECRET_KEY="YOUR_SECRET_KEY_VALUE"
$ echo "web: gunicorn config.wsgi --log-file -" >> Procfile

REDIS  URL why?
$ heroku config:set DJANGO_ADMIN_URL="admin"
$ heroku config:set DJANGO_ALLOWED_HOSTS=".herokuapp.com"





4. git push heroku main
3. Add the API key as a secret `vercel secrets add butter-cms-api-key "YOUR_API_KEY"`
4. Run `vercel` at the project root
[ End Example Steps ]
[ End Optional Step - Quick Deployment ]
-->
