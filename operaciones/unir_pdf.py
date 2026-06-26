from pypdf import PdfReader, PdfWriter
from operaciones.operaciones_pdf import OperationPDF

class UnirPDF(OperationPDF):

    def __init__(self, archivos):
        self.archivos = archivos

    def ejecutar(self, salida):
        writer = PdfWriter()
        for archivo in self.archivos:
            reader  = PdfReader(archivo)

            for pagina in reader.pages:
                writer.add_page(pagina)

            with open(salida, 'wb') as f:
                writer.write(f)