numeri=[5,12,26,30,20,9,14,209]
#creare una nuova lista solo con i numeri>10 e dividi per 2

number=[]
for i in numeri:
    if i>10:
        number.append(i/2)
print(number)