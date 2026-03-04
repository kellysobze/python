import numpy as np

numeri = [1,2,3,4]
#voglio moltiplicare tutte per due

nuovi = []
for n in numeri:
    numeri.append(n*2)
    pass
    #nuovi = [n*2 for n in numeri]

#con numpy
array = np.array(numeri)
nuovi = array*2
print(nuovi)

#array numerico casuale tra i 1 e 100,
# calcolare la media ,massimi,moltiplicare tutto per 3 e
# filtrare i numeri maggiori di 50
numeri_random=np.random(1,101,10)
media=np.mean(numeri_random)
massimo=np.max(numeri_random)
print(media)
print(massimo)