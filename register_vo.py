from base import db


class registerVO(db.Model):
    __tablename__ = 'register_Table'
    __table_args__ = {'extend_existing': True}

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('user_name', db.String(255), nullable=False)
    email = db.Column('email', db.String(255), nullable=False)
    pwd1 = db.Column('password', db.String(255), nullable=False)
    pwd2 = db.Column('confirm_password', db.String(255),  nullable=False)

    def bs_dict(self):
        return {
            'id': self.id,
            'user_name': self.name,
            'email': self.email,
            'password': self.pwd1,
            'confirm_password': self.pwd2
        }


# Create the tables
db.create_all()
