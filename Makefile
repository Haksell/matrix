# TODO implement conjugate transpose?
# TODO examples with complex numbers
# TODO fix complex numbers on dot/norm/angle cos

# TODO bonus
# TODO test individually each function/method even if coverage 100%

END := \033[0m
GREEN := \033[1m\033[32m

all:
	@$(MAKE) --no-print-directory clean > /dev/null
	@$(MAKE) --no-print-directory test
	@$(MAKE) --no-print-directory clean > /dev/null

test:
	pytest -rA -vv

clean:
	rm -rf __pycache__ .pytest_cache .coverage