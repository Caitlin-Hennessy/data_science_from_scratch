import csv

with open('stocks.txt') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        date = row[0]
        symbol = row[1]
        closing_price = float(row[2])
        print date, symbol, closing_price

print '*********************'

with open('dict_stocks.txt') as f:
    reader = csv.DictReader(f, delimiter=':')
    for row in reader:
        date = row['date']
        symbol = row['symbol']
        closing_price = float(row['closing_price'])
        print date, symbol, closing_price