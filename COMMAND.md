



docker-compose up --remove-orphan

docker-compose run app alembic revision --autogenerate -m "New Migration"
docker-compose run app alembic upgrade head


# end

docker system prune
