import pandas as pd
dati = {
    'settore':['tech','retail','finance','technology','tech','retail','finance'],
    'dipendenti':[50,70,30,90,80,75,20],
    'fatturato':[5000,6000,33000,12000,9000,85000,18000]
    }

df=pd.DataFrame(dati)
#fatturato medio per settore,
# numero totale di dipendenti per settore,
# settore con massimo fatturato totale

print(df.groupby('settore')['fatturato'].mean())
totali = (df.groupby('settore')['dipendenti'].sum())
print(totali.idxmax())

