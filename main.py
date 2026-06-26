from operaciones.unir_pdf import UnirPDF
from operaciones.extraer_paginas_pdf import ExtraerPaginasPDF

def main():
#    archivos = [
#        "utilidades/Archivo 1.pdf",
#        "utilidades/Archivo 2.pdf"
#    ]

#    operacion = UnirPDF(archivos)
#    operacion.ejecutar("resultado.pdf")

    operacion = ExtraerPaginasPDF(
    archivo="utilidades/Archivo 3.pdf",
    pagina_inicial=1,
    pagina_final=1
    )

    operacion.ejecutar("Extraction.pdf")
    print("PDF unido correctamente.")

if __name__ == "__main__":
    main()