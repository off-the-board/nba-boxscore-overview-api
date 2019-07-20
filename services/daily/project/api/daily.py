from flask import Blueprint
from flask_restful import Api, Resource

from project import cache
from project import db
from project.api.controllers import daily_gamelist_payload
from project.api.models import NBABoxscoreOverview

import datetime

daily_blueprint = Blueprint("daily", __name__)
api = Api(daily_blueprint)


class DailyGameList(Resource):

    @cache.memoize(600)
    def get(self, date):
        """Gets all games for a date"""
        if not date:
            return {}, 400
        formatted_date = datetime.datetime.strptime(date, "%Y%m%d")
        if formatted_date < datetime.datetime.today():
            daily_boxscore = NBABoxscoreOverview.query.filter_by(date=int(date)).first()
            print("Querying...")
            if not daily_boxscore:
                print("Not found")
                data = daily_gamelist_payload(formatted_date.strftime("%Y-%m-%d"))
                db.session.add(NBABoxscoreOverview(date=int(date), data=data))
                return data
            else:
                print("Found")
                return daily_boxscore.data
        else:
            return daily_gamelist_payload(formatted_date.strftime("%Y-%m-%d"))


api.add_resource(DailyGameList, "/games/daily/<date>")
