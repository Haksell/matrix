# TODO add mypy
# TODO use mypy everywhere instead of asserts
# TODO add pylint

# TODO implement conjugate transpose?
# TODO examples with complex numbers
# TODO fix complex numbers on dot/norm/angle cos

test:
	pytest -ra -v --cov

clean:
	rm -rf __pycache__ .pytest_cache .coverage