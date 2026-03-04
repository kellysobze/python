import ese_csv
with open('dc_prodotti.py') as csvfile:
    reader = csv.reader(csvfile,newline ='')
    for row in reader:
        print(row)
        