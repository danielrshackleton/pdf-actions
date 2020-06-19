import sys
from pdfFunctions import read_write


def _check_values(page_num, reader):
    """ Checks that page_num is within pdf page range, returns page_num as integer """

    if page_num == 'start':
        page_num = 0
    elif page_num == 'end':
        page_num = reader.numPages - 1

    if page_num < 0 or page_num >= reader.numPages:
        sys.exit("Error: page number specified is not in range")

    return page_num


def add_blank(filename, page_num):
    """ Adds blank page to pdf file at specified page number"""

    input_stream, pdf_reader, pdf_writer = read_write.read_pdf(filename)

    page_num = _check_values(page_num, pdf_reader)

    # Add blank page
    for page in range(pdf_reader.numPages):

        page_obj = pdf_reader.getPage(page)

        # If page == 0, get dimensions of next page and add blank page to start
        if page == page_num and page_num == 0:
            next_page = pdf_reader.getPage(page + 1)
            width = next_page.mediaBox.getWidth()
            height = next_page.mediaBox.getHeight()
            pdf_writer.addBlankPage(width, height)

        # else add blank page with dimensions of previous page (default)
        elif page == page_num:
            pdf_writer.addBlankPage()
        elif page != page_num:
            pdf_writer.addPage(page_obj)

    read_write.write_pdf(filename, pdf_writer, input_stream) 


if __name__ == "__main__":
    in_file = '../samples/test.pdf'
    add_blank(in_file, 'start')
