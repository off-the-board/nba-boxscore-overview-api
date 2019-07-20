import unittest
import sys
import json

from flask.cli import FlaskGroup

from project import create_app, db
from project.api.models import NBABoxscoreOverview


app = create_app()

cli = FlaskGroup(create_app=create_app)


@cli.command("recreate_db")
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    """Seeds the database."""
    db.session.add(NBABoxscoreOverview(date=20190312, data=json.load(open("./project/db/resources/20190312.json", "rb"))))
    db.session.commit()


@cli.command()
def test():
    """Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover("project/tests", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    sys.exit(result)


if __name__ == "__main__":
    cli()
