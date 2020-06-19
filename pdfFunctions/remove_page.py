from pdfFunctions import read_write

import sys

import PyPDF2


def _check_values(page_num, reader):
    """ Checks that page_number is within pdf range (also accepts 'start'/'end') """

    if page_num == 'start':
        page_num = 0
    elif page_num == 'end':
        page_num = reader.numPages - 1

    if page_num < 0 or page_num >= reader.numPages:
        sys.exit("Error: page number specified is not in range")

    return page_num


def remove_page(filename, page_num):
    """ Remove specified page number from pdf file """

    input_stream, pdf_reader, pdf_writer = read_write.read_pdf(filename)

    page_num = _check_values(page_num, pdf_reader)

    # remove specified page
    for page in range(pdf_reader.numPages):

        page_obj = pdf_reader.getPage(page)

        if page != page_num:
            pdf_writer.addPage(page_obj)

    read_write.write_pdf(filename, pdf_writer, input_stream)


if __name__ == "__main__":
    in_file = '../samples/test.pdf'
    my_page = 0
    remove_page(in_file, my_page)
    print(f'Page {my_page} removed from {in_file}')
