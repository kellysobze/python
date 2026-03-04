import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
df = pd.read_csv('Titanic_Dataset.csv')
#per vedere le prime 5 righe
# print(df.head())
#per vedere le statistiche generali
# print(df.describe())
#conteggio dei sopravissuti
# survied = df['Survived'].value_counts()
# print(survied)
# survied_by_sex = df.groupby('Sex')['Survived'].mean()
# avg_age_survived=df[df['Survived'] == 1]['Age'].mean()
#prezzo medio per classe
# print(df.groupby('Pcclass')['Fare'].max())

#pulizia dei dati

df=df.drop(['Passenger ID''Name', 'Cabin','Ticket'], axis=1) #elimina queste  le colonne
#riempire la colonna dell'eta con i valori medi
df['Age']=df['Age'].fillna(df['Age'].median())
df['Embarked']=df['Embarked'].fillna(df['Embarked'].mode()[0])
df['Family_size']=df['SibSp']+df['Parch'] +1
df['IsMaleChild']=0
df.loc[df.['Nome'].str.contains('Master'), 'IsMaleChild'] = 1
df['Isalone']=0
df['Age0015']=0
df['Age0040']=0
df['Age0080']=0
df.loc[(df['Age'] > 0) & (df['Age'] <= 15), 'Age0015'] = 1
df.loc[(df['Age'] > 15) & (df['Age'] <= 40), 'Age1540'] = 1
df.loc[(df['Age'] > 40), 'Age4080'] = 1
df.drop(['Age'],axis=1)
df.loc[df['FamilySize']==1, 'IsAlone'] = 1 #locpermette di assegnare dei valori condizionali
df=pd.get_dummies(df, columns=['Sex','Embarked'],drop_first=True)


x=df.drop(['Survived'], axis=1)
y=df['Survived']
x_train, x_test, y_train, t_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)
model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)
accuracy= accuracy_score(y_test,y_pred)
cm = confusion_matrix(y_test,y_pred) #matrice che indica i TN(veri negativi), FP(falsi positivi),FN,TP
print(accuracy) #mostra quanto il training si sia avvicinato al test
for feature, coef in zip(x_test, model.coef_): #calcola i pesi
    print(feature, coef)

jack={
    'Plass':3
    'IsMaleChild':0,
    'Age':20
    'family_size':0
    'Isalone':1
    'Sex_male':1,
    'Age0015':0,
    'Age1540':1,
    'Age4080':0,
    'Embarked_Q':1,
    'Embarked_S':1,

}

rose={'Plass':0,
    'IsMaleChild':0,
      'family_size':2,
      'Isalone':0,
      'Sex_male':0,
      'Age0015':0,
      'Age1540':1,
      'Age4080':0,
      'Embarked_Q':0,
      'Embarked_S':1,

}

char_titanic_movie=pd.Dataframe([jack,rose],index=['Jack','Rose'])
char_titanic_movie=char_titanic_movie.re)

survived_vy_sex= df.groupby('Sex')['Survived'].mean()
plt.figure()
plt.bar(['Femminucce','Maschietti'],s)




