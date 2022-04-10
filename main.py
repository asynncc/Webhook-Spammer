import requests, logging, json, time, os, threading; from pystyle import *; from itertools import cycle

def HomePrint():
    print(Colorate.Horizontal(Colors.rainbow, f"""
▄▄▌ ▐ ▄▌▄▄▄ .▄▄▄▄·  ▄ .▄            ▄ •▄     .▄▄ ·  ▄▄▄· ▄▄▄· • ▌ ▄ ·. • ▌ ▄ ·. ▄▄▄ .▄▄▄  
██· █▌▐█▀▄.▀·▐█ ▀█▪██▪▐█▪     ▪     █▌▄▌▪    ▐█ ▀. ▐█ ▄█▐█ ▀█ ·██ ▐███▪·██ ▐███▪▀▄.▀·▀▄ █·
██▪▐█▐▐▌▐▀▀▪▄▐█▀▀█▄██▀▐█ ▄█▀▄  ▄█▀▄ ▐▀▀▄·    ▄▀▀▀█▄ ██▀·▄█▀▀█ ▐█ ▌▐▌▐█·▐█ ▌▐▌▐█·▐▀▀▪▄▐▀▀▄ 
▐█▌██▐█▌▐█▄▄▌██▄▪▐███▌▐▀▐█▌.▐▌▐█▌.▐▌▐█.█▌    ▐█▄▪▐█▐█▪·•▐█ ▪▐▌██ ██▌▐█▌██ ██▌▐█▌▐█▄▄▌▐█•█▌
 ▀▀▀▀ ▀▪ ▀▀▀ ·▀▀▀▀ ▀▀▀ · ▀█▄▀▪ ▀█▄▀▪·▀  ▀     ▀▀▀▀ .▀    ▀  ▀ ▀▀  █▪▀▀▀▀▀  █▪▀▀▀ ▀▀▀ .▀  ▀

> Made By async
_______________________________________________________________________________________________
                                         [LOG]:""",1))

proxies = open('proxies.txt').read().split('\n')
proxy = cycle(proxies)

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def Title():
    os.system('title Webhook Spammer (V1) - Made By async.')

logging.basicConfig(
    level=logging.INFO,
    format="\033[38;5;21m[\033[0m%(asctime)s.%(msecs)03d\033[38;5;21m] \033[0m%(message)s\033[0m", 
    datefmt="%H:%M:%S" 
)

# Use for faster requests
session = requests.Session()

Title()
Clear()
HomePrint()
webhook = input(f"URL : ")
r = session.get(webhook)
if r.status_code == 200:
    logging.info(f"Valid Webhook.")
    time.sleep(1)
else:
    logging.info(f"Invalid Webhook.")
    time.sleep(3)
    exit()
time.sleep(1)
Clear()
HomePrint()
message = input(f"Message : ")
time.sleep(1)
Clear()
HomePrint()
amount = input(f"Amount : ")

def Webhookspam():
    s = session.post(webhook, proxies={"http": 'http://' + next(proxy)}, json = {"content" : message}, params = {'wait' : True})
    if s.status_code in (200, 201, 203, 204, 205, 206, 207, 208, 210):
        logging.info(f"Spammed : {message}")
    if 'retry_after' in s.text:
        time.sleep(s.json()['retry_after'])
        logging.info(f"RateLimited, Retrying After : {s.json()['retry_after']}s.")
    if s.status_code == 400:
        logging.info(f"Failed")

if __name__ == "__main__":
    Clear()
    HomePrint()
    for i in range(int(amount)):
        h = threading.Thread(target=Webhookspam).start()