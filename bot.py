#################################################################
# Title: bot.py
# Author: Sahaj Sarup
# Copyright (c) 2018 Linaro Limited
#################################################################

import tweepy
from weather import Weather, Unit
from datetime import datetime, timedelta, date
import pytz
import time
import logging
from systemd import journal
from github import Github

journal.send('96B_BOT: Starting Auth')


g = Github("<github api tocken>")

auth = tweepy.OAuthHandler("<consumer_key>", "<consumer_secret>")
auth.set_access_token("<access_token>", "<access_token_secret>")
api = tweepy.API(auth)

weatherc = Weather(unit=Unit.CELSIUS)
weatherf = Weather(unit=Unit.FAHRENHEIT)


##### TEST CODE ###############################################################

# ist_dt = datetime.now(pytz.timezone("Asia/Kolkata"))
# pst_dt = datetime.now(pytz.timezone("America/Los_Angeles"))
# uk_dt = datetime.now(pytz.timezone("Europe/London"))

# locationc = weatherc.lookup_by_location('delhi')
# forecastc = locationc.forecast
# delhi = "Delhi:\n"
# for forecast in forecastc:
#     delhi = delhi + forecast.text + '\n' + forecast.date + '\n' + forecast.high + ' C' + '\n' + forecast.low + ' C'  + '\n'
#    break

# locationc = weatherc.lookup(29224777)
# forecastc = locationc.forecast
# erode = "\nErode:\n"
# for forecast in forecastc:
#     erode = erode + forecast.text + '\n' + forecast.date + '\n' + forecast.high + ' C' + '\n' + forecast.low + ' C'  + '\n'
#     break

# locationc = weatherc.lookup(14979)
# forecastc = locationc.forecast
# camb = "\nCambridge:\n"
# for forecast in forecastc:
#     camb = camb + forecast.text + '\n' + forecast.date + '\n' + forecast.high + ' C' + '\n' + forecast.low + ' C'  + '\n'
#     break

# locationf = weatherf.lookup(2487889)
# forecastf = locationf.forecast
# sd = "\nSan Diego:\n"
# for forecast in forecastf:
#    sd = sd + forecast.text + '\n' + forecast.date + '\n' + forecast.high + ' F' + '\n' + forecast.low + ' F'  + '\n'
#    break

# print(delhi,erode,camb,sd,ist_dt.hour)

########################################################################


while True:
    if datetime.now(pytz.timezone("Asia/Kolkata")).hour == 9:
        locationc = weatherc.lookup_by_location('delhi')
        forecastc = locationc.forecast
        delhi = "@sahajsarup :\n"
        for forecast in forecastc:
            delhi = delhi + forecast.text + '\n' + forecast.date + '\n' + 'Max: ' + forecast.high + ' C' + '\n' + 'Min: ' + forecast.low + ' C'  + '\n'
            break

        locationc = weatherc.lookup(29224777)
        forecastc = locationc.forecast
        erode = "\n@mani_sadhasivam :\n"

        for forecast in forecastc:
            erode = erode + forecast.text + '\n' + forecast.date + '\n'  + 'Max: ' +  forecast.high + ' C' + '\n' +  'Min: ' +  forecast.low + ' C'  + '\n'
            break
        tweet = delhi + erode
        try:
            api.update_status(tweet);
            break
        except:
            journal.send('96B_BOT: Weather Status Update Failed!')

        for repo in g.get_repo("96boards/website").get_commits("master"):
            #print (str(repo.commit.committer.date)[0:11])
            if (str(repo.commit.committer.date)[0:10] == str(date.today() - timedelta(1))):
                a = "[website]\n"
                a = a + repo.commit.html_url + '\n'
                a = a + repo.commit.message[0:25] + '... \n'
                a = a + repo.commit.author.name + '\n'
                a = a + str(repo.commit.committer.date) + '\n\n'
                print(a, '\n')
                try:
                    api.update_status(a);
                    break
                except:
                    journal.send('96B_BOT: Website Commit IND Status Update Failed!')
                time.sleep(5)
            elif (str(repo.commit.committer.date)[0:10] < str(date.today() - timedelta(1))):
                break

        for repo in g.get_repo("96boards/documentation").get_commits("master"):
            #print (str(repo.commit.committer.date)[0:11])
            if (str(repo.commit.committer.date)[0:10] == str(date.today() - timedelta(1))):
                a = "[documentation]\n"
                a = a + repo.commit.html_url + '\n'
                a = a + repo.commit.message[0:25] + '... \n'
                a = a + repo.commit.author.name + '\n'
                a = a + str(repo.commit.committer.date) + '\n\n'
                print(a, '\n')
                try:
                    api.update_status(a);
                    break
                except:
                    journal.send('96B_BOT: Documentation Commit Status Update Failed!')
                time.sleep(5)
            elif (str(repo.commit.committer.date)[0:10] < str(date.today() - timedelta(1))):
                break

    if datetime.now(pytz.timezone("America/Los_Angeles")).hour == 10:
            locationf = weatherf.lookup(2487889)
            forecastf = locationf.forecast
            sd = "@sdrobertw \n"
            for forecast in forecastf:
                sd = sd + forecast.text + '\n' + forecast.date + '\n' + forecast.high + ' F' + '\n' + forecast.low + ' F'  + '\n'
                break
            tweet = sd
            try:
                api.update_status(tweet);
                break
            except:
                journal.send('96B_BOT: Weather Status SD Update Failed!')

    time.sleep(3600)
