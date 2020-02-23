PKG_NAME := ViGreyResume
CURRENTDIR := $(dir $(realpath $(firstword $(MAKEFILE_LIST))))

all:
	mkdir -p $(CURRENTDIR)bin; \
	mkdir -p $(CURRENTDIR)build/$(PKG_NAME); \
	cp .gitignore $(CURRENTDIR)build/$(PKG_NAME); \
	cp Makefile $(CURRENTDIR)build/$(PKG_NAME); \
	cp README.md $(CURRENTDIR)build/$(PKG_NAME); \
	cp -r $(CURRENTDIR)src $(CURRENTDIR)build/$(PKG_NAME); \
	cd $(CURRENTDIR)build; \
	zip -r part.zip $(PKG_NAME); \
	cp -r $(CURRENTDIR)src/pdf pdf; \
	cd pdf; \
	sed "s/%footnote%/$$(cat footnote.tex)/" $(PKG_NAME)-LaTeX.tex > $(PKG_NAME)-LaTeX-new.tex; \
	pdflatex $(PKG_NAME)-LaTeX-new.tex; \
	gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dNOPAUSE -dQUIET -dBATCH -dPrinted=false -sOutputFile=$(PKG_NAME)-pdf.pdf $(PKG_NAME)-LaTeX-new.pdf; \
	cd $(CURRENTDIR)build; \
	echo "<!--" > part.pdf; \
	cat pdf/$(PKG_NAME)-pdf.pdf >> part.pdf; \
	echo "-->" >> part.pdf; \
	cat $(CURRENTDIR)/src/html/$(PKG_NAME)-html.html >> part.pdf; \
	echo "<!--" >> part.pdf; \
	echo "\"\"\"" >> part.pdf; \
	cat $(CURRENTDIR)/src/python/$(PKG_NAME)-python.py >> part.pdf; \
	echo "r\"\"\"" >> part.pdf; \
	python3 $(CURRENTDIR)src/brainfu/bfcomment.py part.pdf part-commented.pdf; \
	python3 $(CURRENTDIR)src/brainfu/ascii2bf.py $(CURRENTDIR)src/ascii/$(PKG_NAME)-ascii.txt >> part-commented.pdf; \
	python3 $(CURRENTDIR)src/brainfu/bfcomment.py part.zip part-commented.zip; \
	echo "# coding=latin1" > part2.pdf; \
	echo "r\"\"\"" >> part2.pdf; \
	cat part-commented.pdf >> part2.pdf; \
	cat part-commented.zip >> part2.pdf; \
	zip -F part2.pdf --out part3.pdf; \
	python3 $(CURRENTDIR)src/brainfu/bfcomment.py part3.pdf part3-commented.pdf; \
	tail -c +5 part3-commented.pdf | head -c -1 > final.pdf; \
	echo "-->" >> final.pdf; \
	echo "\"\"\"" >> final.pdf; \
	cp final.pdf $(CURRENTDIR)bin/$(PKG_NAME).pdf; \
	cd $(CURRENTDIR); \

boring:
	mkdir -p $(CURRENTDIR)bin; \
	mkdir -p $(CURRENTDIR)build; \
	cd $(CURRENTDIR)build; \
	cp -r $(CURRENTDIR)src/pdf pdf; \
	cd pdf; \
	pdflatex $(PKG_NAME)-LaTeX.tex; \
	gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dNOPAUSE -dQUIET -dBATCH -dPrinted=false -sOutputFile=$(PKG_NAME)-pdf.pdf $(PKG_NAME)-LaTeX.pdf; \
	cp $(PKG_NAME)-pdf.pdf $(CURRENTDIR)bin/$(PKG_NAME)-boring.pdf; \
	cd $(CURRENTDIR); \

clean:
	rm -rf $(CURRENTDIR)bin; \
	rm -rf $(CURRENTDIR)build; \
