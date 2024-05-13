from database.DB_connect import DBConnect
from model.team import Team


class DAO():
    @staticmethod
    def getAllTeams():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                   from teams t """

        cursor.execute(query, )

        for row in cursor:
            result.append(Team(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllPunteggi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select distinct t.TeamID as id, (v.vittorie *3 + p.pareggi + vfc.vittoriefuoricasa*3 + pfc.pareggifuoricasa) as punteggio
                    from (select m.TeamHomeID, count(*) as vittorie 
                          from matches m 
                          where ResultOfTeamHome = 1
                          group by m.TeamHomeID) as v,
                         (select m.TeamHomeID, count(*) as pareggi 
                          from matches m 
                          where ResultOfTeamHome = 0
                          group by m.TeamHomeID) as p,
                         (select m.TeamAwayID, count(*) as vittoriefuoricasa
                          from matches m 
                          where ResultOfTeamHome = -1
                          group by m.TeamAwayID) as vfc,
                         (select m.TeamAwayID, count(*) as pareggifuoricasa
                          from matches m 
                          where ResultOfTeamHome = 0
                          group by m.TeamAwayID) as pfc,
                          teams as t
                    where t.TeamID = p.TeamHomeID and t.TeamID = v.TeamHomeID and t.TeamId = vfc.TeamAwayID and t.TeamId = pfc.TeamAwayID"""

        cursor.execute(query, )

        for row in cursor:
            result.append((row["id"], row["punteggio"]))

        cursor.close()
        conn.close()
        return result
