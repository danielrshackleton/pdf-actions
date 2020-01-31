import os

from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage, PDFTextExtractionNotAllowed
from pdfminer.pdfparser import PDFParser
from pdfminer.pdftypes import resolve1


def load_form(filename, password):
    filename = os.pardir + "/" + filename

    with open(filename, 'rb') as file:
        parser = PDFParser(file)
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
            _decode_fields(i)


def _decode_fields(field_index):
    field = resolve1(field_index)
    name, value = _decode_decision(field.get('T', b''), '8'), _decode_decision(field.get('V', b''), '16')
    print(f"{name}: {value}")


def _decode_decision(value, decode):
    if isinstance(value, bytes):
        return value.decode(f'utf-{decode}')
    else:
        return ''


def main():
    my_file = 'test.pdf'
    my_pass = None
    load_form(my_file, my_pass)


if __name__ == "__main__":
    main()
