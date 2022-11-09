GEMFURY_AUTH_TOKEN := ${GEMFURY_AUTH_TOKEN}

# distribution details
VERSION := $(shell awk '$$1 == "__version__" {print $$NF}' ./edge_sdk/_version.py)
OS := none
CPU_ARCH = any

help:
	@echo "External node lib Makefile Help:\n"\
	"clean:  Remove all cache and wheel packages.\n"\
	"build:  Build edge-sdk wheel package via setup.py.\n"\
	"version:  Show current edge-sdk version.\n"\
	"publish:  Upload the package in dist directory that matches current edge-sdk version.\n"\
	" VERSION Specify another version to upload (If there is one avaliable). "
test:
	behave tests/features && pytest
clean-dist:
	rm -r ./dist 2>/dev/null || true

clean-cache:
	rm -r *.egg-info || true
	python3 setup.py clean --all || true

clean: clean-dist clean-cache

build: clean
	python setup.py bdist_wheel

obfuscate:
	./code_obfuscation.py

version:
	@echo $(VERSION)

publish: override VERSION := $(if $(VERSION),$(VERSION),)
publish: WHEEL_FILENAME := edge_sdk-$(VERSION)-py3-$(OS)-$(CPU_ARCH).whl
publish:
	curl -F package=@dist/$(WHEEL_FILENAME) https://$(GEMFURY_AUTH_TOKEN)@push.fury.io/quartic-ai/
