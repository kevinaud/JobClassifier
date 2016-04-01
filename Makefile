init:
	pip install -r docs/requirements.txt

test:
	py.test tests

run:
	python classifier/classifier.py
