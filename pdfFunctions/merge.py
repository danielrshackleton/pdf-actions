from PyPDF2 import PdfFileMerger
from pdfFunctions import rotate


def merge(in_file1, in_file2, out_file):
    """ Takes two pdf files and merges them, outputting to out_file """

    merger = PdfFileMerger()
    merger.append(in_file1)
    merger.append(in_file2)

    merger.write(out_file)

    merger.close()


if __name__ == '__main__':
    samples = '../samples/'
    file1 = samples + 'test.pdf'
    file2 = samples + 'test.pdf'
    out = samples + 'mergeTest.pdf'
    merge(file1, file2, out)
