temperature = [18,22,30,12,15,32,27,19,28,20]
#creare una nuova lista con le temperature superiori a 20
def temp(temperatura):
    t=[]
    for i in temperatura:
        if i > 20:
            t.append(i)
    return t
x=temp(temperature)
print(x)