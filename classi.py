from oggetti import Persona

class Studente(Persona):
    def __init__(self,nome,eta,corso):
        super().__init__(nome,eta)
        self.corso = corso

ciccio = Studente('Ciccio','22','python')

print(ciccio.saluta())
