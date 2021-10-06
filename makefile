init:
	pip install -r requirements.txt
	cp .env-example .env
lint:
	python -m flake8 .
format:
	black .
	make lint
serve:
	python craft serve
