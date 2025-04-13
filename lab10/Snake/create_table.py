import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='sampledb',
    user='amirdank',    
    password='financier'
)

current = config.cursor()
sql = '''
        CREATE TABLE users(
            username VARCHAR(100),
            level INT,
            score INT
    );
''' 

current.execute(sql)

current.close()
config.commit()
config.close()