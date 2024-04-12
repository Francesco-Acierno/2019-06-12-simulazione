import mysql.connector
from Lezioni.libretto_voti.modello.voto_dto import VotoDto
from Lezioni.libretto_voti.database.db_connect import DBConnect


class VotiDao:

    def __init__(self):

        self.db_connect = DBConnect()

    def get_voti(self):
        cnx = self.db_connect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * 
                FROM voti"""
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(VotoDto(row["nome"],
                                  row["CFU"],
                                  row["punteggio"],
                                  bool(row["lode"]),
                                  row["data"]))
        cursor.close()
        cnx.close()
        return result

    def add_voti(self, voto: VotoDto) -> None:
        cnx = self.db_connect.get_connection()
        if cnx is None:
            print("Errore")
            return
        cursor = cnx.cursor(dictionary=True)
        query = """
        INSERT INTO voti
        (nome, CFU, punteggio, lode , data) 
        VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(query, (voto.nome,
                               voto.CFU,
                               voto.punteggio,
                               voto.lode,
                               voto.data))
        cnx.commit()
        cursor.close()
        cnx.close()


if __name__ == '__main__':
    voti_dao = VotiDao()
    voti_dao.get_voti()
