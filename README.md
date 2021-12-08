# Django + ButterCMS Starter Project

This Django starter project fully integrates with dynamic sample content from your ButterCMS account, including main menu, pages, blog posts, categories, and tags, and all with a beautiful, custom theme with already-implemented search functionality. All of the included sample content is automatically created in your account dashboard when you 
[sign up for a free trial](https://buttercms.com/join/) of ButterCMS.


[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/pydanny/cookiecutter-django/)


## 1) Installation

First, create a virtual environment and install dependencies by running the 
below commands. *(Note: This project requires pip wheel. Depending on
your version of pip, wheel may not be included; therefore, the command to install wheel is given below.)*

```bash
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

To fetch your ButterCMS content, add your API token as an environment variable. You can find it in your butterCMS account under settings -> API Token. (If you don't already have a ButterCMS account, you can get one free [here](https://buttercms.com/join/).) 

```bash
$ echo 'BUTTERCMS_API_TOKEN=your_token' >> .env
```

### 4) Run Django Local Development Server

To view the app in the browser, you'll need to run the local development server:

```bash
$ python manage.py runserver
```

Congratulations! Your starter project is now live and can be viewed at [http://127.0.0.1:8000/](http://127.0.0.1:8000/) !