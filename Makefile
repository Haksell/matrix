# TODO add mypy
# TODO use mypy everywhere instead of asserts
# TODO add pylint

# TODO implement conjugate transpose?
# TODO examples with complex numbers
# TODO fix complex numbers on dot/norm/angle cos

# TODO bonus
# TODO test individually each function/method even if coverage 100%

END := \033[0m
GREEN := \033[1m\033[32m

test:
	@flake8 --exclude=test_*.py
	@echo "$(GREEN)✓ flake8$(END)"
	@pytest
	@echo "$(GREEN)✓ pytest$(END)"

clean:
	rm -rf __pycache__ .pytest_cache .coverage