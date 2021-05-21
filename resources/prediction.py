# Prediction using the machine learning model
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from sklearn.linear_model import LogisticRegression
import numpy as np
import pickle

class prediction_regression(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('size',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('A',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    parser.add_argument('B',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    parser.add_argument('C',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    #Do prediction:
    def get(self):
        data = prediction_regression.parser.parse_args()
        pkl_filename="/home/rviccinig/Desktop/Landlord_API/machine_learning/regression_vacancy_prediction.pkl"
        with open(pkl_filename, 'rb') as file:
            pickle_model = pickle.load(file)
        User_Values=np.array([data['size'],data['A'],data['B'],data['C']]).reshape(1, -1)
        Ypredict = pickle_model.predict(User_Values)
        return{"Predicted Availability:":str(round(Ypredict[0],2)) + " s.f."}
