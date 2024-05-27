PROJECTION_FOLDER := matrix_display
PROJECTION_TARBALL := display_linux.tar.gz
PROJECTION_LINK := https://cdn.intra.42.fr/document/document/22648/$(PROJECTION_TARBALL)
PROJECTION_MAIN := projection_matrix.py

all:
	-@$(MAKE) clean --no-print-directory
	-@$(MAKE) test --no-print-directory
	-@$(MAKE) clean --no-print-directory

test:
	@pytest -rA -vv

clean:
	rm -rf __pycache__ */__pycache__
	rm -rf .pytest_cache */.pytest_cache
	rm -rf $(PROJECTION_FOLDER) $(PROJECTION_TARBALL)

$(PROJECTION_FOLDER):
	@rm -rf $(PROJECTION_TARBALL)
	@rm -rf $@
	wget $(PROJECTION_LINK)
	tar xvf $(PROJECTION_TARBALL)
	rm $(PROJECTION_TARBALL)

projection: $(PROJECTION_FOLDER)
	@python $(PROJECTION_MAIN) | tee $(PROJECTION_FOLDER)/proj
	@cd $(PROJECTION_FOLDER) && ./display

loc:
	find . -name '*.py' | sort | xargs wc -l

.PHONY: all test clean projection loc