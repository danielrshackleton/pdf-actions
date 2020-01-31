import sys
import os
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage, PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdftypes import resolve1


def load_form(filename, password):
    """Load pdf form contents into a nested list of name/value tuples"""

    # get current directory
    filename = os.pardir + "/" + filename

    with open(filename, 'rb') as file:
        parser = PDFParser(file)

        # for when PDF form has password restrictions
        if password is None:
            doc = PDFDocument(parser)
        else:
            doc = PDFDocument(parser, password)

        if not doc.is_extractable:
            raise PDFTextExtractionNotAllowed

        rsrcmgr = PDFResourceManager()
        device = PDFDevice(rsrcmgr)
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

        fields = resolve1(doc.catalog['AcroForm'])['Fields']
        for i in fields:
            field = resolve1(i)
            name, value = field.get('T'), field.get('V')
            pair = '{0}: {1}'.format(name, value)
            print(pair)

def main():
    #myFile = sys.argv[1]
    #myPass = sys.argv[2]

    myFile = 'test.pdf'
    myPass = None

    load_form(myFile, myPass)


if __name__ == "__main__":
    main()
