



docker-compose up --remove-orphan

docker-compose run app alembic revision --autogenerate -m "New Migration"