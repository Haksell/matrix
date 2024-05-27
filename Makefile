PROJECTION_FOLDER := matrix_display
PROJECTION_LINK := display_linux.tar.gz
PROJECTION_MAIN := projection_matrix.py

all:
	-@$(MAKE) clean --no-print-directory
	-@$(MAKE) test --no-print-directory
	-@$(MAKE) clean --no-print-directory

test:
	@pytest -rA -vv

clean:
	rm -rf __pycache__ src/__pycache__ .pytest_cache .coverage
	rm -rf $(PROJECTION_FOLDER) $(PROJECTION_LINK)

$(PROJECTION_FOLDER):
	@rm -rf $(PROJECTION_LINK)
	@rm -rf $@
	wget https://cdn.intra.42.fr/document/document/22648/$(PROJECTION_LINK)
	tar xvf $(PROJECTION_LINK)
	rm $(PROJECTION_LINK)

projection: $(PROJECTION_FOLDER)
	@python $(PROJECTION_MAIN) | tee $(PROJECTION_FOLDER)/proj
	@cd $(PROJECTION_FOLDER) && ./display

loc:
	find . -name '*.py' | sort | xargs wc -l

.PHONY: all test clean projection loc