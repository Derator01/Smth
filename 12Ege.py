for l in range(200, 300):
    i = '1'*l
    while ('1111' in i):
        i = i.replace("1111", '22', 1)
        i = i.replace("222",'1',1)
    print(f"{i} {l}")