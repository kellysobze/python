#creare un modello che possa prevedere se un soggetto puo avere o meno un prestito da una banca
# le variabili sono eta, reddito anuno, numero debiti, credit score, approvazione:0,1

import numpy as np
np.random.seed(42)
dataset = np.array([
    [25,30000,2,650,1],
    [45,80000,1,720,1],
    [35,50000,5,580,0],
    [23,25000,3,600,0],
    [52,120000,0,800,1],
    [40,70000,4,610,0]])

#separiamo il dataset
x=dataset[:,:-1] #prende tutte le righe e le colonne tranne l'ultima (le feauters)
y=dataset[:,-1] #prende solo l'ultima colonna (il target=l'esito)
#calcolo min e max di ogni colonna delle featuters
minimo = np.min(x,axis=0)
massimo = np.max(x,axis=0)
x_norm=(x-minimo)/(massimo-minimo)
#features engigneering (creo la nuova feauters)
#estraggo la colonna reddito e debito (1,2) creo una nuova feauters che indica il rapporto tra i due
reddito = x[:,1]
debito = x[:,2]
rapporto_debito = debito / reddito
rapporto_debito=rapporto_debito.reshape(-1,1)
x_enhanced = np.hstack((x_norm,rapporto_debito))

indices=np.arange(len(x_enhanced))
np.random.shuffle(indices) #mischio gli indici

train_size=int(len(indices)*0.8)
train_idx=indices[train_size:]

x_train=x_enhanced[train_idx] #dati da mandare in train
x_test=x_enhanced[train_idx] #dati da testare

y_train=y[train_idx]
y_test=y[train_idx]
print(y_train)