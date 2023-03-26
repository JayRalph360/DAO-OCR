import os
from flask import Flask,render_template,redirect,url_for,request
from flask_scss import Scss
#import our OCR function
from PIL import Image
import pytesseract
#from ocr_pro import ocr_core

#define a folder to store and later serve the images
UPLOAD_FOLDER = '/static/Test_Images/'

#allow files of a specific type
ALLOWED_EXTENSIONS = set(['png','jpg','jpeg','gif','tiff','tif'])
app = Flask(__name__)
Scss(app)

#app.config['DEBUG']=True

# function to check the file extension
def allowed_file(filename):
	return '.' in filename and \
			filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def ocr_core(file):
    # Open image using PIL
    image = Image.open(file)
    # Perform OCR using pytesseract
    text = pytesseract.image_to_string(image)
    # Resize the image
    new_size = (380, 240)
    image = image.resize(new_size)
    # Save the image
    image.save('static/test-img/temp.png')
    # Return extracted text
    return text

# route and function to handle the home page

@app.route("/", methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		return redirect(url_for('upload'))
		userEmail = request.form['username']
		userPassword = request.form['password']
		return flask.redirect('/')
		
	return render_template("login.html")
	
@app.route("/signup", methods=['GET', 'POST'])
def signup():
	if request.method == 'POST':
		return redirect(url_for('login'))
	return render_template("signup.html")
	
@app.route('/about', methods=['GET','POST'])
def about():
    return render_template('about.html')

@app.route('/service', methods=['GET','POST'])
def service():
    return render_template('service.html')

@app.route('/team', methods=['GET','POST'])
def team():
    return render_template('team.html')

@app.route('/contact', methods=['GET','POST'])
def contact():
    return render_template('contact.html')

@app.route("/upload", methods=['GET','POST'])
def upload():
	if request.method == 'POST':
		#check if there is a file in the request
		if 'file' not in request.files:
			return render_template('upload.html', msg='No file selected')
		file = request.files['file']
		# if no file is selected
		if file.filename == '':
			return render_template('upload.html', msg='No file selected')
		if file and allowed_file(file.filename):
			
			# call the OCR function on it
			extracted_text = ocr_core(file)
			
			# extract the text and display it
			return render_template('upload.html', msg='Successfully processed', extracted_text=extracted_text,img_src=UPLOAD_FOLDER + file.filename)
	elif request.method == 'GET':
		return render_template('upload.html')
		
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)