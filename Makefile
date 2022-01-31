# Dev
dev:
	uvicorn project.asgi:application --reload

dump:
	python manage.py dumpdata > data.json

load:
	python manage.py loaddata data.json

reset_db:
	python manage.py reset_db --noinput