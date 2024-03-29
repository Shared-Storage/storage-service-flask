from flask import Flask
from flask_smorest import Api
from flask_cors import CORS

from db import db
import models

from configuration.config import Config
from resources.item import blp as ItemBlueprint
from resources.location import blp as LocationBlueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    CORS(app)
    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(LocationBlueprint)

    return app
