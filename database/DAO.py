from database.DB_connect import DBConnect
from model.state import State

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getYears():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor()
        query = """select distinct(year(s.datetime)) from sighting s order by year(s.datetime)"""
        cursor.execute(query)

        for row in cursor:
            result.append(row[0])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getShapes():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor()
        query = """select distinct(s.shape) from sighting s"""
        cursor.execute(query)

        for row in cursor:
            result.append(row[0])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getStates():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary = True)
        query = """select * from state s """
        cursor.execute(query)

        for row in cursor:
            result.append(State(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchiPesati(anno, shape):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select n.state1, n.state2, count(*) as peso
from neighbor n, sighting s 
where s.shape = "circle" and year(s.`datetime`) = 2010
and (s.state = n.state1 or s.state = n.state2)
and n.state1 < n.state2 
group by n.state1, n.state2"""
        cursor.execute(query)

        for row in cursor:
            result.append()

        cursor.close()
        conn.close()
        return result
