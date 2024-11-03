to activate service:
docker-compose -f docker-compose.prod.yml up -d --build

to makemigrations/migrate:
docker-compose exec app uv run manage.py makemigrations
docker-compose exec app uv run manage.py migrate

to access database:
docker-compose exec postgres_new psql -U username -d website_db

to run server(with docker-compose already activated):
docker-compose exec app uv run manage.py runserver (but is already activated, if docker-compose is activated)