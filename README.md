# SuperBook

SuperBook is a social network for superheroes built with [Python][0] using the [Django Web Framework][1]. This is an example project accompanying the book "Django Design Patterns and Best Practices" by Arun Ravindran.


[0]: https://www.python.org/
[1]: https://www.djangoproject.com/

# Local Installation

Git clone to a local directory:

```
git clone https://github.com/DjangoPatternsBook/superbook2.git
```

[Install pipenv system-wide or locally](https://docs.pipenv.org/) but outside a virtualenv. Alternatively, follow these commands:

```
$ pip install -U pip
$ pip install pipenv
```

Now go to the project directory and install the dependencies:
```
$ cd superbook2
$ pipenv install --dev
```

Now you need to enter the pipenv shell:

```
$ pipenv shell
```

Run the project:
```
$ cd src
$ python manage.py migrate
$ python manage.py loaddata initial-fixture.json
$ python manage.py runserver
```

Open your browser and visit http://127.0.0.1:8000/ (or the URL shown in the last command). If you performed loaddata, then you can login using the username: "admin" and password: "admin".

# Deployment to Heroku

Enter project root and run the following commands:

```
$ heroku create superbook-demo
$ heroku addons:create heroku-postgresql:hobby-dev
$ heroku config:set DJANGO_SETTINGS_MODULE=superbook.settings.production
$ git push heroku master
```
