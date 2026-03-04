import ese_csv
import json

class Richiesta:
    def __init__(self,nome,email,eta,categoria_eta,servizio):
        self.nome = nome
        self.email = email
        self.eta = eta
        self.categoria_eta = categoria_eta
        self.servizio = servizi

class Validadtor:
    @staticmethod
    def validate_row(row):
      try:
         if '@' not in row['email']:
            return False,'Indirizzo email non corretto'
         if not row['Nome'].strip():
            return False,'Nome mancante'
         eta = int(row['eta'])
         if eta < 18:
            return False,'Età non corretto'
         return True,None
      except KeyError as e:
         return False, e
      except ValueError as e:
         return False, e
      except Exception as e:
         return False, e



def categoria(age):
    if 18 <= age <= 25:
        return 'Junior'
    elif 26 <= age <= 40:
        return 'Adult'
    else:
        return 'Senior'


valid_requests = []
servizi_unici = set()
conteggio_servizi={}
try:
    with open('requests.csv',newline='') as csvfile:
              reader=csv.DictReader(csvfile)
    for row in reader:
        is_valid, error = validate_row(row)
        if not is_valid:
            continue
        nome = row["nome"].strip().title()
        email = row["email"].strip().lower()
        servizio = row["servizio"].strip().title()
        eta = int(row["eta"])

    cat = categoria(eta)
    richiesta = {
                "nome": nome,
                "email": email,
                "eta": eta,
                "categoria_eta": cat,
                "servizio": servizio
            }
    valid_requests.append(richiesta)
    servizi_unici.add(servizio)
    conteggio_servizi[servizio] = conteggio_servizi.get(servizio, 0) + 1

except FileNotFoundError:
           print("File non trovato")
except Exception as e:
           print(e)


output = {
         "totale_richieste": len(valid_requests),
         "servizi_unici": list(servizi_unici),
         "conteggio_servizi": conteggio_servizi,
         "richieste": valid_requests
          }
try:
    with open("output.json", "w") as f:
              json.dump(output, f, indent=4)
except Exception as e:
           print(e)

print("Done.")

