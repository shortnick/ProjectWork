# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 19:23:43 2016

@author: Admin
"""

import re

#r'stringhere' means RAW string, so no escape chars needed
# \d is regex for digit
# http://www.regexpal.com/ for checking regex expression
# and a cheat sheet
phoneNumRegEx = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')


mo = phoneNumRegEx.search('My number is 545-929-8732.')
# mo is a 'Match object' has attribute .group()

print('Phone number found: '+ mo.group())


#grouping by parenthesis
phoneNumRegEx = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')


mo = phoneNumRegEx.search('My number is 545-929-8732.')


print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
# .group(0) is the whole match, subparts start numbering at 1

#print all, as list of text strings w/in paren's
print(mo.groups())

#label the subgroups
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

#to retain/match paren's in search strings, escape them with \
#explicitly, regex uses \ to escape like python does
phoneNumRegEx = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')


#mo = phoneNumRegEx.search('My number is (545)-929-8732.')
#print(mo.group())
#notice the '-' difference
mo = phoneNumRegEx.search('My number is (545) 929-8732.')
print(mo.group())

### the pipe--> | <-- means 'OR' and will return 1st instance of either side
# see also .findall() at https://automatetheboringstuff.com/chapter7/#calibre_link-60
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
mo2 = heroRegex.search('Tina Fey loves Batman')

print(mo1.group())
print(mo2.group())

#use paren's and pipes to group multiple options
#pipes can also be used as search string with \|
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a while while BatBat was Batcopter pilot.')
print(mo.group())
#despite being a single word, the search result has 2 logical parts
print(mo.group(1))

#use paren's to section off a chunk, followed by ?
#for optional requirements
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('Batwoman beat Batman')
print(mo2.group())
#oddly, mo2.groups() returns only the optional bit
print(mo2.groups())

#consequently, we can search for phone #'s 
#with and w/o area code or 1st dash
#also, /? for searching ?
phoneNumRegEx = re.compile(r'(\(\d{3}\d-)?\d{3}-d{4}')
#mo1 doesn't work correctly
mo1 = phoneNumRegEx.search('My number is (415) 222-5345')
mo2 = phoneNumRegEx.search('My number is (415)-222-5345')
mo3 = phoneNumRegEx.search('My number is 222-5345')

print(mo1.group(), mo2.group(),mo3.group())

#replacing ? with * makes it a wildcard-multimatch
# adding {3,} after paren's will match 3+ instances
# {,5} will do up to five times
# {3,5} will do 3 to 5 instances
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())

#greedy- is the natural state of python, returning longest string
# {3,5}? will return the shortest string
