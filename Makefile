test:
	@pytest -rA -vv

clean:
	rm -rf __pycache__ .pytest_cache .coverage

loc:
	find . -name '*.py' | sort | xargs wc -l
