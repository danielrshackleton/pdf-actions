from PyPDF2 import PdfFileMerger, PdfFileReader


def merge(file1, file2, out_file):

    merger = PdfFileMerger()
    merger.append(PdfFileReader)

    merger.write(out_file)
