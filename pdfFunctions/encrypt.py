import sys

from PyPDF2 import PdfFileWriter, PdfFileReader


def encrypt_pdf(filename, password):
    """ Takes an unencrypted pdf file and encrypts it with password input"""

    if ".pdf" not in filename:
        sys.exit("Please enter a valid pdf file")

    input_stream = open(filename, 'rb')
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(filename)

    if pdf_reader.isEncrypted:
        sys.exit(f'The file "{filename}" is already encrypted.')

    # add each page into the PdfFileWriter
    for page in range(pdf_reader.numPages):

        page_obj = pdf_reader.getPage(page)
        # orientation = pdf_reader.getPage(page).get('/Rotate')
        # page_obj.rotateClockwise(0)
        pdf_writer.addPage(page_obj)

        pdf_writer.encrypt(password)

        # # overwrite the input pdf file
        # with open('../newTest.pdf', "wb") as out_file:
        #     pdf_writer.write(out_file)

    del pdf_reader  # PdfFileReader won't mess with the stream anymore
    input_stream.close()

    # Write the output to pdf.
    output_stream = open(filename, 'wb')
    pdf_writer.write(output_stream)
    output_stream.close()
    print(f'The file "{filename}" is now encrypted.')


if __name__ == '__main__':
    input_file = "../samples/test.pdf"
    encrypt_pdf(input_file, "testPass")
