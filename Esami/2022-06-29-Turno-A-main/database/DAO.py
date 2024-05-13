from database.DB_connect import DBConnect
from model.album import Album


class DAO():

    @staticmethod
    def getAllNodi(n):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select a.AlbumId, count(t.TrackId) as numeroTracce, a.Title 
                   from itunes.track t
                   join itunes.album a on a.AlbumId = t.AlbumId 
                   group by t.AlbumId 
                   having numeroTracce>%s
                   order by a.Title asc"""

        cursor.execute(query, (n,))

        for row in cursor:
            result.append(Album(**row))

        cursor.close()
        conn.close()
        return result

