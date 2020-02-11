import sys
from pdfFunctions import readWrite

import PyPDF2


def decrypt_pdf(filename, password):
    input_stream, pdf_reader, pdf_writer = readWrite.read_pdf(filename)

    if pdf_reader.isEncrypted:
        pdf_reader.decrypt(password)
    else:
        sys.exit(f'The file is already unencrypted.')

    # add FileReader pages to FileWriter
    for page in range(pdf_reader.numPages):

        page_obj = pdf_reader.getPage(page)
        pdf_writer.addPage(page_obj)

    readWrite.write_pdf(filename, pdf_writer, input_stream)


if __name__ == '__main__':
    _filename = '../samples/test.pdf'
    _password = 'testPass'
    decrypt_pdf(_filename, _password)
