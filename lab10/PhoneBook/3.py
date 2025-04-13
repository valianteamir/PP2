import csv, psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='sampledb',
    user='amirdank',    
    password='financier'
)
current = config.cursor()
arr = []
# вставляем данные в телефонную книгу загружая их из csv-файла
with open('/Users/amirdank/Desktop/PP2/lab10/PhoneBook/1.csv') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        row[0] = int(row[0])
        arr.append(row)

sql = '''
    INSERT INTO phonebook VALUES (%s, %s, %s) RETURNING *; 
'''

for row in arr:
    current.execute(sql, row)

final = current.fetchall()
print(final)

current.close()
config.commit()
config.close()
