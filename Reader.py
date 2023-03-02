import PyPDF2
from PyPDF2 import PdfReader
import re

number3_pattern = re.compile("^3\. Gifts, benefits and hospitality from UK sources$")
# Open the PDF file
pdf_file = open('Information.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PdfReader(pdf_file)

# page = pdf_reader.pages[0]

# text = page.extract_text()

# lines = text.split('\n')

# for line in lines:
#    print(line)

# # Close the PDF file
# pdf_file.close()

full = ""
for pages in range(len(pdf_reader.pages)):
    
    page = pdf_reader.pages[pages]
    text = page.extract_text()

    lines = text.split('\n')

    for line in lines:
       #print(line)
       full += line
# Print the extracted text