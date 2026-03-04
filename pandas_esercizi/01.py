import pandas as pd
dati = {
    'nome': ['Ciccio', 'Anna','Marcello','Francesca','PAOLO'],
    'email': ['ciccio@email.it','anna@email.com','marcello@email.com','francsca@email.com','None'],
    'eta': [None,22,38,None,21],
    'stipendio': [1200,1800,None,2100,None],
    'citta':['Roma','Milano','Firenze','Roma','Roma'],
    'categoria':['A','A','B''A','B'],
    'vendita':[100,300,400,500,None,None]}

df = pd.DataFrame(dati)

# sostituire i dati di eta mancanti con un valore standard
media_eta = df['eta'].mean()
df['eta'] = df['eta'].fillna(media_eta)

# pulizia dei dati
df['nome'] = df['nome'].str.strip().str.title()
df['email'] = df['email'].str.strip().str.lower()

df['stipendio'] = df['stipendio'].fillna(df['stipendio'].mean())

df = df.dropna(subset=['email'])

df['eta'] = pd.to_numeric(df['eta'], errors='coerce')
df['eta'] = df['eta'].fillna(df['eta'].mean())
df['eta'] = df['eta'].astype(int)

print(df.groupby('categoria')['vendita'].sum().mean())
print(df)