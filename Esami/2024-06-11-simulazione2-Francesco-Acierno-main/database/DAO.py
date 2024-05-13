from database.DB_connect import DBConnect
from model.gene import Gene


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getNodes():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from genes g
                    where g.Chromosome <> 0"""
        cursor.execute(query)
        for row in cursor:
            result.append(Gene(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select t.cromo1, t.cromo2 , t.id1, t.id2, sum(t.correl) as correl
                from (select distinctrow  g.Chromosome as cromo1, g2.Chromosome as cromo2, i.GeneID1 as id1, i.GeneID2 as id2, i.Expression_Corr as correl
                from genes g, interactions i, genes g2 
                where i.GeneID1 = g.GeneID and i.GeneID2 = g2.GeneID and g2.Chromosome <> g.Chromosome
                and g2.Chromosome <> 0 and g.Chromosome <> 0) as t
                group by t.cromo1, t.cromo2"""
        cursor.execute(query)
        for row in cursor:
            result.append((row["cromo1"], row["cromo2"], row["id1"], row["id2"], row["correl"]))
        cursor.close()
        conn.close()
        return result
