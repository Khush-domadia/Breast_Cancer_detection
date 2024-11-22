from base import db


class loginVO(db.Model):
    __tablename__ = 'login_Table'
    __table_args__ = {'extend_existing': True}
    login_ID = db.Column('login_ID', db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column('user_name', db.String(255), db.ForeignKey('register_Table.user_name'), nullable=False)
    password = db.Column('password', db.String(255), db.ForeignKey('register_Table.password'), nullable=False)
    role = db.Column('role', db.String(255), nullable=False)
    status = db.Column('status', db.Boolean, nullable=False)

    def as_dict(self):
        return {
            'login_ID': self.login_ID,
            'user_name': self.user_name,
            'password': self.password,
            'role': self.role,
            'status': self.status
        }


db.create_all()
