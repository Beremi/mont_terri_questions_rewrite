PAPER_DIR := paper
BUILD_DIR := build
MAIN := main.tex
PDF := $(BUILD_DIR)/mont_terri_ogs_model_chapter.pdf

.PHONY: build figures clean

build: figures
	@mkdir -p $(BUILD_DIR)
	@if command -v latexmk >/dev/null 2>&1; then \
		cd $(PAPER_DIR) && latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=../$(BUILD_DIR) $(MAIN); \
	else \
		cd $(PAPER_DIR) && pdflatex -interaction=nonstopmode -halt-on-error -output-directory=../$(BUILD_DIR) $(MAIN); \
		cd $(BUILD_DIR) && BIBINPUTS=../$(PAPER_DIR): bibtex main; \
		cd $(PAPER_DIR) && pdflatex -interaction=nonstopmode -halt-on-error -output-directory=../$(BUILD_DIR) $(MAIN); \
		cd $(PAPER_DIR) && pdflatex -interaction=nonstopmode -halt-on-error -output-directory=../$(BUILD_DIR) $(MAIN); \
	fi
	@cp $(BUILD_DIR)/main.pdf $(PDF)
	@echo "Built $(PDF)"

figures:
	@python $(PAPER_DIR)/scripts/build_ogs_solver_snapshots.py >/dev/null
	@python $(PAPER_DIR)/scripts/build_open_niche_pressure_curve.py >/dev/null

clean:
	@rm -rf $(BUILD_DIR)
