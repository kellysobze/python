import numpy as np
studenti = np.array([[80,79,90],[60,75,90],[88,93,90],[55,60,70]])
#ogni riga è uno studente
# mentre ogni colonna è una materia
# calcola
# media per studente,
# media per materia,
# studenti con media >75,
# normalizzare

media_studenti = np.mean(studenti,axis=1) #media delle righe
media_materia = np.mean(studenti,axis=0) #media delle colonne
studenti_bravi = media_studenti > 75
studenti_sopra_75= studenti[studenti_bravi] #filtra all'interno degli studenti bravi
minimo = np.min(studenti_sopra_75)
massimo = np.max(studenti_sopra_75)
norm = (studenti - minimo)/(massimo - minimo)
print(media_materia)
print(media_studenti)
print(studenti_bravi)
print(norm)
