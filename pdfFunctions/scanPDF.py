import os
import sys
import pprint

from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.psparser import PSLiteral
from pdfminer.pdfinterp import PDFObjRef
from pdfminer.pdftypes import resolve1


def _pdf_type(doc):
    """ Determines the type of PDF form, exits if invalid """

    if doc.catalog.get('AcroForm') is not None:
        return resolve1(doc.catalog['AcroForm'])['Fields']
    elif doc.catalog.get('XFA') is not None:
        return resolve1(doc.catalog['XFA'])['Fields']
    else:
        sys.exit('Invalid PDF type. Please use a valid electronic PDF form')


def load_form(filename, password):
    """ Loads pdf and extracts form data """

    if '.pdf' not in filename:
        sys.exit("Invalid file. Please use a .pdf file")

    with open(filename, 'rb') as file:
        parser = PDFParser(file)
        if password is None:
            doc = PDFDocument(parser)
        else:
            doc = PDFDocument(parser, password)

        rsrcmgr = PDFResourceManager()
        device = PDFDevice(rsrcmgr)
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

        fields = _pdf_type(doc)
        pdf_table = {}
        for i in fields:
            field = resolve1(i)
            _table_row = _decode_fields(field)
            pdf_table.update(_table_row)

        pprint.pprint(pdf_table)




def _decode_fields(field_index):
    field = resolve1(field_index)
    name, value = _decode_decision(field.get('T', b''), '8'), _decode_decision(field.get('V', b''), '16')
    decoded_field = {name: value}
    return decoded_field


def _decode_decision(value, decode):
    if isinstance(value, bytes):
        return value.decode(f'utf-{decode}')
    elif isinstance(value,  PSLiteral):
        value = value.name
        return value
    elif isinstance(value, PDFObjRef):
        value = resolve1(value)
        return value
    else:
        return value



def main():
    my_file = '../test.pdf'

    my_pass = None
    load_form(my_file, my_pass)


if __name__ == "__main__":
    main()
