import os
import pprint

from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage, PDFTextExtractionNotAllowed
from pdfminer.pdfparser import PDFParser
from pdfminer.psparser import PSLiteral
from pdfminer.pdfinterp import PDFObjRef
from pdfminer.pdftypes import resolve1



def load_form(filename, password):
    filename = os.pardir + "/" + filename

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

        fields = resolve1(doc.catalog['AcroForm'])['Fields']
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
    my_file = 'test.pdf'
    my_pass = None
    load_form(my_file, my_pass)


if __name__ == "__main__":
    main()
