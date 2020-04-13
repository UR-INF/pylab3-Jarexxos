import random
lista=[]
with open('result.txt','w') as result:
    for i in range(6):
        lista.append(round(random.uniform(-5,5),2))
        result.write(str(lista[i])+' ')