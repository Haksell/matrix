all:
	-@$(MAKE) clean --no-print-directory
	-@$(MAKE) test --no-print-directory
	-@$(MAKE) clean --no-print-directory

test:
	@pytest -rA -vv

clean:
	rm -rf __pycache__ src/__pycache__ .pytest_cache .coverage

loc:
	find . -name '*.py' | sort | xargs wc -l
