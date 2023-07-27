from flask import Flask, render_template,request
import os

app = Flask(__name__)

# Folder where uploaded files will be saved
UPLOAD_FOLDER = 'uploaded_files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return "No file part", 400

        file = request.files['file']

        # If the user does not select a file, the browser submits an empty part without filename
        if file.filename == '':
            return "No selected file", 400

        if file:
            # Save the file to the specified upload folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return render_template('index.html', message='File uploaded successfully!')

    
    return "Invalid request", 400


if __name__ == '__main__':
    app.run(debug=True)
