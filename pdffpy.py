from pypdf import PdfWriter
import os

merger = PdfWriter()
files=[file for file in os.listdir() if file.endswith(".pdf")]

for pdf in ["Chapter-1.pdf", "Chapter-2.pdf", "Chapter-3.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()