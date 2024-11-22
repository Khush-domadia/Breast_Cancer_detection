from base import db


class DetectionVO(db.Model):
    __tablename__ = 'detection_Table'
    __table_args__ = {'extend_existing': True}
    sr_no = db.Column(db.Integer, nullable=False, default=1)
    patient_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient_name = db.Column(db.String(100), nullable=False)
    input_image = db.Column(db.String(255))
    input_image_path = db.Column(db.String(255))
    status = db.Column(db.String(100), nullable=False)
    datetime = db.Column(db.String(100), nullable=False)

    def info_dict(self):
        return {
            'Sr No.': self.sr_no,
            'patient ID': self.patient_ID,
            'Patient Name': self.patient_name,
            'Input Image': self.input_image,
            'Input Image Path': self.input_image_path,
            'status': self.status,
            'Date and Time': self.datetime
        }


# Create the tables
db.create_all()
