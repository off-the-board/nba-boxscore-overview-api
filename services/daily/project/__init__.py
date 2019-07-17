import os

from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config.from_object(os.getenv("APP_SETTINGS"))

    from project.api.daily import daily_blueprint
    app.register_blueprint(daily_blueprint)

    return app
