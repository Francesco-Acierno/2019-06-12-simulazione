from Laboratorio.Lab_09.database.DB_connect import DBConnect
from Laboratorio.Lab_09.model.airport import Airport
from Laboratorio.Lab_09.model.flight import Flight
from Laboratorio.Lab_09.model.airline import Airline
from Laboratorio.Lab_09.model.rotta import Rotta


class DAO:

    @staticmethod
    def getAllAirports():

        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select * from airports a"""

        cursor.execute(query)

        for row in cursor:
            result.append(Airport(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllFlights():

        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select * from flights"""

        cursor.execute(query)

        for row in cursor:
            result.append(Flight(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllAirline():

        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select * from airlines"""

        cursor.execute(query)

        for row in cursor:
            result.append(Airline(**row))

        cursor.close()
        conn.close()
        return result

    # Questo metodo legge le rotte dal db, senza aggregare i voli opposti sulla stessa tratta.
    # La query è molto semplice. La Lista risultante quindi avrà una entry per i voli A->B, e un'altra
    # entry per i voli B->A
    @staticmethod
    def getAllRotteV1():

        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT f.ORIGIN_AIRPORT_ID as a1, f.DESTINATION_AIRPORT_ID as a2, SUM(f.DISTANCE) as totDistance, COUNT(*) as nVoli 
                    FROM flights f 
                    GROUP BY f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID"""

        cursor.execute(query)

        for row in cursor:
            result.append(Rotta(**row))

        cursor.close()
        conn.close()
        return result

    # Questo metodo legge le rotte dal db, aggregando già nella query i voli opposti sulla stessa tratta. Per fare
    # questo, la query è abbastanza complicata, e sfrutta una join di due tabelle temporanee (una il flip
    # dell'altra). Visto che alcune rotte non hanno voli in entrambe le direzioni, si fanno dei check sui NULL (che
    # non vanno esclusi). COALESCE permette nella sommatoria di considerare i NULL come zero.
    @staticmethod
    def getAllRotteV2():

        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT T1.ORIGIN_AIRPORT_ID as a1, T1.DESTINATION_AIRPORT_ID as a2, COALESCE(T1.D, 0) + COALESCE(T2.D, 0) as totDistance, COALESCE(T1.N, 0) + COALESCE(T2.N, 0) as nVoli
                    FROM
                    (SELECT f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID, SUM(f.DISTANCE) as D, COUNT(*) as N
                    FROM flights f
                    GROUP BY f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) T1
                    LEFT JOIN
                    (SELECT f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID, SUM(f.DISTANCE) as D, COUNT(*) as N
                    FROM flights f
                    GROUP BY f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) T2
                    ON T1.ORIGIN_AIRPORT_ID = T2.DESTINATION_AIRPORT_ID AND T2.ORIGIN_AIRPORT_ID = T1.DESTINATION_AIRPORT_ID
                    WHERE T1.ORIGIN_AIRPORT_ID < T2.ORIGIN_AIRPORT_ID OR T2.ORIGIN_AIRPORT_ID IS NULL OR T2.DESTINATION_AIRPORT_ID IS NULL"""

        cursor.execute(query)

        for row in cursor:
            result.append(Rotta(**row))

        cursor.close()
        conn.close()
        return result
