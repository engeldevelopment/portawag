MANAGEPY = python manage.py

run:
	@$(MANAGEPY) runserver

migrate:
	@$(MANAGEPY) makemigrations
	@$(MANAGEPY) migrate

clean:
	@rm -rf htmlcov */**/**/**/__pycache__/
