from database.DAO import DAO
import networkx as nx
class Model:
    def __init__(self):
        self.listYears = DAO.getYears()
        self.listShapes = DAO.getShapes()
        self.listStates = DAO.getStates()
        self.mapStates = {}
        for s in self.listStates:
            self.mapStates[s.id] = s
        self.grafo = nx.Graph()

    def creaGrafo(self, anno, shape):
        self.grafo.clear()
        self.grafo.add_nodes_from(self.listStates)
        DAO.getArchiPesati(anno, shape)

    def getNumNodes(self):
        return len(self.grafo.nodes())

    def getNumEdges(self):
        return len(self.grafo.edges())