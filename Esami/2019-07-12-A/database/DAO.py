from database.DB_connect import DBConnect
from model.food import Food


class DAO():
    @staticmethod
    def getAllNodes(soglia):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select *
                    from food f 
                    where f.food_code in (select food_code 
                                          from food_pyramid_mod.portion p 
                                          where p.portion_id <= %s)"""

        cursor.execute(query, (soglia,), )

        for row in cursor:
            result.append(Food(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select c1.food_code as n1, c2.food_code as n2, avg(c1.calories) as peso
                       from (select fc.food_code, c.condiment_code, p.calories
							 from food_pyramid_mod.condiment c, food_pyramid_mod.food_condiment fc, food_pyramid_mod.portion p
							 where c.condiment_code = fc.condiment_code
							 and p.food_code = fc.food_code) as c1, 
                            (select fc.food_code, c.condiment_code, p.calories
							 from food_pyramid_mod.condiment c, food_pyramid_mod.food_condiment fc, food_pyramid_mod.portion p
							 where c.condiment_code = fc.condiment_code
							 and p.food_code = fc.food_code) as c2
                       where c1.food_code <> c2.food_code and c1.condiment_code = c2. condiment_code
                       group by c1.food_code, c2.food_code"""

        cursor.execute(query, )

        for row in cursor:
            result.append((row["n1"], row["n2"], row["peso"]))

        cursor.close()
        conn.close()
        return result


