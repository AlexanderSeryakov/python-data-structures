test:
	coverage run -m pytest . && coverage report
test-detail:
	coverage run -m pytest -s -v . && coverage report
run-lint:
	mypy . && isort . && black . && flake8
