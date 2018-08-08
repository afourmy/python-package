# TODO before committing

check-manifest --ignore tox.ini,tests*

python setup.py check -m -s

flake8

coverage run --source=./sample -m pytest tests

(optional: check coverage) coverage report -m