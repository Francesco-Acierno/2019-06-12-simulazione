from database.DB_connect import DBConnect
from model.attore import Attore


class DAO():
    @staticmethod
    def getAllGeneri():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select distinct genre
                    from movies_genres mg 
                    order by genre asc """

        cursor.execute(query, )

        for row in cursor:
            result.append(row["genre"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodi(genere):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select *
                    from actors a 
                    where a.id in (select r.actor_id
                                   from roles r 
                                   where r.movie_id in (select movie_id 
                                                        from movies_genres mg 
                                                        where mg.genre = %s))"""

        cursor.execute(query, (genere,))

        for row in cursor:
            result.append(Attore(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessioni(genere):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select a1.actor_id as n1, a2.actor_id as n2, count(a1.movie_id) as peso
                    from (select r.actor_id, r.movie_id
                          from roles r 
                          where movie_id in (select mg.movie_id
						                      from movies_genres mg  
						                      where mg.genre = %s)) as a1,
                         (select r.actor_id, r.movie_id
                          from roles r 
                          where movie_id in (select mg.movie_id
						                      from movies_genres mg  
						                      where mg.genre = %s)) as a2
                    where a1.actor_id <> a2.actor_id
                    and a1.movie_id = a2.movie_id
                    group by a1.actor_id, a2.actor_id"""

        cursor.execute(query, (genere, genere))

        for row in cursor:
            result.append((row['n1'], row['n2'], row['peso']))

        cursor.close()
        conn.close()
        return result
