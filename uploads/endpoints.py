import json
import os
from flask import request
from werkzeug.utils import secure_filename
from auth.core import permission
from basehandler import api_response
#'C:/Users/SIKIRU/Desktop/GCSA/uploads'
UPLOAD_FOLDER = 'C:/Users/SIKIRU/Desktop/GCSA/uploads'                 #'/app/uploads/'

#'C:/Users/SIKIRU/Desktop/GCSA/uploads/paths.json'
DOWNLOAD_FOLDER = 'C:/Users/SIKIRU/Desktop/GCSA/uploads/paths.json' #'/app/uploads/paths.json'   #'/uploads/paths.json'
ALLOWED_EXTENSIONS = {'json', 'py'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload(**kwargs):
    permission(kwargs['token_info'], access_role='basic')
    file = request.files['file']
    # # If the user does not select a file, the browser submits an
    # # empty file without a filename.
    if file.filename == '':
        return 'no file'
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
    if file.filename == 'paths.json':
        return 'path file upload successful'
    if file.filename == 'config.py':
        print(file.filename)
        return 'config file upload successful'


def download():
    file = DOWNLOAD_FOLDER
    with open(file, 'rb') as f:
        data = json.load(f)
        return api_response(data)



