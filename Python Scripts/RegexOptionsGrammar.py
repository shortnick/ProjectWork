# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 20:38:57 2016

@author: Admin
"""
import re
#consequently, we can search for phone #'s 
#with and w/o area code or 1st dash
#also, /? for searching ?
phoneNumRegEx = re.compile(r'(\d{3}(\s)?(-)?|\(\d{3}\)(\s)?|\(\d{3}\)(-)?)?(\d{3}-\d{4})')
#1st optional block: \d{3}(\s)?(-)? will take naked area code with/out space or dash
#2nd:\(\d{3}\)(\s)?takes (111), with/out space
#3rd:\(\d{3}\)(-)? takes (111) with/out - (no spaces)
mo1 = phoneNumRegEx.search('My number is (415) 222-5345')
mo2 = phoneNumRegEx.search('My number is (415)-222-5345')
mo3 = phoneNumRegEx.search('My number is 222-5345')

print(mo1.group(),'\n',mo2.group(),'\n',mo3.group())