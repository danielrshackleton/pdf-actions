import sys

import PyPDF2


def decrypt_pdf(filename, password):

    if ".pdf" not in filename:
        sys.exit("Please enter a valid pdf file")

    input_stream = open(filename, 'rb')
    pdf_writer = PyPDF2.PdfFileWriter()
    pdf_reader = PyPDF2.PdfFileReader(filename)

    if pdf_reader.isEncrypted:
        pdf_reader.decrypt(password)
    else:
        sys.exit(f'The file "{filename}" is already unencrypted.')

    # add FileReader pages to FileWriter
    for page in range(pdf_reader.numPages):

        page_obj = pdf_reader.getPage(page)
        pdf_writer.addPage(page_obj)

    del pdf_reader
    input_stream.close()

    # Overwrite the encrypted pdf
    output_stream = open(filename, 'wb')
    pdf_writer.write(output_stream)
    output_stream.close()

    print(f'The file "{filename}" is now unencrypted.')


if __name__ == '__main__':
    _filename = '../samples/test.pdf'
    _password = 'testPass'
    decrypt_pdf(_filename, _password)
