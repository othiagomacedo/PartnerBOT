from io import BytesIO
import PyPDF2


def getPDF():
    try:
        pdf_bin = PyPDF2.PdfFileReader(open('./templatePDF/CNPJ.pdf', 'rb'))
        numPaginas = int(pdf_bin.getNumPages())
        pdfpage = ""

        for i in range(0, numPaginas):
            pdfPage = pdf_bin.getPage(i).extractText() + '\n'

        cnpjs = []
        aux = [pdfPage.replace(".", "").replace("/", "").replace("-", "").replace(" ", "").split('\n')]
        for text in aux:
            if (text == None or text==''):
                del aux[text]
            else:
                for i in text:
                    if (i == '') or (i == None) or (not i.isdigit()):
                        del i
                    else:
                        cnpjs.append(str(i))

        return cnpjs
    except:
        print("nao foi possivel ler arquivo")


class Read:
    pass
