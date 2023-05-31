# backend (серверная часть)
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api()

persons = {1: {'login': 'Sergei', 'password': 234},
           2: {'login': 'Ivan', 'password': 45325}}


class Main(Resource):
    def get(self, id):
        if id == 0:
            return persons
        else:
            return persons[id]


api.add_resource(Main, '/api/persons/<int:id>')
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=3000, host='127.0.0.1')
