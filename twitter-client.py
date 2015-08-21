#!/usr/bin/python
#Created : Thu 06 Aug 2015 02:15:25 PM MYT
#Last Modified : Fri 21 Aug 2015 12:59:57 PM UTC

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
