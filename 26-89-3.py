with open('26-89.txt') as f:
    data = f.readlines()
print(data)

n = int(data[0])
del data[0]
for i in range(n):
    data[i] = int(data[i])
print(n, data)

data.sort(reverse=True)
print(n, data)

cnt = 1
last = data[0]
for x in data:
    if x <= last - 3:
        cnt += 1
        last = x
print(cnt, last)
