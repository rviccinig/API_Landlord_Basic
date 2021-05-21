
from db import db

class User(db.Model):
    __tablename__='user_table'
    __table_args__ = {'extend_existing': True}

    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(64),unique=True)
    username=db.Column(db.String(64),unique=True)
    password=db.Column(db.String(128))
    testing_field=db.Column(db.String(128))

    def __init__(self,email,username,password):
        self.email=email
        self.username=username
        self.password=password

    #This method saves teh user in the database
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # Delete User from database
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def __str__(self):
        return f"id:{self.id},email: {self.email},username:{self.username},password: {self.password}"

    # Instead of calling 'User' I use the decorator @classmethod, I can use this method without starting an instal of USER!
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls,id):
        return cls.query.filter_by(id=id).first()
