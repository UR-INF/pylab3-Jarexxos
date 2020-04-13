def rev():
    list=[]
    i=0
    while True:
        x=input("test: ")
        if x!="koniec":
            list.append(x)
            i+=1
        else:
            break
    z = len(list)
    for z in range(len(list)-1,-1,-1):
        print(list[z])
rev()