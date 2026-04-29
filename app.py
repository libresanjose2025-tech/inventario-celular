import streamlit as st
import pandas as pd

st.set_page_config(page_title="Inventario Municipal", layout="wide")

st.title("📋 Registro de Documentación")

# Matriz de datos
if 'datos' not in st.session_state:
    st.session_state.datos = pd.DataFrame(columns=[
        "Nº", "Descripción", "Tipo", "Cant.", "Codificación", "Resp.", "Estado", "Obs.", "Justificación", "Aclaraciones"
    ])

with st.form("form_inventario", clear_on_submit=True):
    st.subheader("📝 Rellenar campos desde el celular")
    col1, col2 = st.columns(2)
    with col1:
        nro = st.number_input("Nº (1-77)", 1, 77)
        desc = st.text_input("Descripción")
        tipo = st.text_input("Tipo de Documento")
        cant = st.text_input("Cantidad")
        cod = st.text_input("Codificación")
    with col2:
        resp = st.text_input("Responsable")
        est = st.selectbox("Estado", ["Tiene", "No tiene"])
        obs = st.text_area("Observaciones")
        just = st.text_area("Justificación (si no tiene)")
        acla = st.text_area("Aclaraciones")
        foto = st.file_uploader("📷 Tomar Foto / Subir", type=["jpg", "png"])
    
    guardar = st.form_submit_button("💾 GUARDAR EN MATRIZ")

if guardar:
    nueva = {"Nº": nro, "Descripción": desc, "Tipo": tipo, "Cant.": cant, "Codificación": cod, "Resp.": resp, "Estado": est, "Obs.": obs, "Justificación": just, "Aclaraciones": acla}
    st.session_state.datos = pd.concat([st.session_state.datos, pd.DataFrame([nueva])], ignore_index=True)
    st.success("✅ ¡Datos guardados con éxito!")

st.write("### 📊 Matriz de Datos Actualizada")
st.dataframe(st.session_state.datos, use_container_width=True)
