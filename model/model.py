import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._idMap = {}

    def buildGraph(self,d):
        self._graph.clear()
        self._graph.add_nodes_from(DAO.getAlbums(d))
        self._idMap = {a.AlbumId: a for a in list(self._graph.nodes)}
        edges = DAO.getEdges(self._idMap)
        self._graph.add_edges_from(edges)

    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getNodes(self):
        return list(self._graph.nodes)


def toMillsec(d):
    return d*60*1000
