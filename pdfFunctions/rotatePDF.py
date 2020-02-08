import PyPDF2


def pdf_rotate(origFileName, newFileName):
    # creating a pdf File object of original pdf
    with open(origFileName, 'rb') as pdfFileObj:
        # creating a pdf Reader object
        pdf_reader = PyPDF2.PdfFileReader(pdfFileObj)

        # creating a pdf writer object for new pdf
        pdf_writer = PyPDF2.PdfFileWriter()

        # rotating each page
        for page in range(pdf_reader.numPages):

            page_obj = pdf_reader.getPage(page)
            orientation = pdf_reader.getPage(page).get('/Rotate')

            if orientation == 'None' or orientation == 0:
                page_obj.rotateClockwise(0)
            elif orientation == 90:
                page_obj.rotateClockwise(270)
            elif orientation == 180:
                page_obj.rotateClockwise(180)
            elif orientation == 270:
                page_obj.rotateClockwise(90)

            # adding rotated page object to pdf writer
            pdf_writer.addPage(page_obj)

        # new pdf file object
        with open(newFileName, 'wb') as newFile:

            # writing rotated pages to new file
            pdf_writer.write(newFile)

    return newFile


if __name__ == "__main__":
    orig = '../origTest.pdf'
    new = '../newnew.pdf'
    pdf_rotate(orig, new)