# Python 3.6 ver
# Name : email_find
# -*- coding : utf -8 -*-

import re
import sys

foundemail = []

mailsrch = re.compile(r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
for line in open(sys.argv[1]):
    foundemail.extend(mailsrch.findall(line))

foundemail = list(set(foundemail)) #중복제
                  
print (foundemail)
