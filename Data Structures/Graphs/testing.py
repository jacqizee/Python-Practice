from graph import Graph
from vertex import Vertex
import unittest

class TestGraph(unittest.TestCase):
    def setUp(self) -> None:
        self.mta_stations = Graph()
        flushing = Vertex('Flushing')
        manhattan = Vertex('Manhattan')
        corona = Vertex('Corona')
        bronx = Vertex('Bronx')
        self.mta_stations.add_vertex(flushing)
        self.mta_stations.add_vertex(manhattan)
        self.mta_stations.add_vertex(corona)
        self.mta_stations.add_edge(flushing, corona)
        self.mta_stations.add_edge(manhattan, flushing)
    
    def test_graph_get_path(self):
        self.assertTrue(self.mta_stations.find_path_by_value('Flushing', 'Corona'))
        self.assertTrue(self.mta_stations.find_path_by_value('Manhattan', 'Corona'))
        self.assertFalse(self.mta_stations.find_path_by_value('Flushing', 'Bronx'))

    def test_graph_dfs(self):
        self.assertEqual(self.mta_stations.dfs('Manhattan', 'Corona'), ['Manhattan', 'Flushing', 'Corona'])

    def test_graph_bfs(self):
        self.assertEqual(self.mta_stations.bfs('Manhattan', 'Corona'), ['Manhattan', 'Flushing', 'Corona'])

if __name__ == '__main__':
    unittest.main()