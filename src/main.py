import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter
from edit_pdf import save_pdf

class PDFMetadataEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Metadata Editor")

        # Initialize variables
        self.pdf_path = ''
        self.metadata = {}

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Open PDF Button
        open_btn = tk.Button(self.root, text="Open PDF", command=self.open_pdf)
        open_btn.grid(row=0, column=0, pady=10, padx=10)

        # Metadata fields
        tk.Label(self.root, text="Title:").grid(row=1, column=0, sticky='e')
        tk.Label(self.root, text="Author:").grid(row=2, column=0, sticky='e')
        tk.Label(self.root, text="Subject:").grid(row=3, column=0, sticky='e')
        tk.Label(self.root, text="Keywords:").grid(row=4, column=0, sticky='e')

        self.title_var = tk.StringVar()
        self.author_var = tk.StringVar()
        self.subject_var = tk.StringVar()
        self.keywords_var = tk.StringVar()

        self.title_entry = tk.Entry(self.root, textvariable=self.title_var, width=50)
        self.author_entry = tk.Entry(self.root, textvariable=self.author_var, width=50)
        self.subject_entry = tk.Entry(self.root, textvariable=self.subject_var, width=50)
        self.keywords_entry = tk.Entry(self.root, textvariable=self.keywords_var, width=50)

        self.title_entry.grid(row=1, column=1, padx=10)
        self.author_entry.grid(row=2, column=1, padx=10)
        self.subject_entry.grid(row=3, column=1, padx=10)
        self.keywords_entry.grid(row=4, column=1, padx=10)

        # Save PDF Button
        try:
          save_btn = tk.Button(self.root, text="Save PDF", command=self.try_save_pdf)
        except ValueError as e:
          messagebox.showwarning("No PDF Selected", "Please open a PDF file first.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save PDF.\n{e}")
        save_btn.grid(row=5, column=0, pady=10, padx=10)

        # Exit Button
        exit_btn = tk.Button(self.root, text="Exit", command=self.root.quit)
        exit_btn.grid(row=5, column=1, pady=10, padx=10, sticky='e')

    def open_pdf(self):
        # Open file dialog to select PDF
        self.pdf_path = filedialog.askopenfilename(
            filetypes=[("PDF Files", "*.pdf")],
            title="Select a PDF file"
        )
        if self.pdf_path:
            try:
                reader = PdfReader(self.pdf_path)
                self.metadata = reader.metadata

                # Update the entry fields with existing metadata
                self.title_var.set(self.metadata.get('/Title', ''))
                self.author_var.set(self.metadata.get('/Author', ''))
                self.subject_var.set(self.metadata.get('/Subject', ''))
                self.keywords_var.set(self.metadata.get('/Keywords', ''))

                messagebox.showinfo("PDF Loaded", "PDF metadata loaded successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to read PDF metadata.\n{e}")

    def try_save_pdf(self):
        save_path = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF Files", "*.pdf")],
                title="Save updated PDF as"
            )
        try:
            save_pdf(self.pdf_path, self.title_var.get(), self.author_var.get(), self.subject_var.get(), self.keywords_var.get(), save_path)
            messagebox.showinfo("Success", "PDF metadata updated and saved successfully.")
        except ValueError as e:
            messagebox.showwarning("No PDF Selected", "Please open a PDF file first.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save PDF.\n{e}")

def main():
    root = tk.Tk()
    app = PDFMetadataEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
