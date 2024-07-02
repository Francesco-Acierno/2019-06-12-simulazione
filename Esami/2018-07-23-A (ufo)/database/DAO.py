from database.DB_connect import DBConnect
from model.stato import Stato
from model.confinante import Confine


class DAO():
    @staticmethod
    def getAllForme(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select distinct s.shape 
                    from sighting s 
                    where year(s.`datetime`) = %s"""

        cursor.execute(query, (anno,), )

        for row in cursor:
            result.append(row['shape'])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select *
                    from state s """

        cursor.execute(query, )

        for row in cursor:
            result.append(Stato(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPaeseiConfinanti(idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct n.state1,  n.state2 
                       from neighbor n """

        cursor.execute(query, )

        for row in cursor:
            c1 = idMap[row["state1"]]
            c2 = idMap[row["state2"]]

            if c1 is not None and c2 is not None:
                result.append(Confine(c1, c2))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPeso(anno, forma, paese1, paese2):
        conn = DBConnect.get_connection()

        result = 0

        cursor = conn.cursor(dictionary=True)
        query = """select count(*) as peso
                   from sighting s
                   where year (s.`datetime`) = %s
                   and shape = %s
                   and (s.state = %s or s.state = %s)"""

        cursor.execute(query, (anno, forma, paese1, paese2))

        for row in cursor:
            result = row["peso"]

        cursor.close()
        conn.close()
        return result

