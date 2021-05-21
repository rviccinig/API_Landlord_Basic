from db import db


class Building(db.Model):
    __tablename__='Building_table'
    __table_args__ = {'extend_existing': True}

    id=db.Column(db.Integer,primary_key=True)
    building_name=db.Column(db.String(64),unique=True)
    adress=db.Column(db.String(64),unique=True)
    city=db.Column(db.String(64))
    state=db.Column(db.String(64))
    zip=db.Column(db.String(64))
    bldg_class=db.Column(db.String(64))
    size=db.Column(db.Integer())
    available_area=db.Column(db.Integer)
    vacancy=db.Column(db.Integer)
    vacant_suites = db.relationship('Vacant_Suite')

    def __init__(self,building_name,adress,city,state,zip,bldg_class,size,available_area):
        self.building_name=building_name
        self.adress=adress
        self.city=city
        self.state=state
        self.zip=zip
        self.bldg_class=bldg_class
        self.size=size
        self.available_area=available_area
        self.vacancy=round((available_area/size)*100,2)

    #Updating occupation is a post method
        #This method saves teh user in the database
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    # This is fundamental in order to organize what I am putting in the database
    def __str__(self):
        return "id:{},Building:{},Adress:{},City:{},State:{},Zip:{},Class:{},Size:{},Available:{},Vacancy:{}".format(self.id,self.building_name,
                                                                                                    self.adress,self.city,self.state,
                                                                                                    self.zip,self.bldg_class,self.size,self.available_area,
                                                                                                    self.vacancy)
