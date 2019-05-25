#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from getpass import getpass

from api import login, trend
from util import utf, init, uinput, py_version

def main():
    username = uinput('Your Twitter Username => ')
    password = getpass('Your Twitter Password => ')

    attempt = login(username, password)
    
    if attempt.status_code != 200:
        print("Username/Password Is incorrect")
        return
    
    print("Logged as {}".format(username))

    attempt = attempt.json()
    X_Token, X_Secret = attempt['oauth_token'], attempt['oauth_token_secret']
    
    hashtag = uinput('Hashtag [Without (# or %23)] => ')
	
    if not utf(hashtag):
		hashtag = (unicode(hashtag, 'utf-8') if py_version==2 else hashtag.encode('utf-8'))  
    
    search = trend(hashtag, None, X_Token, X_Secret)
    
    if '"tweets":{}' in search:
        print("Hashtag not found")
        return
    
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
