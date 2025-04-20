import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(host="localhost", dbname="sampledb", user="amirdank", password="financier", port=5432)

# Define a function to return all records based on a pattern
# def search_records(pattern):
#     with conn.cursor() as cur:
#         cur.execute("SELECT * FROM phonebook WHERE name LIKE %s OR number LIKE %s", (f'%{pattern}%', f'%{pattern}%'))
#         return cur.fetchall()

# # Define a procedure to insert or update a user by name and number
# def insert_or_update_user(name, number):
#     with conn.cursor() as cur:
#         cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
#         if cur.rowcount == 0:
#             cur.execute("INSERT INTO phonebook (name, number) VALUES (%s, %s)", (name, number))
#         else:
#             cur.execute("UPDATE phonebook SET number = %s WHERE name = %s", (number, name))
#         conn.commit()
# # Define a procedure to insert many new users by list of name and number
# def insert_users(users):
#     with conn.cursor() as cur:
#         for user in users:
#             name, number = user
#             cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
#             if cur.rowcount == 0:
#                 cur.execute("INSERT INTO phonebook (name, number) VALUES (%s, %s)", (name, number))
#             else:
#                 cur.execute("UPDATE phonebook SET number = %s WHERE name = %s", (number, name))
#         conn.commit()

# Define a function to query data from the tables with pagination
# def query_data(limit, offset):
#     with conn.cursor() as cur:
#         cur.execute("SELECT * FROM phonebook ORDER BY name LIMIT %s OFFSET %s", (limit, offset))
#         return cur.fetchall()


# user_list = [("Hfhla", "8998"), ("Kyfjafaran", "9875"), ("fa", "75555")]
# insert_users(user_list)

# Close the database connection when finished

# print(query_data(10,2))
conn.close()