export PIPENV_VERBOSITY=-1

deps:
	pipenv sync
	pipenv update

run:
	gunicorn -c config/gunicorn.py website.wsgi

daemon:
	gunicorn -c config/gunicorn.py website.wsgi --daemon

container:
	docker build .

statics:
	python manage.py collectstatic