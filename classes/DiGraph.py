import random

from src.GraphInterface import GraphInterface
from classes.Node import Node
from classes.Edge import Edge


class DiGraph(GraphInterface):
    def __init__(self):
        # id = int ,value = Node/class
        self.Nodes = {}
        # id = "src,dest" , value Edge/class
        self.Edges = {}
        self.mc = 0

    def __repr__(self):
        return "graph: |V|=" + str(self.v_size()) + " , |E|=" + str(self.e_size())

    def v_size(self) -> int:
        length = len(self.Nodes.values())
        return length

    def e_size(self) -> int:
        length = len(self.Edges.values())
        return length

    def get_all_v(self) -> dict:
        return self.Nodes

    # for evey Node there is a list of Nodes comming in and out of it
    # while running over the list i take the Node nedded and add it to my dict
    def all_in_edges_of_node(self, id1: int) -> dict:
        dict = {}

        node = self.Nodes.get(id1)
        node.into
        for Key in node.into:
            tempKey = str(Key) + "," + str(id1)
            edge = self.Edges.get(tempKey)
            dict[Key] = edge.weight

        return dict
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
         """

    def all_out_edges_of_node(self, id1: int) -> dict:
        dict = {}
        node = self.Nodes.get(id1)
        for Key in node.out:
            tempKey = str(id1) + "," + str(Key)
            edge = self.Edges.get(tempKey)
            dict[Key] = edge.weight

        return dict
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        key = str(id1) + "," + str(id2)
        if self.Edges.get(key) == None and self.Nodes.get(id1) != None and self.Nodes.get(id2) != None:
            # this will add to Edges
            self.Edges[key] = Edge(id1, id2, weight)
            # this will add to the lists "into" and "out" of id1 and id2
            self.Nodes.get(id1).out.append(id2)
            self.Nodes.get(id2).into.append(id1)
            self.mc += 1
            return True

        else:
            return False
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """

    import random
    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.Nodes.get(node_id) == None:
            if (pos == None):
                num1 = random.random() + 35
                num2 = random.random() + 32
                pos = (num1, num2, 0)
            self.Nodes[node_id] = Node(node_id, pos)
            self.mc += 1
            return True
        else:
            return False

        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """

    def remove_node(self, node_id: int) -> bool:
        if self.Nodes.get(node_id) != None:
            # this pops the Node out of the dict Node
            node_removed = self.Nodes.pop(node_id)

            # now we deall with the Edge
            for key in node_removed.into:
                # this removes all the Edges connected to that Node
                tempKey = str(key) + "," + str(node_id)
                self.Edges.pop(tempKey)
                # this will remove node_id from list out of Node Key
                self.Nodes.get(key).out.remove(node_id)

            for key in node_removed.out:
                # this removes all the Edges connected to that Node
                tempKey = str(node_id) + "," + str(key)
                self.Edges.pop(tempKey)
                # this will remove node_id from list into of Node Key
                self.Nodes.get(key).into.remove(node_id)

            return True
        else:
            return False

        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
        """

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        tempKey = str(node_id1) + "," + str(node_id2)
        if self.Edges.get(tempKey) != None:
            self.Nodes.get(node_id1).out.remove(node_id2)
            self.Nodes.get(node_id2).into.remove(node_id1)
            self.Edges.pop(tempKey)
            return True
        else:
            return False
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """
