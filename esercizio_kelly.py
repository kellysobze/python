import ese_csv
import json
from abc import ABC, abstractmethod


class BaseValidator(ABC):
    @abstractmethod

    def validate(self, row):
        pass


class Validator(BaseValidator):
    def validate(self, row):
        try:
            if '@' not in row['email']:
                return False
            if not row['nome'].strip():
                return False
            if int(row['eta']) < 18:
                return False
            return True
        except KeyError:
            return False
        except ValueError:
            return False


class Pipeline:
    def __init__(self, validator):
        self.validator = validator

    def categoria(self, eta):
        if eta <= 25:
            return "Junior"
        elif eta <= 40:
            return "Adult"
        else:
            return "Senior"

    def run(self):

        valid_requests = []
        servizi_unici = set()
        conteggio_servizi = {}

        try:
            with open("requests.csv", newline="") as f:
                reader = csv.DictReader(f)

                for row in reader:

                    # Sanificazione
                    nome = row["nome"].strip().title()
                    email = row["email"].strip().lower()
                    servizio = row["servizio"].strip().title()
                    eta = int(row["eta"].strip())

                    row["nome"] = nome
                    row["email"] = email
                    row["eta"] = eta
                    row["servizio"] = servizio

                    if not self.validator.validate(row):
                        continue

                    categoria_eta = self.categoria(eta)

                    richiesta = {
                        "nome": nome,
                        "email": email,
                        "eta": eta,
                        "categoria_eta": categoria_eta,
                        "servizio": servizio
                    }

                    valid_requests.append(richiesta)

                    servizi_unici.add(servizio)
                    conteggio_servizi[servizio] = conteggio_servizi.get(servizio, 0) + 1

        except FileNotFoundError:
            print("File not found")
            return None

        output = {
            "totale_richieste": len(valid_requests),
            "servizi_unici": list(servizi_unici),
            "conteggio_servizi": conteggio_servizi,
            "richieste": valid_requests
        }

        with open("output.json", "w") as f:
            json.dump(output, f, indent=4)

        print("Done")


if __name__ == "__main__":
    pipeline = Pipeline(Validator())
    pipeline.run()