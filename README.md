# PDFMetaDataEditor
This editor allows you to edit metadata of your PDFs. E.g. if you have any downloaded books where you are missing the author or title field you can easily add them with this. 
They will then look better on your e-reader.

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
