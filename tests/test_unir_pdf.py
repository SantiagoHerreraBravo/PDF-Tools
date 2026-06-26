from operaciones.unir_pdf import UnirPDF

def test_unir_pdf():
    operacion = UnirPDF([
        "pruebas/documento1.pdf",
        "pruebas/documento2.pdf"
    ])

    operacion.ejecutar("salida.pdf")

    # Aquí luego verificaremos que el archivo exista