#!/usr/bin/python
# -*- coding: utf-8 -*-
from requests_oauthlib import OAuth1
import requests,platform,os,time
def utf(s):
    try: s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError: return False
    else: return True
###################################
# API Functions
login = lambda u,p: requests.post("https://api.twitter.com/auth/1/xauth_password.json",data={'x_auth_identifier':u,'x_auth_password':p},headers={'Authorization':'Bearer AAAAAAAAAAAAAAAAAAAAAFXzAwAAAAAAMHCxpeSDG1gLNLghVe8d74hl6k4%3DRUMF4xAQLsbeBhTSRrCiQpJtxoGWeyHrDb5te2jpGskWDFW82F','X-Guest-Token':requests.post("https://api.twitter.com/1.1/guest/activate.json",headers={"Authorization":"Bearer AAAAAAAAAAAAAAAAAAAAAFXzAwAAAAAAMHCxpeSDG1gLNLghVe8d74hl6k4%3DRUMF4xAQLsbeBhTSRrCiQpJtxoGWeyHrDb5te2jpGskWDFW82F"}).json()['guest_token']})
trend = lambda q,c,o1,o2: requests.get('https://api.twitter.com/2/search/adaptive.json?qf_abuse=true&q='+q.replace('#','%23')+'&query_source=trend_click&spelling_corrections=true&tweet_search_mode=live&earned=true&include_entities=true&include_cards=true&cards_platform=Android-12&include_carousels=true&ext=stickerInfo%2CmediaRestrictions%2CaltText%2CmediaStats%2CmediaColor%2Cinfo360%2CcameraMoment%2Cmaster_playlist_only&include_media_features=true&include_blocking=true&include_blocked_by=true&tweet_mode=extended&include_reply_count=true&include_composer_source=true&simple_quoted_tweet=true&include_ext_media_availability=true&include_user_entities=true&include_profile_interstitial_type=true',auth=OAuth1('3nVuSoBZnx6U4vzUxf5w','Bcs59EFbbsdF6Sl9Ng71smgStWEGwXXKSjYvPVt7qys',o1,o2,decoding=None)).text if not c else requests.get('https://api.twitter.com/2/search/adaptive.json?cursor=scroll%3A'+c.replace('=','%3D')+'&qf_abuse=true&q=%23'+q.replace('#','%23')+'&query_source=trend_click&spelling_corrections=true&tweet_search_mode=live&earned=true&include_entities=true&include_cards=true&cards_platform=Android-12&include_carousels=true&ext=stickerInfo%2CmediaRestrictions%2CaltText%2CmediaStats%2CmediaColor%2Cinfo360%2CcameraMoment%2Cmaster_playlist_only&include_media_features=true&include_blocking=true&include_blocked_by=true&tweet_mode=extended&include_reply_count=true&include_composer_source=true&simple_quoted_tweet=true&include_ext_media_availability=true&include_user_entities=true&include_profile_interstitial_type=true',auth=OAuth1('3nVuSoBZnx6U4vzUxf5w','Bcs59EFbbsdF6Sl9Ng71smgStWEGwXXKSjYvPVt7qys',o1,o2,decoding=None)).text

pversion = platform.python_version().split(".")[0]
uinput = lambda m: raw_input(m) if pversion=="2" else str(input(m))
###################################
if __name__ == '__main__':
	os.system('cls||clear')
	os.system('export PYTHONIOENCODING=utf-8')
	print('''+----------------------------------------------+
|       CoDeD By 1337r00t (@0x1337r00t)        |
|             Blackfox's Group ©               |
|----------------------------------------------|
|  Arabic Tags [Windows(CMD)]: only urlencode  |
|             TrendCatch © 2019                |
+----------------------------------------------+''')

	username = uinput('Your Twitter Username => ')
	password = uinput('Your Twitter Password => ')
	attemp = login(username,password)
	if attemp.status_code != 200:
		print("Username/Password Is incorrect")
		exit()
	print("Logged as "+username)
	X_Token,X_Secret = attemp.json()['oauth_token'],attemp.json()['oauth_token_secret']
	hashtag = uinput('Hashtag [With (#)] => ')
	if not utf(hashtag):
		unicode(hashtag, 'utf-8') if pversion=="2" else hashtag.encode('utf-8')
	search = trend(hashtag,None,X_Token,X_Secret)
	if '"tweets":{}' in search:
		print("Hashtag not found")
		exit()
	cursor = re.search('"value":"scroll:(.+?)","cursorType":"Bottom"', search).group(1)
	
	while True:
		print(cursor)
		search = trend(hashtag,cursor,X_Token,X_Secret)
		if '"tweets":{}' in search:
			print("First Tweet -> https://twitter.com/i/status/" + re.search('tweets":{"(.+?)":{', search).group(1))
			break
		else:
			cursor = re.search('"value":"scroll:(.+?)","cursorType":"Bottom"', search).group(1)
