## automate migration code

alembic revision --autogenerate -m "snapshot"

## automate sqlalchemy's model

sqlacodegen $DATABASE_URL --outfile db/\_models.py

issue: for relationship function, the inpu table argument should be the class name not table name. and some relationships are not detected
