import streamlit as st
import requests
from PIL import Image
import io
import os

st.title("Image Enhancement App")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

if uploaded_file is not None:
    # Mostrar la imagen subida
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

    # Enviar la imagen al backend para mejorarla
    files = {"file": uploaded_file.getvalue()}
    response = requests.post("http://localhost:8000/enhance-image/", files=files)

    if response.status_code == 200:
        st.success('Image successfully enhanced and saved locally!')

        # Obtener la imagen mejorada
        enhanced_image_path = response.json().get("filename")

        # Asegurarse de que la ruta es correcta
        if enhanced_image_path and os.path.exists(enhanced_image_path):
            enhanced_image = Image.open(enhanced_image_path)
            # Mostrar la imagen mejorada
            st.image(enhanced_image, caption='Enhanced Image', use_column_width=True)
        else:
            st.error('Enhanced image not found.')
    else:
        st.error(f'Failed to enhance image: {response.text}')
