release: python3 manage.py migrate
web: gunicorn recipe.wsgi --log-file --settings=settings.base -