# Autotagger

*by Travis Le, Min Kim*

*Last updated January 18th, 2022*

## Overview
#### High level explanation
The auto-tagger is a web application with a backend in Python. Its main task is to read in a .txt file transcribed by the content team in a specific encoding schema and return an XML file that reflects that encoding schema. That XML file can then be used to return a LaTeX file, which can be then converted to PDF, or an HTML file as well.

#### Details
The auto-tagger repository consists of many files that manage the conversion of our diaries to many other formats for distribution purposes. There are a few main files that manage the main conversions:
* **“autotagger.py”**:  manage the conversion to “.xml” files
  * Input: Transcription file (.txt)
  * Output: “.xml” files
* **“tei2latex.xslt”** : manage the conversion to “.tex” (LaTex) files.
  * Input: “.xml” files.
  * Output: .tex (LaTex).
* **“tei2html_lb.xslt”**: manage the conversion to “html” files.
  * Input: “.xml” files.
  * Output: a web page (.html)
* **“xml2txt.py”**: manage the conversion to “.txt” files (different from transcription file).
  * Input: “.xml” files
  * Output: TXT files (.txt)

Note that all the XSLT files are located under `/xslt`.
