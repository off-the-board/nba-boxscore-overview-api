from flask import Blueprint, request
from flask_restful import Api, Resource

from project.api.controllers import daily_gamelist_payload


daily_blueprint = Blueprint("daily", __name__)
api = Api(daily_blueprint)


class DailyGameList(Resource):

    def get(self):
        """Gets all games for a date"""
        date = request.args.get("date")
        if not date:
            return {}, 400
        return daily_gamelist_payload(date)


api.add_resource(DailyGameList, "/games/daily")
