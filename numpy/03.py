import numpy as np
dati = np.array([[36,167,89],[37,185,92],[22,173,65]])

print(dati[:,0]) #stampa tutta la prima colonna

media= np.mean(dati,axis=0)  #axis = -1 fa la media sulle righe  mentra = 0 fa la media sulle colonne
print(media)