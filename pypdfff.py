from pypdf import PdfReader
reader=PdfReader('Chapter-1.pdf')
print(len(reader.pages))
page=reader.pages[0]
print(page.extract_text())

'''Extracting text from PDF
Rotating PDF pages
Merging PDFs
Splitting PDF
Adding watermark to PDF pages'''