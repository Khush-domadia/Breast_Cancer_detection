from base import db
from base.com.vo.login_vo import loginVO


class login_DAO:
    def insert_login(self, login_vo):
        db.session.add(login_vo)
        db.session.commit()

    def login_validate_username(self, login_vo):
        login_vo_list = loginVO.query.filter_by(login_username=login_vo.user_name).all()
        return login_vo_list

    def login_validate_password(self, login_vo):
        login_vo_list = loginVO.query.filter_by(password=login_vo.password).all()
        return login_vo_list

    def print_login_table():
        login_entries = loginVO.query.all()
        for entry in login_entries:
            print(entry.as_dict())
