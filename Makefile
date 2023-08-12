# TODO add __iter__ and other magic methods
# TODO test_repr

test:
	pytest -ra -vv --cov

clean:
	rm -rf __pycache__ .pytest_cache