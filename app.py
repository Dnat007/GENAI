from flask import Flask,render_template,request,url_for
from src.Gemini import generation_text
from src.Gemini import image_information
import markdown2
import os
app = Flask(__name__)
from PIL import Image


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/responsive_text',methods=['GET','POST'])
def answer():
    if request.method == "POST":
        text = request.form['text']
        answer = generation_text(input_text=text)
        answer_of_text = markdown2.markdown(answer)
        
    return render_template('response.html',text=text,answer_of_text = answer_of_text)

@app.route('/image_information',methods=["GET","POST"])
def img_description():
    if request.method == "POST":
        if 'image' not in request.files:
            return 'No file is present'
        image = request.files['image']
        if image.filename == '':
            return 'No selected file'
        load_img = image.filename
        img = Image.open(image)
        resized_img = img.resize((300, 300))
        resized_img.save('static/' + image.filename)
        
        answer = image_information(img=load_img)
        answer_img = markdown2.markdown(answer)
        return render_template('response_image.html', filename=load_img, answer_img = answer_img)
        
        
if __name__ == "__main__":
    app.run(debug=True)