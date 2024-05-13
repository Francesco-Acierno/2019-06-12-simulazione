from database.DB_connect import DBConnect
from model.genere import Genere
from model.traccia import Traccia


class DAO():
    @staticmethod
    def getAllGeneri():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                   from genre g 
                   order by name asc """

        cursor.execute(query, )

        for row in cursor:
            result.append(Genere(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getMinMax(genere):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select min(t.Milliseconds) as min, max(t.Milliseconds) as max
                   from track t 
                   where GenreId = %s"""

        cursor.execute(query, (genere,), )

        for row in cursor:
            result.append((row['min'], row['max']))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllTracce(minG, maxG, genere):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                   from track t
                   where Milliseconds >= %s and Milliseconds <= %s
                   and GenreId = %s"""

        cursor.execute(query, (minG, maxG, genere,), )

        for row in cursor:
            result.append(Traccia(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessioni(genere, minG, maxG):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select t1.ti1 as n1, t2.ti2 as n2
                   from (select count(*) as p1, t.TrackId as ti1
						 from track t, playlisttrack p 
						 where t.TrackId = p.TrackId 
						 and t.GenreId=%s 
						 and t.Milliseconds>=%s
						 and t.Milliseconds<=%s
						 group by t.TrackId) as t1,
						(select count(*) as p2, t.TrackId as ti2
						 from track t, playlisttrack p 
						 where t.TrackId = p.TrackId 
						 and t.GenreId=%s 
						 and t.Milliseconds>=%s
						 and t.Milliseconds<=%s
						 group by t.TrackId) as t2
                   where t1.ti1 <> t2.ti2 and t1.p1=t2.p2"""

        cursor.execute(query, (genere, minG, maxG, genere, minG, maxG), )

        for row in cursor:
            result.append((row["n1"], row["n2"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPlaylist(traccia):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct p.PlaylistId as id
                   from playlisttrack p
                   where p.TrackId = %s"""

        cursor.execute(query, (traccia,), )

        for row in cursor:
            result.append(row['id'])

        cursor.close()
        conn.close()
        return result
