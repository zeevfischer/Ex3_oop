import unittest
from DiGraph import *
from GraphAlgo import *

class TestAlgo(unittest.TestCase):
    def test_lode(self):
        algo = GraphAlgo()
        self.assertTrue(len(algo.graph.Nodes.values()) == 0)
        self.assertTrue(len(algo.graph.Edges.values()) == 0)
        algo.load_from_json("../data/test_on.json")
        self.assertTrue(len(algo.graph.Nodes.values()) == 6)
        self.assertTrue(len(algo.graph.Edges.values()) == 17)

    def test_save(self):
        graph = DiGraph()

        pos0 = (1, 2, 0)
        pos1 = (5, 1, 0)
        pos2 = (2, 5, 0)
        pos3 = (6, 7, 0)
        pos4 = (8, 4, 0)
        pos5 = (5, 4, 0)

        graph.add_node(0, pos0)
        graph.add_node(1, pos1)
        graph.add_node(2, pos2)
        graph.add_node(3, pos3)
        graph.add_node(4, pos4)
        graph.add_node(5, pos5)

        graph.add_edge(0, 1, 7)
        graph.add_edge(1, 0, 7)
        graph.add_edge(0, 2, 14)
        graph.add_edge(2, 0, 14)
        graph.add_edge(0, 5, 9)
        graph.add_edge(5, 0, 9)
        graph.add_edge(1, 5, 10)
        graph.add_edge(5, 1, 10)
        graph.add_edge(1, 4, 15)
        graph.add_edge(4, 1, 15)
        graph.add_edge(2, 5, 2)
        graph.add_edge(5, 2, 2)
        graph.add_edge(2, 3, 100)
        graph.add_edge(3, 4, 60)
        graph.add_edge(4, 3, 60)
        graph.add_edge(5, 4, 20)
        graph.add_edge(4, 5, 20)
        algo = GraphAlgo(graph)
        algo.save_to_json("../data/tester_save.json")

        algo2 =GraphAlgo()
        algo2.load_from_json("../data/tester_save.json")

        temp = algo2.graph.Nodes.get(0)
        self.assertTrue(int(temp.pos.x) == 1)
        self.assertTrue(int(temp.pos.y) == 2)

        temp = algo2.graph.Nodes.get(1)
        self.assertTrue(int(temp.pos.x) == 5)
        self.assertTrue(int(temp.pos.y) == 1)

        temp = algo2.graph.Nodes.get(2)
        self.assertTrue(int(temp.pos.x) == 2)
        self.assertTrue(int(temp.pos.y) == 5)

        temp = algo2.graph.Nodes.get(3)
        self.assertTrue(int(temp.pos.x) == 6)
        self.assertTrue(int(temp.pos.y) == 7)

        temp = algo2.graph.Nodes.get(4)
        self.assertTrue(int(temp.pos.x) == 8)
        self.assertTrue(int(temp.pos.y) == 4)

        temp = algo2.graph.Nodes.get(5)
        self.assertTrue(int(temp.pos.x) == 5)
        self.assertTrue(int(temp.pos.y) == 4)


    # def test_shortestPath(self):
    #
    # def test_center(self):
