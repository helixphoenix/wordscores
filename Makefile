setup:
	python3 setup.py build
	python3 setup.py install

clean:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	rm -fr .pytest_cache/
	rm -fr venv/ 
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +


lint:
	flake8 --max-line-length 128 wording tests 

lint-fix:
	black --line-length 120 wording tests        


test:
	PYTHONPATH=. pytest
	pytest tests