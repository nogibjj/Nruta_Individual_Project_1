install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py mylib/*.py *.ipynb

lint:
	ruff check *.py mylib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

test:
	pytest --nbval
	python -m pytest -cov=mylib test_script.py mylib/test_lib.py

generate_and_push:
	python sustainable_fashion.py
	git config --local user.email "action@github.com"
	git config --local user.name "GitHub Action"
	git add .coverage bar_plot.png pie_chart.png sustainable_fashion.md
	git commit -m "Generate stats and plots" || true 
	git push

all: install format lint test
