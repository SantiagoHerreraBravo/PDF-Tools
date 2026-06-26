from pypdf import PdfReader, PdfWriter
from operaciones.operaciones_pdf import OperationPDF

class ExtraerPaginasPDF(OperationPDF):
    def __init__(self, archivo: str, pagina_inicial: int, pagina_final: int):
        self.archivo = archivo
        self.pagina_inicial = pagina_inicial
        self.pagina_final = pagina_final

    def ejecutar(self, salida):
        reader = PdfReader(self.archivo)
        writer = PdfWriter()

        total_paginas = len(reader.pages)

        if self.pagina_inicial < 1:
            raise ValueError("La página inicial debe ser mayor o igual a 1.")

        if self.pagina_final > total_paginas:
            raise ValueError(
                f"El documento solo tiene {total_paginas} páginas."
            )

        if self.pagina_inicial > self.pagina_final:
            raise ValueError(
                "La página inicial no puede ser mayor que la final."
            )

        for i in range(self.pagina_inicial - 1, self.pagina_final):
            writer.add_page(reader.pages[i])

        with open(salida, "wb") as f:
            writer.write(f)
