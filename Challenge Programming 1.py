import requests

# send une request sur le site pour recup le code
headers = {'Cookie': 'WC=17687231-65384-HwWPH90KLlX1c1pb'} # set les info du cookie ( pour se connecter )
response = requests.get("https://www.wechall.net/challenge/training/programming1/index.php?action=request",headers.headers)
content = response.text
print(content)

# re-send une request sur le site pour donner la réponse
url = "https://www.wechall.net/challenge/training/programming1/index.php?answer=" + content
response = requests.get(url, headers=headers)