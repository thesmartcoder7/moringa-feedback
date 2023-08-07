
run:
	flask run

init:
	flask db init

migrate:
	flask db migrate -m "migration"

upgrade:
	flask db upgrade

migrations:
	flask db upgrade && flask db migrate -m "migration"

test:
	python -m tests.tests

active:
	pipenv shell