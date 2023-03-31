import streamlit as st
import requests
from PIL import Image
import io

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

def app():
    # Set the app title
    st.title("Image Generator")
    st.write("This app generates images from text input.")
    st.write("Developed by ahsan")
    

    # Add a text input field for the user to enter text
    text_input = st.text_input("Enter text")

    # Add a button to submit the text
    if st.button("Generate"):
        # Call the query function with the user input
        image_bytes = query({
            "inputs": text_input,
        })

        # Display the generated image
        image = Image.open(io.BytesIO(image_bytes))
        st.image(image, caption="Generated Image")
if __name__ == "__main__":
    app()
