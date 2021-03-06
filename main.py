#!/usr/bin/python

import argparse

from pdfFunctions import rotate, scan_form, merge, rotate, get_range, encrypt, decrypt


def main():
    # original pdf file name
    origFileName = 'test.pdf'

    # new pdf file name
    newFileName = 'rotatedFile.pdf'

    # calling the rotatePDF function
    # rotatePDF.pdf_rotate(origFileName, newFileName)

    # parser = argparse.ArgumentParser(prog='main', description='PDF file name and password (optional)')
    #
    # parser.add_argument("filename", default='test.pdf', help="Name of pdf file (please include '.pdf'")
    # parser.add_argument("-p", "--password", help="Password field is optional")
    # args = parser.parse_args()
    #
    # file_name = args.filename
    # password = args.password

    file_name = 'samples/form.pdf'

    rotate.pdf_rotate(file_name)
    scan_form.load_form(file_name, password=None)


if __name__ == "__main__":
    main()