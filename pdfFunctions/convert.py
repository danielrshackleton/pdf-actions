#!/usr/bin/env python
import sys
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams
from pdfminer.image import ImageWriter


# main
def main(in_file, out_file, out_type):

    # debug option
    debug = 0
    # input option
    password = b''
    pagenos = set()
    maxpages = 0
    # output option
    # outfile = None
    # outtype = None
    imagewriter = None
    rotation = 0
    stripcontrol = False
    layoutmode = 'normal'
    encoding = 'utf-8'
    # pageno = 1
    scale = 1
    caching = True
    # showpageno = True
    laparams = LAParams()

    #
    PDFDocument.debug = debug
    PDFParser.debug = debug
    CMapDB.debug = debug
    PDFPageInterpreter.debug = debug
    #
    rsrcmgr = PDFResourceManager(caching=caching)
    device = PDFDevice(rsrcmgr)

    if not outtype:
        out_type = 'text'
        if outfile:
            if outfile.endswith('.htm') or outfile.endswith('.html'):
                out_type = 'html'
            elif outfile.endswith('.xml'):
                out_type = 'xml'
            elif outfile.endswith('.tag'):
                out_type = 'tag'

    outfp = open(out_file, 'w', encoding=encoding)

    if out_type == 'text':
        device = TextConverter(rsrcmgr, outfp, laparams=laparams,
                               imagewriter=imagewriter)
    elif out_type == 'xml':
        device = XMLConverter(rsrcmgr, outfp, laparams=laparams,
                              imagewriter=imagewriter,
                              stripcontrol=stripcontrol)
    elif out_type == 'html':
        device = HTMLConverter(rsrcmgr, outfp, scale=scale,
                               layoutmode=layoutmode, laparams=laparams,
                               imagewriter=imagewriter, debug=debug)
    elif out_type == 'tag':
        device = TagExtractor(rsrcmgr, outfp)

    with open(in_file, 'rb') as fp:
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.get_pages(fp, pagenos,
                                      maxpages=maxpages, password=password,
                                      caching=caching, check_extractable=True):
            page.rotate = (page.rotate+rotation) % 360
            interpreter.process_page(page)
    device.close()
    outfp.close()
    return


if __name__ == '__main__':
    infile = '../samples/form2.pdf'
    outfile = '../samples/htmlTest.html'
    outtype = 'html'
    main(infile, outfile, outtype)
