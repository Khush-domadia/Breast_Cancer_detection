from base import db
from base.com.vo.register_vo import registerVO


class RegisterDAO:
    def insert_register(self, register_vo):
        db.session.add(register_vo)
        db.session.commit()

    def view_register(self):
        register_vo_list = registerVO.query.all()
        return register_vo_list

    def check_register_username(self, register_vo):
        register_vo_list = registerVO.query.filter_by(
            register_username=register_vo.name).all()
        return register_vo_list

    def update_register(self, register_vo):
        db.session.merge(register_vo)
        db.session.commit()

    def find_register_id(self, register_vo):
        register_vo_list = \
            registerVO.query.filter_by(
                register_username=register_vo.name).all()[-1].id
        return register_vo_list

    def register_validate_username(self, register_vo):
        register_vo_list = registerVO.query.filter_by(
            register_username=register_vo.name).all()
        return register_vo_list

    def register_validate_password(self, register_vo):
        register_vo_list = registerVO.query.filter_by(
            login_password=register_vo.login_password).all()
        return register_vo_list
