import sys

import PyPDF2

from pdfFunctions import read_write


def _check_values(page_num, reader):
    """ Checks that page_number is within pdf range """

    if page_num == 'start':
        page_num = 0
    elif page_num == 'end':
        page_num = reader.numPages - 1

    if page_num < 0 or page_num >= reader.numPages:
        sys.exit("Error: page number specified is not in range")

    return page_num


def remove_blank(filename):
    """ Removes any blank pages from the pdf """
    
    input_stream, pdf_reader, pdf_writer = read_write.read_pdf(filename)

    # rotating each page
    for page in range(pdf_reader.numPages):

        page_obj = pdf_reader.getPage(page)

        # Add page to pdf_writer if it is not empty
        if page_obj.getContents():

            # adding rotated page object to pdf writer
            pdf_writer.addPage(page_obj)

    read_write.write_pdf(filename, pdf_writer, input_stream)


if __name__ == "__main__":
    orig = '../samples/origTest.pdf'
    remove_blank(orig)
