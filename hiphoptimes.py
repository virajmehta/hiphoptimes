#!/usr/local/bin/python
import requests
import requests.auth
import time
import json
from bs4 import BeautifulSoup


def main():
    while True:
        #import pdb; pdb.set_trace()
        x = requests.get('http://reddit.com/r/hiphopheads')
        if x.status_code == 200:
            soup = BeautifulSoup(x.text, 'html.parser')
            stringUsers = soup.find(class_='users-online')
            users = stringUsers.span.string.replace(',','')
            with open('traffic.txt', 'a') as output:
                output.write(time.strftime("%Y-%m-%d %H:%M") + '\n')
                output.write(users + '\n')
        time.sleep(600) #wait 10 minuntes before checking again


if __name__ == '__main__':
    main()


