from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Sample API',
          description='A sample API',
          )

usr = api.namespace('user', description='VK Users Operations')

@usr.route('/healthCheck')
class Hello(Resource):
    def get(self):
        return {'Yasos Biba Studios': True}



@usr.route('/user/communities/<id>')
@api.doc(params={'id': 'vk user id'})
class UserComminities(Resource):
    @cross_origin()
    def post(self, id):
        return {}


@usr.route('/user/friends/<id>')
@api.doc(params={'id': 'vk user id'})
class UserFriends(Resource):
    @cross_origin()
    def post(self, id):
        return {}

@usr.route('/user/authorize/<id>')
@api.doc(params={'id': 'vk user id'})
class UserAuthorize(Resource):
    @cross_origin()
    def get(self, id):
        return {}


if __name__ == '__main__':
    app.run()
