from PyPDF2 import PdfReader, PdfWriter
import sys

def save_pdf(pdf_path, 
             title_var, author_var, subject_var, keywords_var, save_path=None):
        if not pdf_path:
            raise ValueError("No PDF file selected.")

        # Get updated metadata from entry fields
        new_metadata = {
            '/Title': title_var,
            '/Author': author_var,
            '/Subject': subject_var,
            '/Keywords': keywords_var,
        }

        reader = PdfReader(pdf_path)
        writer = PdfWriter()

        # Copy pages to writer
        for page in reader.pages:
            writer.add_page(page)

        # Add metadata
        writer.add_metadata(new_metadata)

        # Save updated PDF
        if save_path:
            with open(save_path, 'wb') as f:
                writer.write(f)

def main():
    args = sys.argv[1:]  
    if len(args) == 0:
      print("Usage: python edit_pdf.py <pdf_file> [...metadata] <output_file>")
      print("Example: python edit_pdf.py input.pdf --title 'New Title' --author 'Author Name' output.pdf")
      sys.exit(1)
    elif len(args) < 3:
        print("Error: Not enough arguments.")
        sys.exit(1)
    else:
        pdf_path = args[0]
        save_path = args[-1]
        metadata = dict(zip(args[1:-1:2], args[2:-1:2]))
        title = metadata.get('--title', '')
        author = metadata.get('--author', '')
        subject = metadata.get('--subject', '')
        keywords = metadata.get('--keywords', '')

        try:
            save_pdf(pdf_path, title, author, subject, keywords, save_path)
            print("PDF metadata updated and saved successfully.")
        except Exception as e:
            print(f"Failed to save PDF.\n{e}")
        sys.exit(0)

if __name__ == "__main__":
    main()
