from database.DB_connect import DBConnect
from model.gene import Gene
from model.connessione import Connessione

class DAO():
    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select *
                    from genes g 
                    where g.Essential = 'Essential'
                    group by GeneID """

        cursor.execute(query, )

        for row in cursor:
            result.append(Gene(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessione():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select g1.GeneID as n1, g2.GeneID as n2, i.Expression_Corr as peso, g1.Chromosome as cromosoma1, g2.Chromosome as cromosoma2
from genes g1
join interactions i on g1.GeneID = i.GeneID1 or g1.GeneID = i.GeneID2
join genes g2 on (g2.GeneID = i.GeneID1 or g2.GeneID = i.GeneID2) and g2.GeneID <> g1.GeneID
where g1.Essential = "Essential" and g2.Essential = "Essential"
group by n1, n2, peso, cromosoma1, cromosoma2;"""

        cursor.execute(query, )

        for row in cursor:
            result.append(Connessione(**row))

        cursor.close()
        conn.close()
        return result
