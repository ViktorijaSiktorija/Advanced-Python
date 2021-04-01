# pip3 install PyPDF2
import sys
import PyPDF2
from tika import parser

# rb je read binary, file object konvertuje u binary mode
# da bi fileReader mogao da ga procita
with open('AAAAI_2021_Abstracts_001-312.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)  # pokaze broj strana
    print(reader.getPage(0))  # dobijemo page objekat prve strane od PyPDF2

    # rotacija
page = reader.getPage(0)
content = page.extractText()
print(content)
# print(page.rotateCounterClockwise(90)) #/Rotate': -90
# ovo za sada nije sacuvano na kompjuteru

# wb je write binary
# writer objekat uz biblioteku
writer = PyPDF2.PdfFileWriter()
writer.addPage(page)
novoTekst = 'AAAAI_2021_Abstracts_001-312.pdf'
with open('novoTekst.pdf', 'wb') as new_file:
    writer.write(new_file)

# za spajanje
#inputs = sys.argv[1:]
# def pdf_combiner(pdf_list):
#merger = PyPDF2.PdfFileMerger()
# for pdf in pdf_list:
# print(pdf)
# merger.append(pdf)
# merger.write('super.pdf')
# pdf_combiner(inputs)

# za watermark
# PyPDF2

#template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
#watermark = PyPDF2.PdfFileReader(open('watermark.pdf','rb'))
#output = PyPDF2.PdfFileWriter()

# for i in range(template.getNumPages()):
#page = template.getPage(i)
# mergePage spaja
# page.mergePage(watermark.getPage(0))
# output.addPage(page)

# with open('watermarked_output.pdf', 'wb') as file:
# output.write(file)
