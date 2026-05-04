PAPER_DIR := paper/sections
PAPER_TEX := heavy_tail_backup_recast_xelatex.tex
PAPER_BASE := heavy_tail_backup_recast_xelatex
PAPER_PDF := $(PAPER_DIR)/build/$(PAPER_BASE).pdf
PAPER_LOG := $(PAPER_DIR)/build/$(PAPER_BASE).log
PAPER_SOURCES := $(PAPER_DIR)/$(PAPER_TEX) $(PAPER_DIR)/.latexmkrc $(wildcard $(PAPER_DIR)/tex/*.tex)

.PHONY: all paper pdf paper-check numerical-check clean help

all: paper

paper pdf: $(PAPER_PDF)

$(PAPER_PDF): $(PAPER_SOURCES)
	cd $(PAPER_DIR) && latexmk -xelatex $(PAPER_TEX)

paper-check: paper
	@if rg -n "LaTeX Warning|Overfull|Underfull|undefined|Undefined|Error|Missing" "$(PAPER_LOG)"; then \
		echo "LaTeX log contains warnings/errors: $(PAPER_LOG)"; \
		exit 1; \
	elif ! pdffonts "$(PAPER_PDF)" | rg -q "Hira|Hiragino|HaranoAji|Noto|IPA"; then \
		echo "No embedded Japanese font found in $(PAPER_PDF)"; \
		exit 1; \
	else \
		echo "LaTeX log clean: $(PAPER_LOG)"; \
		echo "Japanese font embedded in $(PAPER_PDF)"; \
	fi

numerical-check:
	python3 analysis/paper_review_checks/run.py

clean:
	cd $(PAPER_DIR) && latexmk -C $(PAPER_TEX)

help:
	@echo "Targets:"
	@echo "  make              Build $(PAPER_PDF)"
	@echo "  make paper        Build $(PAPER_PDF)"
	@echo "  make paper-check  Build paper and fail on serious LaTeX issues or missing Japanese fonts"
	@echo "  make numerical-check  Regenerate numerical check outputs"
	@echo "  make clean        Remove LaTeX build artifacts"
