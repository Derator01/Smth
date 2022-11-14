x = 4**2018+2**2017-5
empty = ''
while x!=0:
    empty += str(x%2)
    x //= 2
    empty = empty[::-1]
print(empty)
print(empty.count('1'))