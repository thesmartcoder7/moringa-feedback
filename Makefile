
run:
	flask run

init:
	flask db init

migrate:
	flask db migrate -m "migration."

upgrade:
	flask db upgrade

test:
	python -m tests.tests