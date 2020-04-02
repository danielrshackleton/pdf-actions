import PyPDF2
from PIL import Image
import base64

from pdfFunctions import read_write


def extract_images(filename):

    input_stream, pdf_reader, pdf_writer = read_write.read_pdf(filename)
    img_array = []

    for page in range(pdf_reader.numPages-12):
        page_obj = pdf_reader.getPage(page)
        xObject = page_obj['/Resources']['/XObject'].getObject()

        for obj in xObject:
            if xObject[obj]['/Subtype'] == '/Image':
                size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                data = xObject[obj].getData()
                if xObject[obj]['/ColorSpace'] in ('/DeviceRGB', '/DeviceCMYK'):
                    mode = "RGBA"
                    print('rgb')
                else:
                    mode = "P"
                    print(xObject[obj]['/ColorSpace'])

                img_type = ''
                if xObject[obj]['/Filter'] == '/FlateDecode':
                    img_type = 'png'
                elif xObject[obj]['/Filter'] == '/DCTDecode':
                    img_type = 'jpg'
                elif xObject[obj]['/Filter'] == '/JPXDecode':
                    img_type = 'jp2'

                img = str(base64.b64encode(data))
                img_string = 'data:image/%s;base64,%s' % (img_type, img)
                img_array.append(img_string)
                file1 = open("myfile.txt", "w")
                file1.write(img_string)
                file1.close()


if __name__ == '__main__':
    input_file = "../samples/mergeTest.pdf"
    extract_images(input_file)