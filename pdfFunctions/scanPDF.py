import sys
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdftypes import resolve1


def load_form(filename, password):
    """Load pdf form contents into a nested list of name/value tuples"""
    with open(filename, 'rb') as file:
        parser = PDFParser(file)

        # for when PDF form has password restrictions
        if password is None:
            doc = PDFDocument(parser)
        else:
            doc = PDFDocument(parser, password)

        fields = resolve1(doc.catalog['AcroForm'])['Fields']
        for i in fields:
            field = resolve1(i)
            name, value = field.get('T'), field.get('V')
            pair = escape_utf16('{0}: {1}'.format(name, value))  # .encode('utf-8')
            print(pair)

def main():
    #myFile = sys.argv[1]
    #myPass = sys.argv[2]

    myFile = 'test.pdf'
    myPass = None

    load_form(myFile, myPass)


if __name__ == "__main__":
    main()
