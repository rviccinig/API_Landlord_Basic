from flask_restful import Resource, reqparse
from models.user import User
from flask_jwt import jwt_required
#Resource to register a new '/register'
class register_user(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = register_user.parser.parse_args()

        if User.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = User(data['email'],data['username'], data['password'])
        user.save_to_db()

        return {"message": "User created successfully."}, 201

## Resource to see all registered users
class UserList(Resource):
    @jwt_required()
    def get(self):
        result=User.query.all()
        users_list=[]
        content={}
        return {'items': list(map(lambda x: str(x), result))}
