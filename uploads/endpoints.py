import os
from flask import request
from werkzeug.utils import secure_filename
from dronelib.server import gcs
from auth.core import permission
UPLOAD_FOLDER = 'C:/Users/SIKIRU/Desktop/GCSA/uploads'

ALLOWED_EXTENSIONS = {'json', 'py'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload(**kwargs):
    permission(kwargs['token_info'], access_role='basic')
    file = request.files['fileName']
    # # If the user does not select a file, the browser submits an
    # # empty file without a filename.
    if file.filename == '':
        return 'no file'
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
    if file.filename == 'paths.json':
        gcs.upload_path()
        return 'path file upload successful'
    if file.filename == 'config.py':
        print(file.filename)
        return 'config file upload successful'


