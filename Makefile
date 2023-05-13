PROJECTNAME := "devblaze"

define HELP

Manage $(PROJECTNAME). Usage:

make lint           	Run linter
make format         	Run formatter
make test           	Run tests
make all            	Show help

endef

export HELP

help:
	@echo "$$HELP"

lint:
	 @bash ./scripts/lint.sh

format:
	@bash ./scripts/format.sh

test:
	@bash ./scripts/test.sh

all: help

.PHONY: help lint format test all
