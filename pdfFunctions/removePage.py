import sys

import PyPDF2


def remove_page(filename, page_num):
    """ Remove the specified page number from pdf file (accepts 'first' and 'last') """

    input_stream = open(filename, 'rb')
    pdf_writer = PyPDF2.PdfFileWriter()
    pdf_reader = PyPDF2.PdfFileReader(filename)

    if page_num == 'first':
        page_num = 0
    elif page_num == 'last':
        page_num = pdf_reader.numPages - 1

    if page_num < 0 or page_num >= pdf_reader.numPages:
        sys.exit("Error: page number specified is not in range")

    # remove specified page
    for page in range(pdf_reader.numPages):

        page_obj = pdf_reader.getPage(page)

        if page != page_num:
            pdf_writer.addPage(page_obj)

    # delete pdf_reader object + close input stream so it doesn't interfere with pdf_writer
    del pdf_reader
    input_stream.close()

    # Create the output stream and overwrite file
    output_stream = open(filename, 'wb')
    pdf_writer.write(output_stream)
    output_stream.close()


if __name__ == "__main__":
    in_file = '../samples/test.pdf'
    my_page = 3
    remove_page(in_file, my_page)
    print(f'Page {my_page} removed from {in_file}')
