MANAGEPY = python manage.py

run:
	@$(MANAGEPY) runserver

migrate:
	@$(MANAGEPY) makemigrations
	@$(MANAGEPY) migrate

pre_deploy: migrate
	@echo "Pre deploy listo!"

deploy:
	gunicorn -c config/gunicorn/config.py config.wsgi:application

clean:
	@rm -rf htmlcov */**/**/**/__pycache__/
