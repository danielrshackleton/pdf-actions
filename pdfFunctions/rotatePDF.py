import PyPDF2


def pdfRotate(origFileName, newFileName):
    # creating a pdf File object of original pdf
    pdfFileObj = open(origFileName, 'rb')

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
    newFile = open(newFileName, 'wb')

    # writing rotated pages to new file
    pdfWriter.write(newFile)

    # closing the original pdf file object
    pdfFileObj.close()

    # closing the new pdf file object
    newFile.close()