#importing necessary libraries
import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO

st.header("Background Remover App")

image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

def main():
    if image is not None:
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        image_bytes = image.read()
        image_io = BytesIO(image_bytes)
        uploaded_image = Image.open(image_io)
        with st.spinner('Removing background...'):
            output_bytes = remove(image_bytes)
        output_io = BytesIO(output_bytes)
        processed_image = Image.open(output_io)
        st.image(processed_image, caption='Processed Image.', use_column_width=True)
        st.download_button(label='Download', data=output_bytes, file_name='processed_image.jpeg', mime='image/jpeg')
    else:
        st.write("Please upload an Image.")
main()