PYTHON ?= python3
LATEXMK ?= latexmk
LEAN ?= lean

.PHONY: all pdf check formal standalone clean dist
all: check pdf

pdf:
	cd paper && $(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error -file-line-error -jobname=gersten-counterexamples main.tex

check:
	$(PYTHON) scripts/verify_sources.py
	$(PYTHON) scripts/verify_publication.py

formal:
	$(PYTHON) scripts/verify_formal.py --lean "$(LEAN)"

standalone:
	$(PYTHON) scripts/flatten_tex.py

clean:
	$(PYTHON) scripts/clean.py

dist: check pdf formal
	$(PYTHON) scripts/make_dist.py
