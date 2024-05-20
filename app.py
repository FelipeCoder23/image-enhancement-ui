import streamlit as st
import requests
from PIL import Image
import io
import base64

st.title("Image Enhancement App")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

if uploaded_file is not None:
    # Mostrar la imagen subida
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

    # Enviar la imagen al backend para mejorarla
    files = {"file": uploaded_file.getvalue()}
    response = requests.post("http://3.93.163.184:8000/enhance-image/", files=files)  # Cambia aquí la URL

    if response.status_code == 200:
        st.success('Image successfully enhanced and returned!')

        # Obtener la imagen mejorada codificada en base64
        encoded_image = response.json().get("image")

        if encoded_image:
            # Decodificar la imagen base64
            enhanced_image = Image.open(io.BytesIO(base64.b64decode(encoded_image)))
            # Mostrar la imagen mejorada
            st.image(enhanced_image, caption='Enhanced Image', use_column_width=True)
        else:
            st.error('Enhanced image not found.')
    else:
        st.error(f'Failed to enhance image: {response.text}')
