# from flask import request, render_template, redirect, url_for
# from werkzeug.utils import secure_filename
# from base import app
# from base.service import testing
# from datetime import datetime
# from base.com.vo.detection_vo import DetectionVO
# from base.com.dao.detection_dao import detection_DAO
# import os
# from PIL import Image
#
# UPLOAD_FOLDER = 'base/static/adminResourses/upload_image'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#
#
# def allowed_file(filename):
#     ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
#     return '.' in filename and filename.rsplit('.', 1)[
#         1].lower() in ALLOWED_EXTENSIONS
#
#
# # @app.route('/upload', methods=['POST'])
# # def upload_file():
# #     if 'photo[]' not in request.files:
# #         return 'No file part', 400
# #
# #     files = request.files.getlist('photo[]')
# #     for file in files:
# #         if file.filename == '':
# #             return 'No selected file', 400
# #         if file and allowed_file(file.filename):
# #             filename = secure_filename(file.filename)
# #             filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
# #             file.save(filepath)
# #         else:
# #             return 'Invalid file', 400
#
#
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'photo[]' not in request.files:
#         return 'No file part', 400
#
#     files = request.files.getlist('photo[]')
#     for file in files:
#         if file.filename == '':
#             return 'No selected file', 400
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#
#             # Open the uploaded image
#             img = Image.open(file)
#
#             # Resize the image (e.g., to 200x200 pixels)
#             resized_img = img.resize((200, 200))
#
#             # Save the resized image
#             resized_img.save(filepath)
#         else:
#             return 'Invalid file', 400
#
#     # Calling functions from testing.py
#     status = testing.image_classification()
#     # status = testing.cancer_status()
#
#     # Create DetectionVO instance and set attributes
#     detection_vo = DetectionVO()
#
#     # Table Attributes
#     patient_name = request.form.get('patientName')
#     current_datetime = datetime.now()
#     datetime_string = current_datetime.strftime('%d-%m-%Y %H:%M')
#     detection_vo.datetime = datetime_string
#
#     # Insert data into the database
#     detection_vo.patient_name = patient_name
#     detection_vo.datetime = datetime_string
#     detection_vo.status = status
#
#     # for saving the image in table
#     image_name = files[0].filename
#     image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_name)
#     detection_vo.input_image = files
#     detection_vo.input_image_path = image_path.replace("base", "..").replace('\\', '/')
#
#     detection_dao = detection_DAO()
#     detection_vo_list = detection_dao.view_detection()
#     detection_dao.insert_info(detection_vo)
#
#     return 'Files uploaded successfully', 200
#
#
# @app.route('/detection', methods=['GET', 'POST'])
# def detection():
#     return render_template('admin/PerformDetection.html')
#
#
# @app.route('/audit_table', methods=['GET', 'POST'])
# def audit_table():
#     detection_dao = detection_DAO()
#     detection_vo_list = detection_dao.view_detection()
#     return render_template('admin/datatable.html', detection_vo_list=detection_vo_list)
#
#
# @app.route('/admin/delete_product')
# def admin_delete_product():
#     detection_dao = detection_DAO()
#     detection_vo = DetectionVO()
#     sr_no = request.args.get('sr_no')
#     detection_vo.sr_no = sr_no
#     detection_vo_list = detection_dao.delete_detection(sr_no)
#     file_path = (detection_vo_list.input_image_path.replace("..", "base"))
#     os.remove(file_path)
#     return redirect(url_for('audit_table'))

from flask import request, render_template, redirect, url_for, session
from werkzeug.utils import secure_filename
from base import app
from base.service import testing
from datetime import datetime
from base.com.vo.detection_vo import DetectionVO
from base.com.dao.detection_dao import detection_DAO
import os
from PIL import Image

UPLOAD_FOLDER = 'base/static/adminResourses/upload_image'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    return '.' in filename and filename.rsplit('.', 1)[
        1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'photo[]' not in request.files:
        return 'No file part', 400

    files = request.files.getlist('photo[]')
    for file in files:
        if file.filename == '':
            return 'No selected file', 400
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            # Open the uploaded image
            img = Image.open(file)

            # Resize the image (e.g., to 200x200 pixels)
            resized_img = img.resize((200, 200))

            # Save the resized image
            resized_img.save(filepath)
        else:
            return 'Invalid file', 400

    # Calling functions from testing.py
    status = testing.image_classification()
    # status = testing.cancer_status()

    # Create DetectionVO instance and set attributes
    detection_vo = DetectionVO()

    # Table Attributes
    patient_name = request.form.get('patientName')
    current_datetime = datetime.now()
    datetime_string = current_datetime.strftime('%d-%m-%Y %H:%M')
    detection_vo.datetime = datetime_string

    # Insert data into the database
    detection_vo.patient_name = patient_name
    detection_vo.datetime = datetime_string
    detection_vo.status = status

    # Trying to get Sr_no here and make it dynamic
    # img_list = os.listdir(UPLOAD_FOLDER)
    # Sr_no = len(img_list)
    # detection_vo.sr_no = Sr_no

    # for saving the image in table
    image_name = files[0].filename
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_name)
    detection_vo.input_image = files
    detection_vo.input_image_path = image_path.replace("base", "..").replace('\\', '/')

    detection_dao = detection_DAO()
    detection_vo_list = detection_dao.view_detection()
    detection_dao.insert_info(detection_vo)

    return 'Files uploaded successfully', 200


@app.route('/detection', methods=['GET', 'POST'])
def detection():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('admin/PerformDetection.html')


@app.route('/audit_table', methods=['GET', 'POST'])
def audit_table():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    detection_dao = detection_DAO()
    detection_vo_list = detection_dao.view_detection()
    count = len(detection_vo_list)
    return render_template('admin/datatable.html', detection_vo_list=detection_vo_list, count=count)


# @app.route('/admin/delete_product')
# def admin_delete_product():
#     if not session.get('logged_in'):
#         return redirect(url_for('login'))
#     detection_dao = detection_DAO()
#     detection_vo = DetectionVO()
#     patient_ID = request.args.get('patient_ID')
#     detection_vo.patient_ID = patient_ID
#     detection_vo_list = detection_dao.delete_detection(patient_ID)
#     file_path = (detection_vo_list.input_image_path.replace("..", "base"))
#     os.remove(file_path)
#     return redirect(url_for('audit_table'))

@app.route('/admin/delete_product')
def admin_delete_product():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    detection_dao = detection_DAO()
    patient_ID = request.args.get('patient_ID')

    # Getting patient-ID to remove associated image from backend
    detection_vo = DetectionVO.query.filter_by(patient_ID=patient_ID).first()

    # Perform deletion in the database
    detection_dao.delete_detection(patient_ID)

    # Remove associated file
    if detection_vo:
        file_path = (detection_vo.input_image_path.replace("..", "base"))
        os.remove(file_path)

    return redirect(url_for('audit_table'))

# @app.route('/admin/delete_product')
# def admin_delete_product():
#     if not session.get('logged_in'):
#         return redirect(url_for('login'))
#
#     detection_dao = detection_DAO()
#     sr_no = request.args.get('patient_ID')
#     detection_vo = detection_dao.delete_detection(sr_no)
#
#     if detection_vo:
#         file_path = (detection_vo.input_image_path.replace("..", "base"))
#         os.remove(file_path)
#
#         # Update sr_no for subsequent rows
#         detection_dao.update_sr_no_after_delete(sr_no)
#
#     return redirect(url_for('audit_table'))
