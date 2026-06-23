ARCHIVE := display_linux.tar.gz

validate:
	@cargo fmt --all
	@RUSTFLAGS="--deny warnings" cargo check --all-targets
	@RUSTFLAGS="--deny warnings" cargo clippy --all-targets
	@RUSTFLAGS="--deny warnings" cargo test --all-targets --release

clean:
	cargo clean
	rm -rf $(ARCHIVE) matrix_display/

get_display:
	wget https://cdn.intra.42.fr/document/document/29525/$(ARCHIVE) -O $(ARCHIVE)
	tar xvf $(ARCHIVE)
	rm $(ARCHIVE)
