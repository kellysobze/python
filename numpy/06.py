import numpy as np
dataset=np.random.randint(0,100,(5,4))
#eta,altezza,peso,punteggio
#normalizzare le ultime tre colonne(altezza peso e punteggio),
# aggiungere una nuova colonna con la media dei tre,
# creare una copia del dataset e verificare che non viene alterato

#creo una copia di sicurezza
dataset_originale=dataset.copy()

#normalizzo le ultime tre colonne ovvero quelle con indice:1,2,3
features_ds = dataset[:,1:]
minimo = np.min(features_ds,axis=0)
massimo = np.max(features_ds,axis=0)
features_norm = (features_ds - minimo)/(massimo - minimo)
print(features_norm)

#sostituisco le features normalizzare al dataset originale
dataset[:,1:]=features_norm
print(dataset)

#calcolo la media delle features per ogni riga
media_features = np.mean(dataset[:,1:],axis=1)
media_features = media_features.reshape(-1,1)
dataset_con_media = np.hstack((dataset,media_features)) #hstack= orizzontal stack
print(dataset_con_media)

