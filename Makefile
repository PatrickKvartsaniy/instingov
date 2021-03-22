export PIPENV_VERBOSITY=-1

deps:
	pipenv sync
	pipenv update

run:
	pipenv run gunicorn -c config/gunicorn.py website.wsgi

daemon:
	pipenv run gunicorn -c config/gunicorn.py website.wsgi --daemon

container:
	docker build .

statics:
	pipenv run python manage.py collectstatic

migrate:
	pipenv run python manage.py makemigrations
	pipenv run python manage.py migrate