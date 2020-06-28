install:
	PIPENV_VENV_IN_PROJECT=true pipenv install

run/example:
	pipenv run python xlsx.py -s ',' -i examples/sample_data.csv -o examples/sample_data.xlsx