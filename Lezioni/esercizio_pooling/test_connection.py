import mysql.connector
from time import time

N = 10000

# Senza pooling
start_time = time()
for i in range(N):
    cnx = mysql.connector.connect(host="127.0.0.1",
                                  user='root',
                                  password="password",
                                  database='iscritticorsi')
    cursor = cnx.cursor()
    query = """SELECT * FROM corso"""
    cursor.execute(query)
    row = cursor.fetchall()
    cursor.close()
    cnx.close()
end_time = time()
print(f"Elapsed time = {end_time - start_time}")

#Con pooling

start_time = time()
cnx_pool = mysql.connector.pooling.MySQLConnectionPool(host="127.0.0.1",
                                                       user='root',
                                                       password="password",
                                                       database='iscritticorsi',
                                                       pool_size=3,
                                                       pool_name="mypool")
for i in range(N):
    cnx = cnx_pool.get_connection()
    cursor = cnx.cursor()
    query = """SELECT * FROM corso"""
    cursor.execute(query)
    row = cursor.fetchall()
    cursor.close()
    cnx.close()
end_time = time()
print(f"Elapsed time = {end_time - start_time}")
