export PIPENV_VERBOSITY=-1

deps:
	pipenv update
	pipenv lock -r > requirements.txt

run:
	gunicorn -c config/gunicorn.py website.wsgi

container:
	docker build .

static:
	python manage.py collectstatic