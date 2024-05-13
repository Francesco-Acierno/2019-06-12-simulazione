import mysql.connector

try:
    cnx = mysql.connector.connect(user='root', password='password', host='127.0.1', database='test')

    print(type(cnx))
    cursor = cnx.cursor(dictionary=True)
    querys = """INSERT into users
                (id, nome)
                VALUES(%s, %s)
            """
    cursor.execute(querys, (5,"Carlo"))
    # rows = cursor.fetchall()
    # for row in rows:
    # print(row["nome"]
    cursor.close()
    cnx.close()
except mysql.connector.Error as err:
    print(err)


