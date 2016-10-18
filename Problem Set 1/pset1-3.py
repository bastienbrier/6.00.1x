# -*- coding: utf-8 -*-
s = 'ibcwpyyrwhoqjwucotx'

substring = s[0]
word = s[0]

for i in range(len(s) - 1):
    if s[i+1] >= s[i]:
        substring += s[i+1]
        if len(substring) > len(word):
            word = substring
    else:
        substring = s[i+1]

print "Longest substring in alphabetical order is: " + str(word)