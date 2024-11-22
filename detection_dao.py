from base import db
from base.com.vo.detection_vo import DetectionVO

class detection_DAO:
    def insert_info(self, detection_vo):
        db.session.add(detection_vo)
        db.session.commit()

    def view_detection(self):
        detection_vo_list = db.session.query(DetectionVO).all()
        return detection_vo_list

    def delete_detection(self, patient_ID):
        detection_vo_list = DetectionVO.query.get(patient_ID)
        db.session.delete(detection_vo_list)
        db.session.commit()
        return detection_vo_list

    # def delete_detection(self, patient_ID):
    #     detection_vo = DetectionVO.query.filter_by(patient_ID=patient_ID).first()
    #     if detection_vo:
    #         db.session.delete(detection_vo)
    #         db.session.commit()

    # def update_sr_no_after_delete(self, deleted_sr_no):
    #     # Execute raw SQL to update sr_no for subsequent rows
    #     sql_query = text(
    #         f"UPDATE detection_Table SET sr_no = sr_no - 1 WHERE sr_no > {deleted_sr_no}"
    #     )
    #     db.session.execute(sql_query)

        # Check if there are any remaining rows
        # remaining_rows = db.session.query(DetectionVO).count()
        # if remaining_rows == 0:
        #     # Reset sr_no to start from 1 for MySQL
        #     reset_query = text(
        #         "TRUNCATE TABLE detection_Table"
        #     )
        #     db.session.execute(reset_query)
        #
        #     reset_auto_increment = text(
        #         "ALTER TABLE detection_Table AUTO_INCREMENT = 1"
        #     )
        #     db.session.execute(reset_auto_increment)

        # db.session.commit()

# from base import db
# from base.com.vo.detection_vo import DetectionVO
# from sqlalchemy import text
#
#
# class detection_DAO:
#     def insert_info(self, detection_vo):
#         db.session.add(detection_vo)
#         db.session.commit()
#
#     def view_detection(self):
#         detection_vo_list = db.session.query(DetectionVO).all()
#         return detection_vo_list
#
#     def delete_detection(self, sr_no):
#         detection_vo = DetectionVO.query.get(sr_no)
#         if detection_vo:
#             db.session.delete(detection_vo)
#             db.session.commit()
#             self.update_sr_no_after_delete(sr_no)
#         return detection_vo

