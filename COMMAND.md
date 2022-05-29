



docker-compose up --remove-orphan -d && docker exec -it app bash -c "uvicorn formatter:formatter --reload --port 1000"

docker exec -it app bash -c "uvicorn formatter:formatter --reload --port 1000"

docker-compose run app alembic revision --autogenerate -m "New Migration"
docker-compose run app alembic upgrade head


# end

docker system prune

