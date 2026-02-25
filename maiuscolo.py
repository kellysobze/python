nomi = ['anna','luca','ciccio']
#trasforma questi nome in maiucolo
def maiuscolo(nome):
    l=[]
    for i in nome:
        l.append(i.upper())
    return l
x=maiuscolo(nomi)
print(x)
