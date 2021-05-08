MANAGEPY = python manage.py

run:
	@$(MANAGEPY) runserver

migrate:
	@$(MANAGEPY) makemigrations
	@$(MANAGEPY) migrate

load:
	@$(MANAGEPY) loaddata portafolio/fixtures/backup.json

dump:
	@$(MANAGEPY) dumpdata home -o portafolio/fixtures/backup.json

pre_deploy: migrate load
	@echo "Se cargaron los datos!"

deploy:
	gunicorn -c config/gunicorn/config.py config.wsgi:application

clean:
	@rm -rf htmlcov */**/**/**/__pycache__/
