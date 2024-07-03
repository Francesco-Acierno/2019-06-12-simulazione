from database.DB_connect import DBConnect
from model.traccia import Traccia


class DAO():
    @staticmethod
    def getAllGeneri():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select distinct g.Name 
                    from genre g 
                    order by g.Name asc"""

        cursor.execute(query, )

        for row in cursor:
            result.append(row['Name'])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodi(genere):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select *
                    from genre g, track t 
                    where g.Name = %s
                    and g.GenreId = t.GenreId """

        cursor.execute(query, (genere,), )

        for row in cursor:
            result.append(Traccia(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessioni(genere):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select c1.TrackId as n1, c2.trackId as n2, abs(c1.Milliseconds-c2.Milliseconds) as peso
                   from (select t.TrackId, t.Milliseconds, t.MediaTypeId
                         from track t, genre g 
                         where t.genreId = g.genreId
                         and g.Name = %s) as c1,
                        (select t.TrackId, t.Milliseconds, t.MediaTypeId
                         from track t, genre g 
                         where t.genreId = g.genreId
                         and g.Name = %s) as c2
                   where c1.TrackId<>c2.trackId and c1.MediaTypeId = c2.MediaTypeId
                   group by c1.TrackId,c2.trackId"""

        cursor.execute(query, (genere, genere,), )

        for row in cursor:
            result.append((row["n1"], row["n2"], row["peso"]))

        cursor.close()
        conn.close()
        return result


