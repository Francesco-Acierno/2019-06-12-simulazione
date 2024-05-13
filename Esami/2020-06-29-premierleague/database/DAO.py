from database.DB_connect import DBConnect
from model.match import Match


class DAO():
    @staticmethod
    def getAllMatch(mese):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                   from matches m 
                   where month (m.`Date`) = %s"""

        cursor.execute(query, (mese,), )

        for row in cursor:
            result.append(Match(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessioni(min):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select m1.idm1 as n1, m2.idm2 as n2, count(distinct p1) as peso
                   from (select distinct m.MatchId as idm1, a.PlayerId as p1
                         from premierleague.matches m , actions a 
                         where m.MatchId = a.MatchId and a.TimePlayed > %s) as m1, 
                        (select distinct m.MatchId as idm2, a.PlayerId as p2
                         from premierleague.matches m, actions a 
                         where m.MatchId = a.MatchId and a.TimePlayed > %s) as m2
                   where m1.idm1 <> m2.idm2 and m1.p1 = m2.p2 
                   group by m1.idm1, m2.idm2"""

        cursor.execute(query, (min, min))

        for row in cursor:
            result.append((row['n1'], row['n2'], row['peso']))

        cursor.close()
        conn.close()
        return result
