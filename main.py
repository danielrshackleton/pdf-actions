from pdfFunctions import rotatePDF


def main():
    # original pdf file name
    origFileName = 'inFile.pdf'

    # new pdf file name
    newFileName = 'rotatedFile.pdf'


    # calling the PDFrotate function
    rotatePDF.pdfRotate(origFileName,newFileName)


if __name__ == "__main__":
    main()