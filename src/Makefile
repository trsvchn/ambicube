STATES_DIR = states/
TEX_DIR = cubes/
PDF_DIR = images/

STATES = $(wildcard $(STATES_DIR)*.csv)
CUBES = $(addsuffix .tex,$(basename $(subst $(STATES_DIR),$(TEX_DIR),$(STATES))))
PDF = $(addsuffix .pdf,$(basename $(subst $(TEX_DIR),$(PDF_DIR),$(CUBES))))
PNG = $(addsuffix .png,$(basename $(PDF)))

all: f2l.pdf

f2l.pdf: main.tex
	@echo "===> Compiling f2l.pdf <==="
	pdflatex --jobname="f2l" -output-directory . main.tex
	rm -f ./*.aux ./*.log ./*.gz

main.tex: $(PDF)

$(PDF): $(PDF_DIR)%.pdf: $(TEX_DIR)%.tex
	@echo "===> Compiling $@ <==="
	./scripts/tex2pdf $< $@

$(CUBES): $(TEX_DIR)%.tex: $(STATES_DIR)%.csv
	python ./scripts/csv2tex.py -i $< -o $@

png: $(PNG)

$(PNG): $(PDF_DIR)%.png: $(PDF_DIR)%.pdf
	@echo "===> Converting $< <==="
	./scripts/pdf2png $< $@

clean:
	rm -rf $(PDF_DIR)* $(TEX_DIR)*
	rm -f ./f2l.pdf
