#Import the modules required for reading and writing pdf
from PyPDF2 import PdfFileWriter, PdfFileReader


pdfwriter = PdfFileWriter() # creating a pdf writer object
pdf = PdfFileReader("source.pdf")# crate an object of the pdf you intend to duplicate and encript

#for each page in the pdf we intend to write from
#we add each page to the pdf writer object created
for page_num in range(pdf.numPages):
    pdfwriter.addPage(pdf.getPage(page_num))

#
passsw = "password"  #set the password to be used to encript the pdf
pdfwriter.encrypt(passsw) # add the password to the pdf writer object containing the pdf to write

# create new pdf name and write content and password to it
with open("new_pdf_name.pdf", 'wb') as f:
    pdfwriter.write(f)
    f.close()