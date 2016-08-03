#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import zipfile
import datetime
import json

alexa_url = "http://s3.amazonaws.com/alexa-static/top-1m.csv.zip"
alexa_file = "top-1m.csv.zip"
user_agent = {"User-agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0"}
r = requests.get(alexa_url, headers=user_agent)
with zipfile.ZipFile(alexa_file, 'r') as alexa_lists:
    for name in alexa_lists.namelist():
        if name == "top-1m.csv":
            with alexa_lists.open(name) as top:
                top1000 = top.readlines()[0:999]
        else:
            continue

alexa_warninglist = {}

alexa_warninglist['description'] = "Event contains one or more entries from the top 1000 of the most used website (Alexa)."
d = datetime.datetime.now()
alexa_warninglist['version'] = "{0}{1:02d}{2:02d}".format(d.year,d.month,d.day)
alexa_warninglist['name'] = "Top 1000 website from Alexa"
alexa_warninglist['list'] = []
alexa_warninglist['matching_attributes'] = ['hostname','domain']

for site in top1000:
    v = str(site).split(',')[1]
    alexa_warninglist['list'].append(v[:-3])
print (json.dumps(alexa_warninglist))
