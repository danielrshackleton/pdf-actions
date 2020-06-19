import PyPDF2
from pdfFunctions import read_write


def get_range(in_file, out_file, start_page, end_page):
    """ Remove pages not in range and write new pdf """ 

    input_stream, pdf_reader, pdf_writer = read_write.read_pdf(in_file)

    for i in range(min(start_page, end_page), max(start_page, end_page)):
        page_obj = pdf_reader.getPage(i)
        pdf_writer.addPage(page_obj)

    read_write.write_pdf(out_file, pdf_writer, input_stream)


if __name__ == '__main__':
    samples = '../samples/'
    infile = samples + 'test.pdf'
    outfile = '../splitPDF.pdf'

    get_range(infile, outfile, 2, 4)
