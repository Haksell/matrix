ARCHIVE := display_linux.tar.gz

clean:
	cargo clean
	rm -rf $(ARCHIVE) matrix_display/

get_display:
	wget https://cdn.intra.42.fr/document/document/29525/$(ARCHIVE) -O $(ARCHIVE)
	tar xvf $(ARCHIVE)
	rm $(ARCHIVE)
