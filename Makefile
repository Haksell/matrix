# TODO add mypy
# TODO use mypy everywhere instead of asserts
# TODO add pylint
# TODO examples with complex numbers

test:
	pytest -ra -vv --cov

clean:
	rm -rf __pycache__ .pytest_cache .coverage