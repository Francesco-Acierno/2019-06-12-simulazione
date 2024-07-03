from database.DB_connect import DBConnect
from model.anno import Anno
from model.stato import Stato


class DAO():
    @staticmethod
    def getAllAnni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select year(s.`datetime`) as anno, count(*) as avvistamenti
                    from sighting s 
                    group by year(s.`datetime`) """

        cursor.execute(query, )

        for row in cursor:
            result.append(Anno(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllStati(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select *
                    from state s
                    where id in (select state
                                from sighting s2
                                where year(s2.`datetime`)=%s) """

        cursor.execute(query, (anno,), )

        for row in cursor:
            result.append(Stato(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessioni(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select s.state as stato1, s2.state as stato2
                    from sighting s, sighting s2 
                    where s.state <> s2.state 
                    and year(s.datetime) = %s
                    and year(s2.datetime) = %s
                    and s.datetime > s2.datetime"""

        cursor.execute(query, (anno, anno), )

        for row in cursor:
            result.append((row["stato1"], row["stato2"]))

        cursor.close()
        conn.close()
        return result
