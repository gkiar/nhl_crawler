#!/usr/bin/env python

import requests
import json


baseurl = "https://statsapi.web.nhl.com/api/v1/"

def get_game_ids(start_date, end_date):
    requrl = baseurl +\
             "schedule?" +\
             "startDate={0}".format(start_date) +\
             "&endDate={0}".format(end_date) +\
             "&expand=schedule.teams"
    r = requests.get(requrl)
    data = r.json()

    gids = []
    for date in data['dates']:
        for game in date['games']:
            gids += [game['gamePk']]

    return gids


def get_game_pbp(gid):
    requrl = baseurl +\
             "game/" +\
             str(gid) +\
             "/feed/live"

    r = requests.get(requrl)
    data = r.json()

    return data


def main():
    start_date = "2017-01-01"
    end_date = "2017-01-02"

    games = get_game_ids(start_date, end_date)
    print(games)

    pbp = get_game_pbp(games[0])
    import pdb; pdb.set_trace()
    print(pbp)


if __name__ == "__main__":
    main()
