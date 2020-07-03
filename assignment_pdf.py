import PyPDF2
pdf_file = open('/The_Living_World.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
for i in range(0,number_of_pages):
  page = read_pdf.getPage(i)
  page_content = page.extractText()
  with open("/Pdf_Questions.txt","a+") as fp:
    fp.write(page_content)
  print(page_content)
