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
    def getShapes(anno):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor()
        query = """select distinct s.shape from sighting s where s.shape != "" and year(s.`datetime`) = %s order by s.shape"""
        cursor.execute(query, (anno,))

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
        query = """select * from state s order by s.id"""
        cursor.execute(query)

        for row in cursor:
            result.append(State(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchiPesati(anno, shape, map):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select n.state1, n.state2, count(*) as peso from sighting s, neighbor n where s.shape = %s 
        and year(s.datetime) = %s and n.state1 < n.state2 and (s.state = n.state1 or s.state = n.state2) group by n.state1, n.state2"""
        cursor.execute(query, (shape, anno,))

        for row in cursor:
            result.append((map[row['state1']], map[row['state2']], row['peso']))

        cursor.close()
        conn.close()
        return result
