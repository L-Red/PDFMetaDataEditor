# PDFMetaDataEditor
If you're like me you like to read a lot. I find myself downloading a lot of texts, short stories, articles and essays from the internet in the form of PDFs. And if you're like me, you like to read your texts on an e-reader. 

But if a downloaded text stems from a poorly managed or obscure source, it's meta-data such as author, title, etc. will be incorrectly set or not set at all. 
In my opinion, it makes for a much more enjoyable experience if your files are organized with the correct metadata. This is why I created this app. 
It is not complex nor highly functional, and it would take you no more than 60 minutes to code from scratch if you have some coding experience.
But let me save you 60 minutes!

I made this for my personal use, but if can be used by someone else, please go ahead.
Also, I open for any ideas regarding extra features.

# Usage
## GUI
Open the MacOS application in the `dist` folder.
Another option would be to call
```bash
python src/main.py
```

## Command line
Just call:
```bash
python src/edit_pdf.py <pdf_file> [...metadata flags] <output_file>
```
Example:
```bash
python src/edit_pdf.py input.pdf --title 'New Title' --author 'Author Name' output.pdf
```
