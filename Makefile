# TODO add mypy
# TODO use mypy everywhere instead of asserts
# TODO add pylint

# TODO implement conjugate transpose?
# TODO examples with complex numbers
# TODO fix complex numbers on dot/norm/angle cos

# TODO bonus
# TODO test individually each function/method even if coverage 100%

test:
	pytest -ra -vv --cov

clean:
	rm -rf __pycache__ .pytest_cache .coverage