from database.DB_connect import DBConnect


class DAO():
    @staticmethod
    def getAllSquadre():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select distinct name 
                    from teams t 
                    order by name asc """

        cursor.execute(query, )

        for row in cursor:
            result.append(row["name"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodi(squadra):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select year
                    from teams t 
                    where name=%s"""

        cursor.execute(query, (squadra,), )

        for row in cursor:
            result.append(row["year"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessioni(squadra):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT 
    a1.year AS y1, 
    a2.year AS y2, 
    COUNT(a1.playerId) AS peso
FROM 
    (
        SELECT t.year, a.playerId
        FROM teams t, appearances a
        WHERE t.name = %s and a.teamCode = t.teamCode
        GROUP BY t.year, a.playerId
    ) AS a1,
    (
        SELECT t.year, a.playerId
        FROM teams t, appearances a
        WHERE t.name = %s and a.teamCode = t.teamCode
        GROUP BY t.year, a.playerId
    ) AS a2
where 
    a1.playerId = a2.playerId AND a1.year <> a2.year
GROUP BY 
    a1.year, a2.year
ORDER BY 
    a1.year, a2.year;"""

        cursor.execute(query, (squadra, squadra), )

        for row in cursor:
            result.append((row["y1"], row["y2"], row["peso"]))

        cursor.close()
        conn.close()
        return result
