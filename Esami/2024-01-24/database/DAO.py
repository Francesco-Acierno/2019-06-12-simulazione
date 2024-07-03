from database.DB_connect import DBConnect
from model.metodo import Metodo
from model.prodotto import Prodotto

class DAO():
    @staticmethod
    def getAllMetodi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select *
                    from go_methods gm  """

        cursor.execute(query, )

        for row in cursor:
            result.append(Metodo(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodi(anno, metodo):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select gp.*, sum(gds.quantity*gds.unit_sale_price) as ricavo
                    from go_daily_sales gds, go_products gp, go_methods gm 
                    where gp.Product_number = gds.Product_number and year(gds.`Date`) = %s
                    and gm.Order_method_code = gds.Order_method_code and gm.Order_method_code = %s 
                    group by gp.Product_number"""

        cursor.execute(query, (anno, metodo,),)

        for row in cursor:
            result.append(Prodotto(**row))

        cursor.close()
        conn.close()
        return result







