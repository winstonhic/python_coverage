PYTHONPATH=. coverage run -p --source . -m pytest -s -v test.py && coverage combine && coverage report -m


