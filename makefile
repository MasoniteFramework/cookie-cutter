init:
	pip install -r requirements.txt
lint:
	python -m flake8 app/ --ignore=E501,F401,E203,E128,E402,E731,F821,E712,W503,F811
	python -m flake8 config/ --ignore=E501,F401,E203,E128,E402,E731,F821,E712,W503,F811
	python -m flake8 routes/ --ignore=E501,F401,E203,E128,E402,E731,F821,E712,W503,F811
	python -m flake8 tests/ --ignore=E501,F401,E203,E128,E402,E731,F821,E712,W503,F811
format:
	black app
	black config
	black routes
	black tests/
	make lint
