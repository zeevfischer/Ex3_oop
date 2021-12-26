import unittest
from DiGraph import *
from GraphAlgo import *

class TestGraph(unittest.TestCase):

    def test_Vsize(self):
        algo = GraphAlgo()
        algo.load_from_json("../data/test_on.json")
        self.assertEqual(algo.graph.v_size(), 6)

    def test_Eszie(self):
        algo = GraphAlgo()
        algo.load_from_json("../data/test_on.json")
        self.assertEqual(algo.graph.e_size(), 17)

    def test_getAll_V(self):
        algo = GraphAlgo()
        algo.load_from_json("../data/test_on.json")
        self.assertEqual(len(algo.graph.get_all_v()),6)
        self.assertTrue(algo.graph.Nodes.get(0) != None)
        self.assertTrue(algo.graph.Nodes.get(1) != None)
        self.assertTrue(algo.graph.Nodes.get(2) != None)
        self.assertTrue(algo.graph.Nodes.get(3) != None)
        self.assertTrue(algo.graph.Nodes.get(4) != None)
        self.assertTrue(algo.graph.Nodes.get(5) != None)

    def test_all_in(self):
        algo = GraphAlgo()
        algo.load_from_json("../data/test_on.json")

        into0 = [1, 2, 5]
        temp = algo.graph.Nodes.get(0).into
        self.assertEqual(into0[0], temp[0])
        self.assertEqual(into0[1], temp[1])
        self.assertEqual(into0[2], temp[2])

        into1 = [0, 5, 4]
        temp = algo.graph.Nodes.get(1).into
        self.assertEqual(into1[0], temp[0])
        self.assertEqual(into1[1], temp[1])
        self.assertEqual(into1[2], temp[2])

        into2 = [0, 5]
        temp = algo.graph.Nodes.get(2).into
        self.assertEqual(into2[0], temp[0])
        self.assertEqual(into2[1], temp[1])

        into3 = [2, 4]
        temp = algo.graph.Nodes.get(3).into
        self.assertEqual(into3[0], temp[0])
        self.assertEqual(into3[1], temp[1])

        into4 = [1, 3, 5]
        temp = algo.graph.Nodes.get(4).into
        self.assertEqual(into4[0], temp[0])
        self.assertEqual(into4[1], temp[1])
        self.assertEqual(into4[2], temp[2])

        into5 = [0, 1, 2, 4]
        temp = algo.graph.Nodes.get(5).into
        self.assertEqual(into5[0], temp[0])
        self.assertEqual(into5[1], temp[1])
        self.assertEqual(into5[2], temp[2])
        self.assertEqual(into5[3], temp[3])

    def test_all_out(self):
        algo = GraphAlgo()
        algo.load_from_json("../data/test_on.json")

        out0 = [1, 2, 5]
        temp = algo.graph.Nodes.get(0).out
        self.assertEqual(out0[0], temp[0])
        self.assertEqual(out0[1], temp[1])
        self.assertEqual(out0[2], temp[2])

        out1 = [0, 5, 4]
        temp = algo.graph.Nodes.get(1).out
        self.assertEqual(out1[0], temp[0])
        self.assertEqual(out1[1], temp[1])
        self.assertEqual(out1[2], temp[2])

        out2 = [0, 5, 3]
        temp = algo.graph.Nodes.get(2).out
        self.assertEqual(out2[0], temp[0])
        self.assertEqual(out2[1], temp[1])
        self.assertEqual(out2[2], temp[2])

        out3 = [4]
        temp = algo.graph.Nodes.get(3).out
        self.assertEqual(out3[0], temp[0])

        out4 = [1, 3, 5]
        temp = algo.graph.Nodes.get(4).out
        self.assertEqual(out4[0], temp[0])
        self.assertEqual(out4[1], temp[1])
        self.assertEqual(out4[2], temp[2])

        out5 = [0, 1, 2, 4]
        temp = algo.graph.Nodes.get(5).out
        self.assertEqual(out5[0], temp[0])
        self.assertEqual(out5[1], temp[1])
        self.assertEqual(out5[2], temp[2])
        self.assertEqual(out5[3], temp[3])

    def test_addNode(self):
        algo = GraphAlgo()
        algo.load_from_json("../data/test_on.json")
        self.assertEqual(algo.graph.Nodes.get(6) , None)
        self.assertTrue(algo.graph.add_node(6, (1, 7, 0.0)))
        self.assertEqual(algo.graph.v_size(), 7)

    def test_RmNode(self):
        algo = GraphAlgo()
        algo.load_from_json("../data/test_on.json")
        self.assertTrue(algo.graph.Nodes.get(5) != None)
        self.assertEqual(algo.graph.v_size(), 6)
        algo.graph.remove_node(5)
        self.assertTrue(algo.graph.Nodes.get(5) == None)
        self.assertEqual(algo.graph.v_size(), 5)

    def test_addEdge(self):
        algo = GraphAlgo()
        algo.load_from_json("../data/test_on.json")
        tempKey = str(3) + "," + str(2)
        self.assertTrue(algo.graph.Edges.get(tempKey) == None)
        self.assertEqual(algo.graph.e_size(), 17)
        algo.graph.add_edge(3,2,100)
        self.assertTrue(algo.graph.Edges.get(tempKey) != None)
        self.assertEqual(algo.graph.e_size(), 18)

    def test_RmEdge(self):
        algo = GraphAlgo()
        algo.load_from_json("../data/test_on.json")
        tempKey = str(2) + "," + str(3)
        self.assertTrue(algo.graph.Edges.get(tempKey) != None)
        self.assertEqual(algo.graph.e_size(), 17)
        self.assertTrue(algo.graph.remove_edge(2,3))
        self.assertTrue(algo.graph.Edges.get(tempKey) == None)
        self.assertEqual(algo.graph.e_size(), 16)



