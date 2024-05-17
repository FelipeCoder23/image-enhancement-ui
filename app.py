import streamlit as st
import requests

st.title("Image Enhancement App")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

if uploaded_file is not None:
    files = {"file": uploaded_file.getvalue()}
    response = requests.post("http://<EC2_PUBLIC_IP>:8000/enhance-image/", files=files)
    if response.status_code == 200:
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        st.success('Image successfully enhanced and uploaded!')
    else:
        st.error('Failed to enhance image')
