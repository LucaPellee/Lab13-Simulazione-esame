import copy

from database.DAO import DAO
import networkx as nx
from geopy import distance
class Model:
    def __init__(self):
        self.listStates = DAO.getStates()
        self.mapStates = {}
        for s in self.listStates:
            self.mapStates[s.id] = s
        self.grafo = nx.Graph()
        self.bestPath = []
        self.bestDist = 0

    def getAnni(self):
        return DAO.getYears()

    def getShape(self, anno):
        return DAO.getShapes(anno)

    def creaGrafo(self, anno, shape):
        self.grafo.clear()
        for n in self.listStates:
            self.grafo.add_node(n)
        listaTuple = DAO.getArchiPesati(anno, shape, self.mapStates)
        for t in listaTuple:
            self.grafo.add_edge(t[0], t[1], weight=t[2])

    def calcolaSommaArchi(self):
        listaTuple = []
        for n in self.listStates:
            peso = 0
            vicini = []
            vicini = list(self.grafo.neighbors(n))
            for v in vicini:
                peso += self.grafo[n][v]['weight']
            listaTuple.append((n, peso))
        return listaTuple

    def getPath(self):
        nodi = self.listStates
        #parziale = []
        self.bestPath = []
        self.bestDist = 0
        for n in nodi:
            parziale = []
            parziale.append(n)
            self.ricorsione(parziale)
            #parziale.pop()
        return self.bestPath, self.bestDist

    def ricorsione(self, parziale):
        vicini = list(self.grafo.neighbors(parziale[-1]))
        if (len(vicini) == 1 and len(parziale) > 1) or (len(vicini) == 0):
            if self.getDist(parziale) > self.bestDist:
                self.bestDist = self.getDist(parziale)
                self.bestPath = copy.deepcopy(parziale)
            return
        else:
            for v in vicini:
                if len(parziale) == 1 or (self.grafo[parziale[-1]][v]['weight'] > self.grafo[parziale[-2]][parziale[-1]]['weight']):
                    parziale.append(v)
                    self.ricorsione(parziale)
                    parziale.pop()


    def getDist(self, parziale):
        somma = 0
        for i in range(len(parziale)-1):
            v0 = parziale[i]
            v1 = parziale[i + 1]
            v0tup = (v0.Lat, v0.Lng)
            v1tup = (v1.Lat, v1.Lng)
            somma += distance.distance(v0tup, v1tup).km
        return somma


    def getNumNodes(self):
        return len(self.grafo.nodes())

    def getNumEdges(self):
        return len(self.grafo.edges())