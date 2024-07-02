from database.DB_connect import DBConnect


class DAO():
    @staticmethod
    def getAllNodes(cal):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select  distinct portion_display_name as name
                   from food_pyramid_mod.portion p 
                   where calories < %s"""

        cursor.execute(query, (cal,), )

        for row in cursor:
            result.append(row["name"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessioni(cal):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select p1.portion_display_name as n1, p2.portion_display_name as n2, count(*) as peso
                   from (select *
                         from food_pyramid_mod.portion p 
                         where p.calories < %s) as p1, 
                        (select *
                         from food_pyramid_mod.portion p 
                         where p.calories < %s) as p2
                   where p1.food_code = p2.food_code 
                   and p1.portion_display_name <> p2.portion_display_name
                   and p1.portion_id <> p2.portion_id
                   group by p1.portion_display_name, p2.portion_display_name"""

        cursor.execute(query, (cal, cal))

        for row in cursor:
            result.append((row['n1'], row['n2'], row['peso']))

        cursor.close()
        conn.close()
        return result
