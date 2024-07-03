from database.DB_connect import DBConnect
from model.business import Business


class DAO():
    @staticmethod
    def getAllCitta():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select distinct b.city 
                    from business b 
                    order by b.city asc """

        cursor.execute(query, )

        for row in cursor:
            result.append(row['city'])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodes(citta, anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select *
                    from business b 
                    where b.city=%s
                    and b.business_id in (select r.business_id
                                            from reviews r
                                            where year(r.review_date)=%s) """

        cursor.execute(query, (citta, anno), )

        for row in cursor:
            result.append(Business(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessioni(citta, anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select b1.business_id as n1, b2.business_id as n2, (b1.media-b2.media) as peso
                   from (select b.business_id, avg(r.stars) media
                         from business b, reviews r 
                         where b.business_id = r.business_id
                         and b.city = %s and year(r.review_date) = %s
                         group by b.business_id) as b1,
                        (select b.business_id, avg(r.stars) media
                         from business b, reviews r 
                         where b.business_id = r.business_id
                         and b.city = %s and year(r.review_date) = %s
                         group by b.business_id) as b2
                   where b1.business_id != b2.business_id and b1.business_id< b2.business_id
                   group by b1.business_id, b2.business_id"""

        cursor.execute(query, (citta, anno, citta, anno), )

        for row in cursor:
            result.append((row["n1"], row["n2"], row["peso"]))

        cursor.close()
        conn.close()
        return result


