from database.DB_connect import DBConnect
from model.ingrediente import  Ingrediente


class DAO():
    @staticmethod
    def getAllIngredienti(cal):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                   from condiment c
                   where c.condiment_calories < %s
                   order by c.condiment_calories desc"""

        cursor.execute(query, (cal,))

        for row in cursor:
            result.append(Ingrediente(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select i1.id1 as n1, i2.id2 as n2, count(distinct f1) as peso
                       from (select  distinct c.condiment_code as id1, fc.food_code as f1
                             from condiment c, food_condiment fc 
                             where c.condiment_code = fc.condiment_code) as i1, 
                            (select  distinct c.condiment_code as id2, fc.food_code as f2
                             from condiment c, food_condiment fc 
                             where c.condiment_code = fc.condiment_code) as i2
                       where i1.id1 != i2.id2 and i1.f1=i2.f2
                       group by i1.id1, i2.id2"""

        cursor.execute(query, )

        for row in cursor:
            result.append((row["n1"], row["n2"], row["peso"]))

        cursor.close()
        conn.close()
        return result

