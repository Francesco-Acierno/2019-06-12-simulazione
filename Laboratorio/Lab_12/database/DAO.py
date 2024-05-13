from database.DB_connect import DBConnect

from Laboratorio.Lab_12.model.retailer import Retailer


class DAO():
    @staticmethod
    def getAllNazioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct gr.Country 
                   from go_sales.go_retailers gr """

        cursor.execute(query)

        for row in cursor:
            result.append(row["Country"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllRetailers(nazione):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                   from go_sales.go_retailers gr 
                   where Country = %s """

        cursor.execute(query, (nazione,))

        for row in cursor:
            result.append(Retailer(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessioni(anno, v0, v1):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select gds.Retailer_code, gds2.Retailer_code, count(distinct(gds.Product_number)) as N
                   from go_daily_sales gds, go_daily_sales gds2
                   where gds.Product_number = gds2.Product_number and year(gds.Date) = year(gds2.Date) 
                   and year(gds2.Date)=%s and gds.Retailer_code = %s and gds2.Retailer_code = %s"""

        cursor.execute(query, (anno, v0.Retailer_code, v1.Retailer_code))

        for row in cursor:
            result = row["N"]

        cursor.close()
        conn.close()
        return result
