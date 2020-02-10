import PyPDF2


def remove_blank(filename):

    input_stream = open(filename, 'rb')
    pdf_writer = PyPDF2.PdfFileWriter()
    pdf_reader = PyPDF2.PdfFileReader(filename)

    # rotating each page
    for page in range(pdf_reader.numPages):

        page_obj = pdf_reader.getPage(page)

        # Add page to pdf_writer if it is not empty
        if page_obj.getContents():

            # adding rotated page object to pdf writer
            pdf_writer.addPage(page_obj)

    del pdf_reader
    input_stream.close()

    output_stream = open(filename, 'wb')
    pdf_writer.write(output_stream)
    output_stream.close()


if __name__ == "__main__":
    orig = '../samples/origTest.pdf'
    remove_blank(orig)
