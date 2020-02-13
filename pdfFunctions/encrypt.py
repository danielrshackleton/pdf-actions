import sys
from pdfFunctions import read_write

import PyPDF2


def encrypt_pdf(filename, password):
    """ Takes an unencrypted pdf file and encrypts it with password input"""

    input_stream, pdf_reader, pdf_writer = read_write.read_pdf(filename)

    if pdf_reader.isEncrypted:
        sys.exit(f'The file "{filename}" is already encrypted.')

    # add each page into the PdfFileWriter
    for page in range(pdf_reader.numPages):

        page_obj = pdf_reader.getPage(page)
        pdf_writer.addPage(page_obj)
        pdf_writer.encrypt(password)

    read_write.write_pdf(filename, pdf_writer, input_stream)
    print(f'The file "{filename}" is now encrypted.')


if __name__ == '__main__':
    input_file = "../samples/test.pdf"
    encrypt_pdf(input_file, "testPass")
