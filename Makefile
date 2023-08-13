# TODO add mypy
# TODO use mypy everywhere instead of asserts
# TODO add pylint
# TODO examples with complex numbers
# TODO learn conjugate transpose, sesquilinear algebra, and Pre-Hilbert space
# TODO implement conjugate transpose?
# TODO learn triangle inequality, holder norms, minkowski inequality, frobenius norm
# TODO learn pseudonorms, lorentz transform, split-complex numbers, hyperbolic geometry

test:
	pytest -ra -vv --cov

clean:
	rm -rf __pycache__ .pytest_cache .coverage