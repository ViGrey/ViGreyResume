# ViGreyResume

My personal resume.  This resume is simultaneously a PDF, HTML, Python (2 & 3 compatible), Brainfu--, and ZIP file.

**_ViGreyResume was created by Vi Grey (https://vigrey.com) <vi@vigrey.com> and is licensed under the BSD 2-Clause License._**

### Description:

This is my personal resume.  It is simultaneously a valid PDF, HTML, Python (2 & 3 compatible), Brainfu--, and ZIP file.  Unzipping ViGreyResume.pdf will result in the source code of ViGreyResume.pdf, which can be used to build ViGreyResume.pdf, which will be a PDF/HTML/Python/Brainfu--, ZIP polyglot file.

### Platforms:
- Linux

### Build Dependencies:
- texlive
- pdflatex
- ghostscript
- python3
- zip

### Build ViGreyResume.pdf:

From a terminal, go to the the main directory of this project (the directory this README.md file exists in), you can then build the file with the following command.

    $ make

The resulting file will be located in at **bin/ViGreyResume.pdf**.

### Cleaning Build Environment:

If you used `make` to build the polyglot, you can run the following command to clean up the build environment.

    $ make clean

### Viewing ViGreyResume.pdf as a PDF File:

ViGreyResume.pdf is a valid PDF file and should be viewable in your PDF file viewer, including Firefox and Chrome, as long as the extension of ViGreyResume.pdf is **.pdf**.

### Viewing ViGreyResume.pdf as an HTML File in a Web Browser:

ViGreyResume.pdf is a valid static HTML file.  To see the HTML version of the file, change the file extension to **.html**.  You should now be able to open it up in your web browser.

### Running ViGreyResume.pdf as a Python 2 File:

ViGreyResume.pdf is a valid Python 2 file.  If you run this file using python2 without any options, it will print out an ASCII version of the resume text.

    $ Usage: python2 ViGreyResume.pdf [ OPTIONS ] 

    Prints an ASCII version of the resume if no options are provided

    Options:
      -b, --bf BF_FILE_PATH   Interpret BF_FILE_PATH as a Brainfu-- Program
      -h, --help              Print Help (this message) and exit

    Examples:
      python3 ViGreyResume.pdf
      python3 ViGreyResume.pdf --bf ViGreyResume.pdf
      python3 ViGreyResume.pdf -b ViGreyResume.pdf
      python3 ViGreyResume.pdf --help
      python3 ViGreyResume.pdf -h

### Running ViGreyResume.pdf as a Python 3 File:

ViGreyResume.pdf is a valid Python 3 file.  If you run this file using python3 without any options, it will print out an ASCII version of the resume text.

    $ Usage: python3 ViGreyResume.pdf [ OPTIONS ] 

    Prints an ASCII version of the resume if no options are provided

    Options:
      -b, --bf BF_FILE_PATH   Interpret BF_FILE_PATH as a Brainfu-- Program
      -h, --help              Print Help (this message) and exit

    Examples:
      python3 ViGreyResume.pdf
      python3 ViGreyResume.pdf --bf ViGreyResume.pdf
      python3 ViGreyResume.pdf -b ViGreyResume.pdf
      python3 ViGreyResume.pdf --help
      python3 ViGreyResume.pdf -h

### Interpreting ViGreyResume.pdf as a Brainfu-- File:

ViGreyResume.pdf is valid Brainfu-- program, but is also a functioning Brainfu-- program interpreter.  Interpreting ViGreyResume.pdf as a brainfu-- program will print out an ASCII version of the resume text.

    $ python3 ViGreyResume.pdf --bf ViGreyResume.pdf

### Unzipping ViGreyResume.pdf:

ViGreyResume.pdf is a valid ZIP file.  Unzipping ViGreyResume.pdf will produce the source code to create ViGreyResume.pdf

Your zip file extractor should be able to extract ViGreyResume.pdf, although you may have to change the file extension to **.zip** to make your zip file extractor work.

### Special Thanks

- Ange Albertini
- Evan Sultanik
- Evan Teran

A special thanks to these three individuals for inspiring me to see what I can do with file formats and polyglot files.

### License:
    Copyright (C) 2020, Vi Grey
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions
    are met:

        1. Redistributions of source code must retain the above copyright
           notice, this list of conditions and the following disclaimer.
        2. Redistributions in binary form must reproduce the above copyright
           notice, this list of conditions and the following disclaimer in the
           documentation and/or other materials provided with the distribution.

    THIS SOFTWARE IS PROVIDED BY AUTHOR AND CONTRIBUTORS \`\`AS IS'' AND
    ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
    ARE DISCLAIMED. IN NO EVENT SHALL AUTHOR OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
    OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
    HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
    LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
    OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
    SUCH DAMAGE.
