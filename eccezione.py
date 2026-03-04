try:
    numero_1=int(input("Inserire un numero: "))
    numero_2=int(input("Inserire un numero: "))
    print('Risultato:',numero_1/numero_2)
except ValueError:
    print('Inserire un numero valido')
except ZeroDivisionError:
    print('Non puoi diveidere per zero')
else:
    print('Divisione eseguita con successo')
finally:
    print('Qualsiasi cosa succeda io vengo eseguito')
