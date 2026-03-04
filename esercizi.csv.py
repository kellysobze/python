import ese_csv
with open('traccia.csv',newline='') as f_input:
    reader = csv.DictReader(f_input)
    utenti_modificati=[]
    for riga in reader:
        eta=int(riga('eta)'))
        if eta >= 27:
            categoria = 'Senior'
        else:
            categoria = 'Junior'
        riga['categoria'] = categoria
        utenti_modificati.append(riga)
    print(utenti_modificati)

with open('datinuovi.csv', 'w', newline='') as f_output:
    colonne=['nome','eta','citta','categoria']



