import numpy as np

punteggi = np.array([23,46,78,98,34,65,32,67,45,20])

# per calcolare la percentuale di studenti sopra la media
media = np.mean(punteggi)
sopra_media = punteggi > media #MASCHERA BOOLEANA CHE TRAMITE OPERAZIONI VETTORIALE FA IL CONFRONTO ELEEMENTO PER ELEMENTO
print(sopra_media)

#per contare quanti sono i voti sopra la media
numeri_sopra_media = np.sum(sopra_media)
print(numeri_sopra_media)

#percentuale di numeri sopra la media
pc= (numeri_sopra_media / len(punteggi)*100)
print(pc)

minimo = np.min(punteggi)
massimo = np.max(punteggi)
normalizzati = (punteggi - minimo) / (massimo - minimo)
print(normalizzati)