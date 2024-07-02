import _mysql_connector
from database.DB_connect import DBConnect
from model.corso import Corso


class CorsoDao:

    @staticmethod
    def get_corsi_periodo(pd):
        cnx = DBConnect.get_connection()
        result =[]
        if cnx is None:
            print("errore connessione")
            return result
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT c.*
                    FROM corso c
                    WHERE c.pd = %s"""
            cursor.execute(query, (pd,))
            for row in cursor:
                result.append(Corso(row["codins"],
                                    row["crediti"],
                                    row["nome"],
                                    row["pd"]))
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def get_studenti_periodo(pd):
        cnx = DBConnect.get_connection()

        if cnx is None:
            print("errore connessione")
            return []
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT i.matricola
                FROM corso c, iscrizione i 
                WHERE c.pd = %s AND c.codins = i.codins """
            cursor.execute(query, (pd,))
            rows = cursor.fetchall()
            cursor.close()
            cnx.close()
            return rows

    @staticmethod
    def get_all_corsi():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("errore connessione")
            return result
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT c.*
                        FROM corso c"""
            cursor.execute(query)
            for row in cursor:
                result.append(Corso(row["codins"],
                                    row["crediti"],
                                    row["nome"],
                                    row["pd"]))
            cursor.close()
            cnx.close()
            return result


    @staticmethod
    def get_studenti_singolo_corso(codins):
        cnx = DBConnect.get_connection()
        result = set()
        if cnx is None:
            print("errore connessione")
            return result
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT i.matricola
                FROM iscrizione i 
                WHERE i.codins = %s"""
            cursor.execute(query, (codins,))
            for row in cursor:
                result.add(row["matricola"])
            cursor.close()
            cnx.close()
            return result