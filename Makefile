local/lint:
	flake8 app/

local/black:
	python -m black app/

local/check-packages:
	pipenv check --system -e PIPENV_PYUP_API_KEY=""

local/bandit:
	bandit -r app *.py

local/install:
	pipenv install --dev --skip-lock

local/shell:
	pipenv shell

local/run:
	streamlit run run.py
