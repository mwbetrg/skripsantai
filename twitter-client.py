#!/usr/bin/python
#Created : Thu 06 Aug 2015 02:15:25 PM MYT
#Last Modified : Fri 21 Aug 2015 01:05:32 PM UTC

import os
import sys
from twitter import *

CONSUMER_SECRET = "pd4FVhqBHYkCvNwLnREvmPLmzakU5XL8iuMtfalAw7xu650kV6"

CONSUMER_KEY = "nybx7FHQTJl7u3I9rOpJrmduw"

ACCESS_TOKEN = "16709672-2CtfNKKaJWE1dTDz6M0EbBOCsvQ3DiQ9OjVQpjQsh"

ACCESS_TOKEN_SECRET = "YEiR4IizOObY9mjnTtcpAfobjrAsmIKZPwTj0SMeA1Els"

t = Twitter(auth=OAuth(ACCESS_TOKEN,
                       ACCESS_TOKEN_SECRET,
                       CONSUMER_KEY,
                    CONSUMER_SECRET
                    ))

#print t.statuses.home_timeline(count=5)

#t.statuses.update(status="Testing another twitter client")

#print t.search.tweets(q="#najib")

# Send a direct message
#t.direct_messages.new(
#user="awangjangok",
#text="Nok gi sembahyang doh ning!")


# Send images along with your tweets:
# - first just read images from the web or from files the regular way:
#with open("example.png", "rb") as imagefile:
#imagedata = imagefile.read()
## - then upload medias one by one on Twitter's dedicated server
## and collect each one's id:
#t_up = Twitter(domain='upload.twitter.com',
#auth=OAuth(token, token_key, con_secret, con_secret_key))
#id_img1 = t_up.media.upload(media=imagedata)["media_id_string"]
#id_img2 = t_up.media.upload(media=imagedata)["media_id_string"]
## - finally send your tweet with the list of media ids:
#t.statuses.update(status="PTT ★", media_ids=",".join([id_img1, id_img2]))
