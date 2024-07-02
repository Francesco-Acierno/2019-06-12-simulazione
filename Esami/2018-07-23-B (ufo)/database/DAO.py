from database.DB_connect import DBConnect
from model.stato import Stato
from model.confinante import Confine

class DAO():
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
    def getPeso(diffGiorni, anno, paese1, paese2):
        conn = DBConnect.get_connection()

        result = 0

        cursor = conn.cursor(dictionary=True)
        query = """ select count(*) as peso
                    from sighting s1, sighting s2
                    where DATEDIFF(s1.`datetime`, s2.`datetime`)=%s
                    and year(s1.`datetime`)=%s and year(s2.`datetime`)=%s
                    and (s1.state = %s or s1.state=%s) and (s2.state=%s or s2.state=%s)"""

        cursor.execute(query, (diffGiorni, anno, anno, paese1, paese1, paese2, paese2))

        for row in cursor:
            result = row["peso"]

        cursor.close()
        conn.close()
        return result


