import json

with open("utenti.json",'r') as f:
    dati=json.load(f)
    print(dati["nome"])

