#importing necessary libraries
import streamlit as st
import tempfile
from rembg import remove
from PIL import Image
from io import BytesIO

st.header("Background Remover App")


image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if image is not None:
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    # Convert the file-like object to bytes
    image_bytes = image.read()

    # Use BytesIO to create a file-like object from the bytes data
    image_io = BytesIO(image_bytes)

    # Use PIL to open the image from the file-like object
    uploaded_image = Image.open(image_io)
    
    with st.spinner('Removing background...'):
        # Use rembg.remove() with bytes data
        output_bytes = remove(image_bytes)
    
    # Use BytesIO to create a file-like object from the processed bytes data
    output_io = BytesIO(output_bytes)
    
    # Use PIL to open the processed image from the file-like object
    processed_image = Image.open(output_io)
    
    st.image(processed_image, caption='Processed Image.', use_column_width=True)
    
    # Add a download button for the processed image
    st.download_button(label='Download', data=output_bytes, file_name='processed_image.png', mime='image/png')
else:
    st.write("Please upload an image file.")