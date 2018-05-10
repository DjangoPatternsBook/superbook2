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
$ python manage.py createsuperuser
$ python manage.py runserver
```

Open your browser and visit http://127.0.0.1:8000/ (or the URL shown in the last command)

# Deployment to Heroku

Make sure the following environment variables are set in Heroku
* DATABASE_URL (already set to something like postgres://yqjhfpkrc... if you enable the add-on)
* DEBUG (False but can be True for debugging)
* SECRET_KEY
* ALLOWED_HOSTS (for e.g. superbook-demo.herokuapp.com)

Enter project root
```
git push heroku master

export DEBUG="True"
export DATABASE_URL="sqlite:////tmp/test.db"
gunicorn src.superbook.wsgi --log-file - --pythonpath "./src"

heroku run python src/manage.py migrate --settings "src.superbook.settings.production" -v 3
heroku run python src/manage.py createsuperuser --settings "src.superbook.settings.production"

```
