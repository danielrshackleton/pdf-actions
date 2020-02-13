import PyPDF2

from pdfFunctions import read_write


def pdf_rotate(filename):
    """ Automatically rotates a pdf to portrait """

    input_stream, pdf_reader, pdf_writer = read_write.read_pdf(filename)

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

    read_write.write_pdf(filename, pdf_writer, input_stream)


if __name__ == "__main__":
    orig = '../samples/inFile.pdf'
    pdf_rotate(orig)
