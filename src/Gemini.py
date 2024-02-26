import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
from PIL import Image
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generation_text(input_text):
  
  textual_model = genai.GenerativeModel('gemini-pro')
  response = textual_model.generate_content(input_text)
  return response.text

def image_information(img):
    img_model = genai.GenerativeModel("gemini-pro-vision")
    my_img = Image.open('static/'+img)
    response = img_model.generate_content(my_img)
    return response.text