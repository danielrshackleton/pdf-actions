import PyPDF2


def pdf_rotate(origFileName, newFileName):
    # creating a pdf File object of original pdf
    with open(origFileName, 'rb') as pdfFileObj:
        # creating a pdf Reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        # creating a pdf writer object for new pdf
        pdfWriter = PyPDF2.PdfFileWriter()

        # rotating each page
        for page in range(pdfReader.numPages):

            pageObj = pdfReader.getPage(page)
            orientation = pdfReader.getPage(page).get('/Rotate')

            if orientation == 'None' or orientation == 0:
                pageObj.rotateClockwise(0)
            elif orientation == 90:
                pageObj.rotateClockwise(270)
            elif orientation == 180:
                pageObj.rotateClockwise(180)
            elif orientation == 270:
                pageObj.rotateClockwise(90)


            # adding rotated page object to pdf writer
            pdfWriter.addPage(pageObj)

        # new pdf file object
        with open(newFileName, 'wb') as newFile:

            # writing rotated pages to new file
            pdfWriter.write(newFile)

    return newFile
