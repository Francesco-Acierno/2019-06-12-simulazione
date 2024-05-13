from database.DB_connect import DBConnect
from model.film import Film


class DAO():
    @staticmethod
    def getAllFilm():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select * 
                   from movies m 
                   where m.`rank` is not null """

        cursor.execute(query,)

        for row in cursor:
            result.append(Film(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPeso(rank):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select t1.m1 as n1, t2.m2 as n2, count(distinct ida1) as peso
                   from (select  distinct m.id as m1, r.actor_id as ida1
                         from movies m, roles r
                         where m.`rank` >= %s and r.movie_id = m.id) as t1, 
                        (select distinct m.id as m2, r.actor_id as ida2
                         from movies m, roles r
                         where m.`rank` >= %s and r.movie_id = m.id) as t2
                   where t1.m1 != t2.m2 and ida1 = ida2
                   group by t1.m1, t2.m2"""

        cursor.execute(query, (rank, rank))

        for row in cursor:
            result.append((row['n1'], row['n2'], row['peso']))

        cursor.close()
        conn.close()
        return result
