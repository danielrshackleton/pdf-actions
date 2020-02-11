import sys

import PyPDF2


def add_blank(filename, page_num):
    """ Add a blank page to pdf file (also accepts 'start' and 'end') """

    input_stream = open(filename, 'rb')
    pdf_writer = PyPDF2.PdfFileWriter()
    pdf_reader = PyPDF2.PdfFileReader(filename)

    if page_num == 'start':
        page_num = 0
    elif page_num == 'end':
        page_num = pdf_reader.numPages - 1

    if page_num < 0 or page_num >= pdf_reader.numPages:
        sys.exit("Error: page number specified is not in range")

    # Add blank page
    for page in range(pdf_reader.numPages):

        page_obj = pdf_reader.getPage(page)

        # If page == 0, get dimensions of next page and add blank page to start
        if page == page_num and page_num == 0:
            next_page = pdf_reader.getPage(page+1)
            width = next_page.mediaBox.getWidth()
            height = next_page.mediaBox.getHeight()
            pdf_writer.addBlankPage(width, height)

        # else add blank page with dimensions of previous page (default)
        elif page == page_num:
            pdf_writer.addBlankPage()
        elif page != page_num:
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
    add_blank(in_file, 'first')
