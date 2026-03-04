import ese_csv
with open('dati.csv.py',newline='') as csvfile:
    reader=csv.Dictreader(csvfile)
    writer= csv.writer(csvfile)

    writer.writerow(["nome","eta","citta"])
    writer.writerow(['ciccio','19','ancona'])

