smth =0
isTrue = True

for a in range(100):
    for x in range(100):
        for y in range(100):
            if ((x<a)<=((x*x)<100)and(((y*y)<=64)<=(y<=a)))==0:
                isTrue = False
    if isTrue:
        smth +=1
        print(f"{a} {smth}")
    isTrue =True
#((x<5)<=((x*x)<a)and(((y*y)<=a)<=(y<=5)))
#((x<6)<=((x*x)<a))and(((y*y)<=a)<=(y<=6))