import string
def create_hist(file):
    with open(file,'r') as f:
        text = f.read().lower()
        result = dict()
        for i in text:
            if i in result.keys():
                result[i] += 1
            elif i.isalpha():
                result[i] = 1
    return result
print(create_hist('lab3zad5.txt'))