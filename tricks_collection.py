# -*- coding: utf-8 -*-
"""

Python Tricks

"""

###################################
## Counter in collections
###################################
from collections import Counter
# find the most frequent items in a list 
a=[1, 2, 3, 1, 2, 3, 2, 2, 3, 5, 1]
cnt = Counter(a)
cnt.most_common(2)

# check if two strings are composed of same characters with different orders
Counter("asdf") == Counter("fdas")

###################################
# reverse a list/string/integer
###################################
"asdf"[::-1]
"".join(reversed("asdf"))
int(str(12345)[::-1])

###################################
# transpose a 2-d array with zip and starred expression
'''
If the syntax *expression appears in the function call, expression must 
evaluate to an iterable. Elements from this iterable are treated as if they 
were additional positional arguments; if there are positional arguments 
x1, ..., xN, and expression evaluates to a sequence y1, ..., yM, this is 
equivalent to a call with M+N positional arguments x1, ..., xN, y1, ..., yM.
'''
###################################
a = [['a', 'b'], ['c', 'd'], ['e', 'f']]
list(zip(*a))

###################################
# chain comparison
###################################
a = 6
print(4 < a < 7)
print(4 == a < 7)


###################################
# chain function calls
###################################
def product(a,b):
    return a * b

def add(a,b):
    return a + b

b = True
print((product if b else add)(3,5))


###################################
# copy lists
###################################
a = [['a', 'b'], ['c', 'd'], ['e', 'f']]

# changes both b and a
b=a
b[0]="a"
# changes b only
b=a[:]
b[0]="a"
# copy list by typecasting method - changes b only
b=list(a)
b[0]="a"
# using the list.copy() method (python 3 only) - changes b only
b=a.copy()
b[0]="a"
# copy nested lists using copy.deepcopy
from copy import deepcopy
b=deepcopy(a)
b[0]="a"

# data frames
import pandas as pd
a=pd.DataFrame([['a', 'b'], ['c', 'd'], ['e', 'f']], columns=["c1", "c2"])
# changes both b and a
b=a.c1
b[0]='aa'

b=a.iloc[0,:]
b[0]="aa"

b=a.iloc[0:2,0:2]
b.iloc[0,0]="aa"

b._is_view
b.values.base is a.values.base

# also changes both b and a even b is now an array
b=a.values[0,:]
b[0]="aa"
b.base
b.view()

###################################
# sorting dictionaries
###################################
d={"b":4, "a":2, "c":3}
# sort dict by keys
sorted(d.items())
# sort keys by values
sorted(d, key=d.get)
# sort the dict by values
sorted(d.items(), key=lambda x: x[1])

###################################
# merge dictionaries
###################################
d1={"a": 1}
d2={"b": 2}
print({**d1, **d2})
print(dict(d1.items() | d2.items()))
d1.update(d2)

###################################
# for else - else gets called when for loop does not reach break statement
###################################
for el in [1, 2, 3, 4, 5]:
    if el==0:
        break
else:
    print("did not break out of the loop")

###################################
# return index of the min/max of a list
###################################
a = [1, 2, 3, 4, 5, -10, 6]
def minIndex(lst):
    return min(range(len(lst)), key=lst.__getitem__)
def maxIndex(lst):
    return max(range(len(lst)), key=lst.__getitem__)

minIndex(a)
maxIndex(a)

###################################
# strings in multiple lines
###################################
s1 = "Shall I compare thee to a Summer's day?"\
     "Thou are more lovely and more temperate:"
s2 = ("Rough winds do shake the darling buds of May,"
      "And Summer's lease hath all too short a date:")

# String Formatting
'from {1} to {0}'.format('A', 'B')
