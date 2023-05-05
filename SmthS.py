from fnmatch import *

var = 5321
for i in range(var, 10**10,var):
    if fnmatch(str(i), '12*135*9'):
        print(i, i//var)