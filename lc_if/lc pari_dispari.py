numeri = [5,12,7,20,3,18]
#creare una lista che divida per 2 i numeri >10 lasci invariati gli altri

risultato= [numero/2 if numero>10 else numero for numero in numeri]
print(risultato)