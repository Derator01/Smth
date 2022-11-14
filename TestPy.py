
count = 0
for a in range(300):
    k = 0
    for x in range(300):
        for y in range(300):
            if ((x < 6) <= (x**2 < a)) and ((y**2 <= a) <= (y <= 6)):
                k += 1
    if k == 90000: 
        count += 1
#print(count)
