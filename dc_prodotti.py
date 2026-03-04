prodotti=[
    {'id':1.,'nome':'pc','prezzo':999.},
    {'id':2,'nome':'Monitor','prezzo':699.00},
    {'id:'3,'nome':'Mouse','prezzo':None},
    {'id':4,'nome':'Tastiera','prezzo':129.00},
]

import ese_csv

with open('dc_prodotti.py') as csvfile:
    reader = csv.reader(csvfile, newline='')
    for row in reader:
        print(row)
