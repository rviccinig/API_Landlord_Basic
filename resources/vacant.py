## Create_Building
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.vacant import Vacant_Suite
import pandas as pd
import re
import json

class add_vacancy(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('suite_number',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    parser.add_argument('floor',
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )

    parser.add_argument('size',
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )

    parser.add_argument('building_id',
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )

    @jwt_required()
    def post(self):
        data = add_vacancy.parser.parse_args()
        vacancy= Vacant_Suite(**data)
        vacancy.save_to_db()
        return {"message": "Vacant Suite Created Successfully."}, 201


class Vacancy_List(Resource):
    #@jwt_required()
    def get(self):
        result=Vacant_Suite.query.all()
        return {'Vacancies': list(map(lambda x: str(x), result))}

# Massive Upload to Database Resource

class Vacancy_Massive_Upload(Resource):
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
            vacancy=Vacant_Suite(**dataframe_row)
            vacancy.save_to_db()
        return {"message": "Vacacncies have been sucessfully created"}, 201
    #Delete all the database
    #@jwt_required()
    def delete(self):
        All_vacancies=Vacant_Suite.find_all()
        for vacancy in All_buildings:
            Vacant_Suite.delete_from_db(vacancy)
        return {"message":"All vacancies have been deleted"}
