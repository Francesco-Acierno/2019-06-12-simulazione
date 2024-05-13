from database.DB_connect import DBConnect
from model.giocatore import Giocatore


class DAO():
    @staticmethod
    def getAllNodes(media):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select p.PlayerID, p.Name, sum(a.goals) as gol, count(MatchID) as partite 
                    from players p, actions a
                    where p.PlayerID = a.PlayerID 
                    group by p.PlayerID
                    having (gol/partite) > %s"""

        cursor.execute(query, (media,), )

        for row in cursor:
            result.append(Giocatore(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select g1.PlayerID as n1, g2.PlayerID as n2, ((sum(g1.TimePlayed))-(sum(g2.TimePlayed))) as peso
                   from (select p.PlayerID, m.MatchID, a.TimePlayed, a.TeamID
                         from players p, actions a, matches m 
                         where p.PlayerID = a.PlayerID and a.starts>= 1 and m.MatchID = a.MatchID) as g1, 
                        (select p.PlayerID, m.MatchID, a.TimePlayed, a.TeamID
                         from players p, actions a, matches m 
                         where p.PlayerID = a.PlayerID and a.starts>= 1 and m.MatchID = a.MatchID) as g2
                   where g1.PlayerID <> g2.PlayerID and g1.MatchID = g2.MatchID and g1.TeamID<>g2.TeamID
                   group by g1.PlayerID, g2.PlayerID"""

        cursor.execute(query, )

        for row in cursor:
            result.append((row['n1'], row['n2'], row['peso']))

        cursor.close()
        conn.close()
        return result
