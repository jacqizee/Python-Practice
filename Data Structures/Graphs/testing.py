from graph import Graph
from vertex import Vertex
import unittest

class TestGraph(unittest.TestCase):
    def setUp(self) -> None:
        self.mta_stations = Graph()
    
    def test_graph_get_path(self):
        flushing = Vertex('Flushing')
        manhattan = Vertex('Manhattan')
        corona = Vertex('Corona')
        bronx = Vertex('Bronx')
        self.mta_stations.add_vertex(flushing)
        self.mta_stations.add_vertex(manhattan)
        self.mta_stations.add_vertex(corona)
        self.mta_stations.add_edge(flushing, corona)
        self.mta_stations.add_edge(manhattan, flushing)

        self.assertTrue(self.mta_stations.find_path(flushing, corona))
        self.assertTrue(self.mta_stations.find_path(manhattan, corona))
        self.assertFalse(self.mta_stations.find_path(flushing, bronx))


if __name__ == '__main__':
    unittest.main()