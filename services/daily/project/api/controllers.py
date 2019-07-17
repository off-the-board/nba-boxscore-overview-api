from nba_sdk.request_entities import ScoreboardV2
from nba_sdk.statsclient import NBAStatsClient

client = NBAStatsClient()


def daily_gamelist_payload(date):
    res = client.scoreboard_v2(ScoreboardV2(DayOffset=0, GameDate=date, LeagueID="00"))
    result_sets = res.json()["resultSets"]
    formatted_output = dict()
    for rs in result_sets:
        formatted_output[rs["name"]] = [dict(zip(rs["headers"], rs["rowSet"][i])) for i in range(len(rs["rowSet"]))]
    return formatted_output

