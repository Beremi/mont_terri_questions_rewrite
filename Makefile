PAPER_DIR := paper
BUILD_DIR := build
MAIN := main.tex
REVIEW_MAIN := main_review.tex
PDF := $(BUILD_DIR)/mont_terri_ogs_model_chapter.pdf
CLEAN_PDF := $(BUILD_DIR)/mont_terri_ogs_model_chapter_clean.pdf
REVIEW_PDF := $(BUILD_DIR)/mont_terri_ogs_model_chapter_review.pdf

.PHONY: build review build-all figures clean

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
	@cp $(BUILD_DIR)/main.pdf $(CLEAN_PDF)
	@echo "Built $(PDF)"

review: figures
	@mkdir -p $(BUILD_DIR)
	@if command -v latexmk >/dev/null 2>&1; then \
		cd $(PAPER_DIR) && latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=../$(BUILD_DIR) $(REVIEW_MAIN); \
	else \
		cd $(PAPER_DIR) && pdflatex -interaction=nonstopmode -halt-on-error -output-directory=../$(BUILD_DIR) $(REVIEW_MAIN); \
		cd $(BUILD_DIR) && BIBINPUTS=../$(PAPER_DIR): bibtex main_review; \
		cd $(PAPER_DIR) && pdflatex -interaction=nonstopmode -halt-on-error -output-directory=../$(BUILD_DIR) $(REVIEW_MAIN); \
		cd $(PAPER_DIR) && pdflatex -interaction=nonstopmode -halt-on-error -output-directory=../$(BUILD_DIR) $(REVIEW_MAIN); \
	fi
	@cp $(BUILD_DIR)/main_review.pdf $(REVIEW_PDF)
	@echo "Built $(REVIEW_PDF)"

build-all: build review

figures:
	@python $(PAPER_DIR)/scripts/build_ogs_solver_snapshots.py >/dev/null
	@python $(PAPER_DIR)/scripts/build_open_niche_pressure_curve.py >/dev/null

clean:
	@rm -rf $(BUILD_DIR)
