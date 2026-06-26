import streamlit as st

st.title("PDF Tool")

opcion = st.selectbox(
    "Seleccione una opcion",
    [
        "Unir PDF",
        "Extraer páginas"
    ]
)

st.write("Operación seleccionada", opcion)


