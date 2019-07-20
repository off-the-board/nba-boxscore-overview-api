import os

from flask import Flask
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy

cache = Cache()
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config.from_object(os.getenv("APP_SETTINGS"))

    cache.init_app(app)
    db.init_app(app)

    from project.api.daily import daily_blueprint
    app.register_blueprint(daily_blueprint)

    return app
