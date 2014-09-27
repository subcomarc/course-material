# -*- coding: utf-8 -*-
import json
import re
MyListofKeys = []
TheVelibFile = open('velib.json')
MyVelibFile = json.load(TheVelibFile)
for corr in MyVelibFile:
    FutureZip = re.search('\d+', corr['address'])
    FutureName = re.search('\d+', corr['name'])
    corr['zip_code'] = FutureZip.group(0)
    corr['city'] = corr['address'][FutureZip.start()+6:]
    corr['address'] = corr['address'][:FutureZip.start()-3]
    corr['name'] = corr['name'][FutureName.end()+3:]
with open('solution.json', 'w') as output:
    json.dump(MyVelibFile, output)
