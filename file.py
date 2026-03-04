with open('dati.py','r') as f:
      nome = f.readlines()
nomi_puliti=[]
for n in nome:
    nome = n.strip()
    nome=nome.title()
    nome = nome.replace('\n','')
nomi_puliti.append(nome)
print(nomi_puliti)