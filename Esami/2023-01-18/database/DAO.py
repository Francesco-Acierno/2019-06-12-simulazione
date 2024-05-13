from database.DB_connect import DBConnect
from model.connessione import Connessione


class DAO():
    @staticmethod
    def getAllProvider():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct Provider 
                   from nyc_wifi_hotspot_locations nwhl
                   order by Provider ASC """

        cursor.execute(query, )

        for row in cursor:
            result.append(row["Provider"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllLocation(provider):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct  Location 
                   from nyc_wifi_hotspot_locations nwhl 
                   where Provider = %s """

        cursor.execute(query, (provider,), )

        for row in cursor:
            result.append(row["Location"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllGeolocalizzazione(provider):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select loc1.l1 as n1, loc2.l2 as n2, loc1.lat1 as lat1, loc1.long1 as long1, loc2.lat2 as lat2, loc2.long2 as long2
                       from (select distinct location as l1, nwhl.latitude as lat1, nwhl.longitude as long1
                             from nyc_wifi_hotspot_locations nwhl 
                             where nwhl.provider = %s) as loc1, 
                            (select distinct location as l2, nwhl.latitude as lat2, nwhl.longitude as long2
                             from nyc_wifi_hotspot_locations nwhl 
                             where nwhl.provider = %s) as loc2
                       where loc1.l1 != loc2.l2 
                       group by loc1.l1, loc2.l2 """

        cursor.execute(query, (provider, provider), )

        for row in cursor:
            result.append(Connessione(**row))

        cursor.close()
        conn.close()
        return result
