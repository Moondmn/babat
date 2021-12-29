import os, datetime, requests, random, json
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# print(os.path.exists(os.path.join(desktop, 'text.txt')))
if not os.path.isfile(desktop +'\\text.txt'):
    # print(desktop +'\\test.txt')
    with open(f"{desktop}\\text.txt", "w+") as f:
        f.write(f"{datetime.datetime.now()}: hello my frinedo \n")
else:
    # print("lol")
    with open(f"{desktop}\\text.txt", "r+") as f:
        courent = f.read()
        # f.seek(0)
        f.write(f"\n{datetime.datetime.now()}: hahaha")
        # f.truncate()

WEBHOOK_URL = "https://discord.com/api/webhooks/923148096341409792/7NwILPhR6Xbch5bh-LctPDECd8ywgobJH4sVHwrSfolBUpnFnb0d3mV4UEwX_cxgUAcH"
if WEBHOOK_URL:
    webhook_data = {"username": "yOur goddamn token is here", "embeds": [
        dict(title="Found a valid Token",
            color=f'{random.randint(0, 0xFFFFFF)}',fields=[{
                                     "name": "**Account Info**",
                                     "value": f'Pedarat khorde shode hahah',
                                     "inline": True
                                 },
                             ]),
                    ]}
result = requests.post(WEBHOOK_URL, headers={"Content-Type": "application/json"}, data=json.dumps(webhook_data))
