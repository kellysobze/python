import ese_csv
import json

#funzione di validazione
def validate_row(row):
    try:
        if not row["nome"].strip():
            return False, "Nome mancante"
        if not row["citta"].strip():
            return False,"Citta mancante"
        eta=int(row["eta"])
        if eta <0:
            return False, "Età non valida"
        return True, None
    except: KeyError as e:
        return False
    except: ValueError as e:
        return False


def calculate_category(age):
    if age < 26:
        return ('Junior')
    elif age < 30:
        return ('Senior')
    elif age < 25:
        retunr ('senior')
#pypeline
    try:
        with open('esercizi2.join',newline='') as  f_input\
             open('valid_user.csv','w',newline='') as f_valid_users:\
             open('invalid_user.csv','w',newline='') as f_invalid_users:
             reader = csv.reader(f)
        valid_fieldnames = redaer.fieldnames + ["categoria"]
        invalid_fieldnames = redaer.fieldnames + ["errore"]
        valid_writer = writerheader()
        invalid_writer = writerheader()
    for row in reader:
is _valid.error= validate_row(row)
if is_valid :
    eta=int(row["eta"])
    category = calculate_category(eta)
    row["categoria"] = category



