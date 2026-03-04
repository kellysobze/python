def somma(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError('Somma non possibile')
    return a+b

def sottrazione(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError('Sottrazie non possibile')
    return a-b

def moltiplicazioni(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError('Moltiplicazioni non possibile')

    return a*b

def divisione(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError('Divisione non possibile')
    if b==0:
        raise ZeroDivisionError ('il divisore non può essere zero')
    return a/b
