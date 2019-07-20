from sqlalchemy.dialects.postgresql.json import JSONB

from project import db


class NBABoxscoreOverview(db.Model):
    __tablename__ = "nba_boxscore_overview"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Integer, unique=-True, nullable=False)
    data = db.Column(JSONB)

    def __init__(self, date, data):
        self.date = date
        self.data = data
