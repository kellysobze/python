import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

df = pd.read_csv('dataset.csv')
pd.options.display.max_columns = 20

missing_value = df.isnull().sum()
features_num = ['track', 'energy', 'tempo', 'valence', 'acousticness']

df = df.sort_values('popularity', ascending=False)
df = df.drop_duplicates(subset=['track_id'], keep='first')

genre_ohe = pd.get_dummies(df['track_genre'], prefix='genre')

x_num = df[features_num]

x = pd.concat([x_num, genre_ohe], axis=1)

scaler = StandardScaler()
x_num_scaled = scaler.fit_transform(x_num)

x_final = np.hstack((x_num_scaled, genre_ohe.values))

similar_track = 10 + 1
model = NearestNeighbors(
    n_neighbors=similar_track,
    metric='euclidean'
)

model.fit(x_final)

print(df['track_genre'].nunique())


def recommend_by_track_id(
        track_id: str,
        k: int = 10,
        same_genre: bool = False
        ) -> pd.DataFrame:
    seed = df[df['track_id'] == track_id]

    if seed.empty:
        raise ValueError("Track ID does not exist")

    seed_row = seed.iloc[0]
    seed_num = seed[features_num]
    seed_num_scaled = scaler.transform(seed_num)

    seed_genre = seed_row['track_genre']
    seed_genre_ohe = pd.zeros(1,genre_ohe.shape[1])
    genre_col_name= f'genre_{seed_genre}'
    if genre_col_name in genre_ohe.colums:
        idx=list(genre_ohe.colums).index(genre_col_name)
        seed_genre_ohe[0,idx]= 1
    seed_vec = np.hstack((seed_num_scaled, seed_genre_ohe))
    distances, indices = model.kneighbors(seed_vec)
    rec=df.iloc[indices[0]].copy()
    recs=recs[rec['track_id']] != track_id
    if same_genre:
        recs=recs[recs['track_id'] == seed_row['track_genre']]
    recs=recs.head(k)
    col=[
        'track_id',
        'track_name',
        'artists',
        'track_genre',
        'popularity',


    ]
    return recs[col]
test_id = ''
print('Traccia seed: \n')
print(df[(df['track_id']==test_id)]['track_id','artista'])

