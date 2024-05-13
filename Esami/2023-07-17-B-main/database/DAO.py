from database.DB_connect import DBConnect
from model.prodotto import Prodotto


class DAO():
    @staticmethod
    def getAllBrand():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct Product_brand 
                   from go_products gp """

        cursor.execute(query, )

        for row in cursor:
            result.append(row['Product_brand'])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodi(brand):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct *
                   from go_products gp 
                   where Product_brand = %s"""

        cursor.execute(query, (brand,), )

        for row in cursor:
            result.append(Prodotto(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessioni(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select p1.pc1 as n1, p2.pc2 as n2, count(distinct r1) as peso
                   from (select distinct gp.Product_number as pc1, gds.Retailer_code as r1, gds.date d1
                         from go_products gp, go_daily_sales gds 
                         where gp.Product_number=gds.Product_number and year(gds.date) = %s) as p1, 
                        (select distinct gp.Product_number as pc2, gds.Retailer_code as r2, gds.date d2
                         from go_products gp, go_daily_sales gds 
                         where gp.Product_number=gds.Product_number and year(gds.date) = %s) as p2
                   where p1.pc1 <> p2.pc2 and p1.r1 = p2.r2 and d1 = d2  
                   group by p1.pc1, p2.pc2"""

        cursor.execute(query, (anno, anno,), )

        for row in cursor:
            result.append((row['n1'], row['n2'], row['peso']))

        cursor.close()
        conn.close()
        return result


