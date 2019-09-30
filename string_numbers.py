#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 13:32:35 2019

extracting non-zero numbers in between strings

@author: yuribyk
"""
from collections import Counter


a="clsdkjciow349rifoejfojer93ti0ofkjgs0dfjg095totiejgkfjg04g094g0wijrg04jgop4gj450g4jg"


numlist=[]
y=0
poww=-1


for i in range(len(a),0,-1):
    
    
    try:
        x= int(a[i-1])
        poww+=1
        y+= x*(10**poww)
        
        
    except ValueError:
        if y!=0:
            numlist.append(y)
        y=0
        poww=-1
    
        
print("")
print(numlist)



paragraph = """Emancipation is any effort to procure economic and social\
 rights, political rights or equality, often for a specifically\
 disenfranchised group, or more generally, in discussion of such\
 matters. Emancipation stems from ēx manus capere ('detach from\
 the hand'). Among others, Karl Marx discussed political emancipation\
 in his 1844 essay "On the Jewish Question", although often in\
 addition to (or in contrast with) the term human emancipation.\
 Marx's views of political emancipation in this work were summarized\
 by one writer as entailing "equal status of individual citizens\
 in relation to the state, equality before the law, regardless of\
 religion, property, or other 'private' characteristics of individual\
 people."[1]

"Political emancipation" as a phrase is less common in modern usage,\
 especially outside academic, foreign or activist contexts. However,\
 similar concepts may be referred to by other terms. For instance,\
 in the United States the Civil Rights Movement culminated in the\
 Civil Rights Act of 1964, the Voting Rights Act of 1965, and the\
 Fair Housing Act of 1968 can be seen as further realization of events\
 such as the Emancipation Proclamation and abolition of slavery a\
 century earlier. In the current and former British West Indies\
 islands the holiday Emancipation Day is celebrated to mark the\
 end of the Atlantic slave trade."""
 
print(paragraph)
print(len(paragraph))
word_list = paragraph.split()
words = Counter(word_list)
print(words)