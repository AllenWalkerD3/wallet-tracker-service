from flask import Flask, jsonify, make_response, request
import os
from database import db

from models import Category



basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'wallet.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# @app.before_first_request
# def create_tables():
#     db.create_all()

# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     db.session.remove()


@app.route("/")
def hello_from_root():
    print(Category.query.all())
    return jsonify(message='Hello from root!')


@app.route("/hello")
def hello():
    return jsonify(message='Hello from path!')


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)

