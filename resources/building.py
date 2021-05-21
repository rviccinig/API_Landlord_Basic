## Create_Building
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.building import Building
import pandas as pd
import re
import json

class create_building(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('building_name',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    parser.add_argument('adress',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    parser.add_argument('city',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    parser.add_argument('state',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    parser.add_argument('zip',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    parser.add_argument('bldg_class',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    parser.add_argument('size',
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )

    parser.add_argument('available_area',
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )

    @jwt_required()
    def post(self):
        data = create_building.parser.parse_args()
        property= Building(**data)
        property.save_to_db()
        return {"message": "Property created successfully."}, 201


class PropertyList(Resource):
    #@jwt_required()
    def get(self):
        result=Building.query.all()
        property_list=[]
        content={}
        return {'Buildings': list(map(lambda x: str(x), result))}

# Massive Upload to Database Resource

class Massive_Upload(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('file_path',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    #@jwt_required()
    def post(self):
        file= Massive_Upload.parser.parse_args()
        dataFrame= pd.read_csv(file['file_path'])
        dictionary_1=dataFrame.to_dict(orient='records')
    #Reading row per row and saving it to the database
        for i in range(len(dictionary_1)):
            dataframe_row=dictionary_1[i]
            property= Building(**dataframe_row)
            property.save_to_db()
        return {"message": "Properties have been sucessfully created"}, 201
    #Delete all the database
    #@jwt_required()
    def delete(self):
        All_buildings=Building.find_all()
        for building in All_buildings:
            Building.delete_from_db(building)
        return {"message":"All buildings have been deleted"}
