# TODO add __iter__ and other magic methods
# TODO test_repr
# TODO matrix constructor in vector and vice-versa
# TODO test_init_list
# TODO test_init_vector
# TODO test_init_matrix
# TODO add mypy
# TODO add pylint

test:
	pytest -ra -vv --cov

clean:
	rm -rf __pycache__ .pytest_cache