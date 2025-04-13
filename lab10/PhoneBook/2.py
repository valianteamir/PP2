import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='sampledb',
    user='amirdank',    
    password='financier'
)

current = config.cursor()
# добавляем значения в таблицу 
id = 108
name = 'Mama'
number = '748920472074'

sql = '''
    INSERT INTO users VALUES (%s, %s, %s); 
'''

current.execute(sql, (id, name, number))

current.close()
config.commit()
config.close()
