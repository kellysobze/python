class Persona:
    def __init__(self,nome,eta):
        self.nome = nome
        self.eta = eta
    def saluta(self):
            print(f'Ciao,mi chiamo{self.nome} e ho {self.eta} anni!')

p1= Persona('Ciccio',26)
p2=Persona('Francesca',23)
p3=Persona('Germania',22)
print(p1.saluta)

class Libro:
    def __init__(self, titolo,genere):
        self.titolo = titolo
        self.genere = genere
l1=Libro('harry potter','fantasy')

