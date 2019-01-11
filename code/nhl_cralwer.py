#!/usr/bin/env python

import requests
import json


baseurl = "https://statsapi.web.nhl.com"

def get_game_ids(start_date, end_date):
    requrl = baseurl +\
             "/api/v1/" +\
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
    pass


def main():
    start_date = "2017-01-01"
    end_date = "2017-01-02"

    games = get_game_ids(start_date, end_date)
    print(games)


if __name__ == "__main__":
    main()
