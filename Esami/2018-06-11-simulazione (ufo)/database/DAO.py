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
        query = """select s1.id as n1, s2.id as n2, datediff(s2.data, s1.data) as peso
                   from (select  st.id, max(s.datetime) as data
                         from state st, sighting s 
                         where st.id = s.state
                         and year(s.datetime) = %s
                         group by st.id) as s1,
                        (select  st.id, max(s.datetime) as data
                         from state st, sighting s 
                         where st.id = s.state
                         and year(s.datetime) = %s
                         group by st.id) as s2
                   where s1.id < s2.id 
                   group by s1.id, s2.id"""

        cursor.execute(query, (anno, anno), )

        for row in cursor:
            result.append((row["n1"], row["n2"], row["peso"]))

        cursor.close()
        conn.close()
        return result
