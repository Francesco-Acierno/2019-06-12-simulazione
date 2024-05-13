from database.DB_connect import DBConnect
from model.artista import Artista


class DAO():
    @staticmethod
    def getAllRuoli():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select distinct role
                    from authorship a 
                    order by role asc"""

        cursor.execute(query, )

        for row in cursor:
            result.append(row["role"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodi(ruolo):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select *
                    from artists a 
                    where a.artist_id in (select a.artist_id 
                                          from authorship a  
                                          where a.`role` = %s)"""

        cursor.execute(query, (ruolo, ))

        for row in cursor:
            result.append(Artista(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessioni(ruolo):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select a1.artist_id as n1, a2.artist_id as n2, count(a1.exhibition_id) as peso
                   from (select exhibition_id, eo.object_id, role, artist_id
                         from exhibition_objects eo, authorship a 
                         where eo.object_id = a.object_id
                         and role = %s) as a1, 
                        (select exhibition_id, eo.object_id, role, artist_id
                         from exhibition_objects eo, authorship a 
                         where eo.object_id = a.object_id
                         and role= %s) as a2
                   where a1.exhibition_id = a2.exhibition_id
                   and a1.artist_id <> a2.artist_id
                   group by a1.artist_id, a2.artist_id"""

        cursor.execute(query, (ruolo, ruolo))

        for row in cursor:
            result.append((row['n1'], row['n2'], row['peso']))

        cursor.close()
        conn.close()
        return result

