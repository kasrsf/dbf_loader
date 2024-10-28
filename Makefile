.PHONY: test
test:
	uv run pytest

.PHONY: run
run:
	uv run db_tp_csv.cli:main
