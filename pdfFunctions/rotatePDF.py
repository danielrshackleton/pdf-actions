import PyPDF2


def pdf_rotate(filename):
    """ Automatically rotates a pdf to portrait """

    input_stream = open(filename, 'rb')
    pdf_writer = PyPDF2.PdfFileWriter()
    pdf_reader = PyPDF2.PdfFileReader(filename)

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

    del pdf_reader
    input_stream.close()

    output_stream = open(filename, 'wb')
    pdf_writer.write(output_stream)
    output_stream.close()


if __name__ == "__main__":
    orig = '../samples/inFile.pdf'
    pdf_rotate(orig)