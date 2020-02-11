import PyPDF2


def get_range(in_file, out_file, start_page, end_page):
    """ Remove pages not in range """

    input_stream = open(in_file, 'rb')
    pdf_writer = PyPDF2.PdfFileWriter()
    pdf_reader = PyPDF2.PdfFileReader(in_file)

    for i in range(min(start_page, end_page), max(start_page, end_page)):
        page_obj = pdf_reader.getPage(i)
        pdf_writer.addPage(page_obj)

    del pdf_reader  # PdfFileReader won't mess with the stream anymore
    input_stream.close()

    # Write the output to pdf.
    output_stream = open(out_file, 'wb')
    pdf_writer.write(output_stream)
    output_stream.close()


if __name__ == '__main__':
    samples = '../samples/'
    infile = samples + 'test.pdf'
    outfile = '../splitPDF.pdf'

    get_range(infile, outfile, 2, 4)
