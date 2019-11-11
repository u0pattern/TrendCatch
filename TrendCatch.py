#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from getpass import getpass

from api import login, trend
from util import init, uinput, py_version

def main():
    username = uinput('Your Twitter Username => ')
    password = getpass('Your Twitter Password => ')

    err, X_Token, X_Secret = login(username, password)
    
    if err != 0:
        print("Username/Password Is incorrect")
        return
    
    print("Logged as {}".format(username))
    
    while True: # Main loop
        hashtag = uinput("Hashtag ('q' to quit) => ").strip()
        
        if hashtag == 'q':
            print('Exiting...')
            return
        
        if hashtag == '':
            print('Invalid input')
            continue
        
        hashtag = unicode(hashtag, 'utf-8') if py_version==2 else hashtag
        search = trend(hashtag, None, X_Token, X_Secret)
        
        if '"tweets":{}' in search:
            print("Hashtag not found")
            continue
        
        cursor = re.search(
            '"value":"scroll:(.+?)","cursorType":"Bottom"', search).group(1)
        
        while True:
            print("Cursor -> "+cursor)
            last_tweet = re.search('tweets":{"(.+?)":{', search).group(1)
            search = trend(hashtag, cursor, X_Token, X_Secret)
            if '"tweets":{}' in search:
                print("First Tweet -> https://twitter.com/i/status/{}".format(last_tweet))
                break
            else:
                cursor = re.search(
                    '"value":"scroll:(.+?)","cursorType":"Bottom"', search).group(1)

if __name__ == '__main__':
    init()
    main()
