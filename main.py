from flask import Flask
from flask_restful import Resource, Api
from src.routeer_main import mapper

app = Flask(__name__)
api = Api(app)
mapper(api)

if __name__ == '__main__':
    app.run()