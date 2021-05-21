from db import db

class Vacant_Suite(db.Model):
    __tablename__='vacant_suite_table'
    __table_args__ = {'extend_existing': True}

    id=db.Column(db.Integer,primary_key=True)
    suite_number=db.Column(db.String(64))
    floor=db.Column(db.Integer())
    size=db.Column(db.Integer())
    building_id = db.Column(db.Integer, db.ForeignKey('Building_table.id'))
    building = db.relationship('Building')

    def __init__(self, suite_number, floor, size, building_id):
        self.suite_number= suite_number
        self.floor= floor
        self.size = size
        self.building_id = building_id

    def __str__(self):
        return "suite_number:{},floor:{},size:{},building_id:{}".format(self.suite_number,self.floor,self.size,self.building_id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_all(cls):
        return cls.query.all()
