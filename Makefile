CONTAINER_NAME = "app"

admin:
	docker compose exec $(CONTAINER_NAME) python3 manage.py createsuperuser

bash:
	docker compose exec $(CONTAINER_NAME) bash

build:
	docker compose build

down:
	docker compose down

logs:
	docker compose logs -f $(CONTAINER_NAME)

# migrate:
# 	docker compose exec $(CONTAINER_NAME) python3 manage.py migrate

# migrations:
# 	docker compose exec $(CONTAINER_NAME) python3 manage.py makemigrations

restart:
	docker compose restart $(CONTAINER_NAME)

shell:
	docker compose exec $(CONTAINER_NAME) python3 manage.py shell

up:
	docker compose up -d

# db: migrations migrate
