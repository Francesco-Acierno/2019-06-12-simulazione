from database.DB_connect import DBConnect
from model.utente import Utente


class DAO():
    @staticmethod
    def getAllUtenti(rec):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select u.*
                   from users u 
                   where %s < (select count(*)
                              from reviews r
                              where u.user_id =user_id
                              group by r.user_id)"""

        cursor.execute(query, (rec,))

        for row in cursor:
            result.append(Utente(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessioni(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select u1.id1 as n1, u2.id2 as n2, count(distinct idr1) as peso
                   from (select  distinct u.user_id as id1, r.review_id as idr1, r.business_id as idb1
                         from reviews r, users u 
                         where r.user_id = u.user_id 
                         and YEAR(r.review_date)=%s) as u1, 
                        (select  distinct u.user_id as id2, r.review_id as idr2, r.business_id as idb2
                         from reviews r, users u 
                         where r.user_id = u.user_id and YEAR(r.review_date)=%s) as u2
                   where u1.id1 != u2.id2 and u1.idb1=u2.idb2
                   group by u1.id1, u2.id2"""

        cursor.execute(query, (anno, anno), )

        for row in cursor:
            result.append((row["n1"], row["n2"], row["peso"]))

        cursor.close()
        conn.close()
        return result
