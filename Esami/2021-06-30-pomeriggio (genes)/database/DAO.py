from database.DB_connect import DBConnect


class DAO():
    @staticmethod
    def getAllLocalizzazioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select distinct c.Localization 
                    from classification c """

        cursor.execute(query, )

        for row in cursor:
            result.append(row['Localization'])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessione():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select l1.localization as n1, l2.localization as n2, count(distinct i.type) as peso
                    from classification l1
                    join interactions i on l1.geneid = i.geneid1
                    join classification l2 on l2.geneid = i.geneid2
                    where l1.localization <> l2.localization
                    group by l1.localization, l2.localization"""

        cursor.execute(query, )

        for row in cursor:
            result.append((row['n1'], row['n2'], row['peso']))

        cursor.close()
        conn.close()
        return result

