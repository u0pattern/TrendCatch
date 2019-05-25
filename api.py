# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1
import requests

LOGIN_URI = "https://api.twitter.com/auth/1/xauth_password.json"
AUTH_URI = "https://api.twitter.com/1.1/guest/activate.json"
ADAP_URI = "https://api.twitter.com/2/search/adaptive.json"

# TODO: Make sure those values are safe to share
AUTH_TOKEN = "Bearer AAAAAAAAAAAAAAAAAAAAAFXzAwAAAAAAMHCxpeSDG1gLNLghVe8d74hl6k4%3DRUMF4xAQLsbeBhTSRrCiQpJtxoGWeyHrDb5te2jpGskWDFW82F"
OAUTH_C_KEY = "3nVuSoBZnx6U4vzUxf5w"
OAUTH_C_SECRET = "Bcs59EFbbsdF6Sl9Ng71smgStWEGwXXKSjYvPVt7qys"


SEARCH_TAGS = ['qf_abuse=true',
               'query_source=trend_click',
               'spelling_corrections=true',
               'tweet_search_mode=live',
               'earned=true',
               'include_entities=true',
               'include_cards=true',
               'cards_platform=Android-12',
               'include_carousels=true',
               'ext=stickerInfo%2CmediaRestrictions%2CaltText%2CmediaStats%2CmediaColor%2Cinfo360%2CcameraMoment%2Cmaster_playlist_only',
               'include_media_features=true',
               'include_blocking=true',
               'include_blocked_by=true',
               'tweet_mode=extended',
               'include_reply_count=true',
               'include_composer_source=true',
               'simple_quoted_tweet=true',
               'include_ext_media_availability=true',
               'include_user_entities=true',
               'include_profile_interstitial_type=true'
               ]


def get_guest_token():
    return requests.post(AUTH_URI, headers={"Authorization": AUTH_TOKEN}).json()['guest_token']


def login(u, p):
    return requests.post(LOGIN_URI, data={'x_auth_identifier': u, 'x_auth_password': p}, headers={'Authorization': AUTH_TOKEN, 'X-Guest-Token': get_guest_token()})


def trend(q, c, o1, o2):
    query_string = 'q=%23{}&{}'.format(
        q.replace('#', '%23').replace('%23', ''),
        '&'.join(SEARCH_TAGS)
    )

    if c:
        query_string = 'cursor=scroll%3A{}&{}'.format(
            c.replace('=', '%3D'), query_string)

    return requests.get('{}?'.format(ADAP_URI, query_string),
                        auth=OAuth1(OAUTH_C_KEY, OAUTH_C_SECRET, o1, o2, decoding=None)).text
