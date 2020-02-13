import sys

import PyPDF2


def read_pdf(in_file):

    if not in_file.endswith('.pdf'):
        sys.exit('Not a valid pdf file')

    input_stream = open(in_file, 'rb')
    pdf_writer = PyPDF2.PdfFileWriter()
    pdf_reader = PyPDF2.PdfFileReader(in_file)

    return input_stream, pdf_reader, pdf_writer


def write_pdf(out_file, writer, in_stream):
    in_stream.close()

    # Create the output stream and overwrite file
    output_stream = open(out_file, 'wb')
    writer.write(output_stream)
    output_stream.close()
