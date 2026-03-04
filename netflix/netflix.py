#trasfromare le righe in features numeriche con un metodo che conta le parole:
#es: 'il gatto è sul tavolo' e 'il treno è sul binario'
#do un punteggio in base al numero di volte che comprare una parola -> SE LA PAROLA è PIU RARA VALE DI PIù
#embeddings = modello che trasforma i testi in vettori semantici
# creare una colonna con: director+cost+genere+description
# utilizzare SOUP e TF IDF per creare un modello di predizione per aumentare l'accuratezza dei risultati

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors


#CREAZIONE SOUP
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

# =========================
# 1️⃣ CARICAMENTO DATI
# =========================
df = pd.read_csv(r"C:\Users\Administrator\Desktop\NetFlix.csv")
pd.options.display.max_columns = 20

# Controllo colonne e prime righe
#print(df.columns)
#print(df.head())

# =========================
# 2️⃣ CREAZIONE DELLA COLONNA 'SOUP'
# =========================
df['soup'] = (
        df['director'].fillna('') + ' ' +
        df['cast'].fillna('') + ' ' +
        df['genres'].fillna('') + ' ' +
        df['description'].fillna('')
)

# =========================
# 3️⃣ TF-IDF
# =========================
tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
x_text = tfidf.fit_transform(df['soup'])

# =========================
# 4️⃣ MODELLO NEAREST NEIGHBORS
# =========================
similar_items = 10 + 1  # +1 perché il primo sarà il film stesso
model = NearestNeighbors(n_neighbors=similar_items, metric='cosine')
model.fit(x_text)




# =========================
# 5️⃣ FUNZIONE DI RACCOMANDAZIONE
# =========================
def recommend_by_show_id(show_id: str, k: int = 10) -> pd.DataFrame:
 """
 Restituisce i k contenuti più simili a quello dato dal show_id.
 """
 seed = df[df['show_id'] == show_id]
 if seed.empty:
  raise ValueError(f"Show ID '{show_id}' non trovato.")

 idx = seed.index[0]

 distances, indices = model.kneighbors(x_text[idx], n_neighbors=k + 1)

 # Escludo il primo risultato (è se stesso)
 rec_indices = indices.flatten()[1:]

 return df.iloc[rec_indices][['show_id', 'type', 'title', 'director', 'genres']]


# =========================
# 6️⃣ ESEMPIO DI UTILIZZO
# =========================
example_id = 's5754'  # sostituisci con qualsiasi show_id del tuo dataset
recommendations = recommend_by_show_id(example_id, k=5)
print(recommendations)
