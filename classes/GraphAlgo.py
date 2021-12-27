import json
import sys
from queue import PriorityQueue
from typing import List
from matplotlib import pyplot as plt

from classes import GUI
from classes.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, *args):
        if len(args) == 0:
            self.graph = DiGraph()
        if len(args) == 1:
            self.graph = args[0]

    def get_graph(self) -> GraphInterface:
        return self.graph
        """
        :return: the directed graph on which the algorithm works on.
        """

    def load_from_json(self, file_name: str) -> bool:
        try:
            file = open(file_name)
            data = json.load(file)
            g = DiGraph()
            nodes = data["Nodes"]
            for v in nodes:
                if dict(v).keys().__contains__('pos'):
                    loc = v["pos"].split(',')
                    pos = (loc[0],loc[1],loc[2])
                    g.add_node(v["id"], pos)
                else:
                    g.add_node(v["id"], None)
            edges = data["Edges"]
            for e in edges:
                g.add_edge(e["src"], e["dest"], e["w"])
            self.graph = g
            file.close()
            return True
        except Exception:
            return False

    def save_to_json(self, file_name: str) -> bool:
        try:
            Nodes = []
            Edges = []
            for v in self.graph.Nodes.values():
                # b = isinstance(v, type(Node))
                # if not b:
                #     return False
                key = v.get_key()
                loc = v.get_pos()#.split(',')
                pos=str(loc.x)+","+str(loc.y)+","+str(loc.z)
                node = {"id": key, "pos": pos}
                Nodes.append(node)

            for e in self.graph.Edges.values():
                # if not isinstance(v, Edge):
                #     return False
                src = e.getSrc()
                weight = e.getWeight()
                dest = e.getDest()
                edge = {"src": src, "w": weight, "dest": dest}
                Edges.append(edge)
            file = {"Edges": Edges, "Nodes": Nodes}
            with open(file_name, "w") as j:
                json.dump(file, j)
            # file_name.close()
            return True

        except Exception:
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        (dist, path) = self.dikjestra(id1)
        return (dist[id2], path[id2])

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        # this is a copy of the citiys to run on and the path the tsp will go in to
        total_dist= 0
        tsp_path = []

        # what i do is take node number 1 in the list and check the shortest path from it to the my list and save the closest one
        # i add it to my path remove the one i went to from my list
        # and run until my list is empty
        copy_list = []
        for id in node_lst:
            copy_list.append(id)

        temp_path = []
        first = copy_list.pop(0)
        tsp_path.append(first)
        cur_city = first
        while len(copy_list) != 0:
            shortestDist = sys.float_info.max
            id_short = -1

            for city in copy_list:
                count, path = GraphAlgo.shortest_path(self,cur_city,city)
                if count < shortestDist:
                    shortestDist = count
                    id_short = city
            dist, temp_path = GraphAlgo.shortest_path(self,cur_city,id_short)
            total_dist += dist
            # temp path is a String so we need to change it
            # first to a list of Strings
            # then to int list
            change1 = temp_path.split(',')
            change2 = map(int,change1)
            change3 = list(change2)

            change3.pop(0)
            while len(change3) != 0:
                tsp_path.append(change3.pop(0))
            cur_city = id_short
            copy_list.remove(id_short)

        if len(change3)==1:
            return None
        else:
            return tsp_path , total_dist
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """

    def centerPoint(self) -> (int, float):
        """
        Finds the node that has the shortest distance to it's farthest node.
        :return: The nodes id, min-maximum distance
        """
        maxDist = {}
        maxSize = float('inf')
        maxId = -1
        for v in self.graph.Nodes.values():
            (dist, path) = self.dikjestra(v.get_key())
            all_values = dist.values()
            check = max(all_values)
            if check < maxSize:
                maxId = v.get_key()
                maxSize = check
        return (maxId, maxSize)

    def plot_graph(self) -> None:
        GUI.Gui(self)
    # def plot_graph(self) -> None:
    #
    #     fig, ax = plt.subplots()
    #     # created rome for the button
    #     fig.subplots_adjust(bottom=0.2)
    #     # plt.axes([0,0,100,100])
    #     for v in self.graph.Nodes.values():
    #         pos = v.pos.getpos()
    #         x, y = pos[0], pos[1]
    #         plt.plot(float(x), float(y), markersize=4, marker='o', color='blue')
    #         plt.text(float(x), float(y), str(v.id), color="red", fontsize=12)
    #     for E in self.graph.Edges.values():
    #         src = self.graph.Nodes.get(E.src)
    #         x_src = src.get_pos().getpos()[0]
    #         y_src = src.get_pos().getpos()[1]
    #
    #         dest = self.graph.Nodes.get(E.dest)
    #         x_dest = dest.get_pos().getpos()[0]
    #         y_dest = dest.get_pos().getpos()[1]
    #         plt.annotate("", xy=(float(x_src), float(y_src)), xytext=(float(x_dest), float(y_dest)), arrowprops=dict(arrowstyle="<-"))
    #
    #     plt.show()
    def dikjestra(self, src: int) -> (list, list):
        visited = {v.get_key(): False for v in (self.graph.Nodes.values())}
        DistanceDist = {v.get_key(): float('inf') for v in (self.graph.Nodes.values())}
        DistanceDist[src] = 0
        DistancePath = {path.get_key(): "" for path in (self.graph.Nodes.values())}
        DistancePath[src] += str(src)
        pq = PriorityQueue()
        pq.put((0, src))
        while not pq.empty():
            (dist, current_vertex) = pq.get()
            visited[self.graph.Nodes[current_vertex]] = True
            cur = self.graph.Nodes[current_vertex]
            for neighbor in cur.get_out():
                key = str(cur.get_key()) + "," + str(neighbor)
                if not self.graph.Edges.keys().__contains__(key):
                    continue
                distance = self.graph.Edges[key].getWeight()
                if not visited[neighbor]:
                    new_path = DistancePath[current_vertex]
                    new_path += "," + str(neighbor)
                    old_cost = DistanceDist[neighbor]
                    new_cost = DistanceDist[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        DistanceDist[neighbor] = new_cost
                        DistancePath[neighbor] = new_path
        return DistanceDist, DistancePath


# if __name__ == '__main__':
    # graph = DiGraph()
    #
    # pos0 = (1, 2, 0)
    # pos1 = (5, 1, 0)
    # pos2 = (2, 5, 0)
    # pos3 = (6, 7, 0)
    # pos4 = (8, 4, 0)
    # pos5 = (5, 4, 0)
    #
    # graph.add_node(0, pos0)
    # graph.add_node(1, pos1)
    # graph.add_node(2, pos2)
    # graph.add_node(3, pos3)
    # graph.add_node(4, pos4)
    # graph.add_node(5, pos5)
    #
    # graph.add_edge(0, 1, 7)
    # graph.add_edge(1, 0, 7)
    #
    # graph.add_edge(0, 2, 14)
    # graph.add_edge(2, 0, 14)
    #
    # graph.add_edge(0, 5, 9)
    # graph.add_edge(5, 0, 9)
    #
    # graph.add_edge(1, 5, 10)
    # graph.add_edge(5, 1, 10)
    #
    # graph.add_edge(1, 4, 15)
    # graph.add_edge(4, 1, 15)
    #
    # graph.add_edge(2, 5, 2)
    # graph.add_edge(5, 2, 2)
    #
    # graph.add_edge(2, 3, 100)
    # # graph.add_edge(3, 2, 100)
    #
    # graph.add_edge(3, 4, 60)
    # graph.add_edge(4, 3, 60)
    #
    # graph.add_edge(5, 4, 20)
    # graph.add_edge(4, 5, 20)
    # list2 =[0,1,2,3,4,5]
    # algo = GraphAlgo(graph)
    # algo.plot_graph()
    # a=algo.graph.v_size()
    # print(algo.graph.v_size())
    # algo.save_to_json("../data/test_on.json")
    # algo2 =GraphAlgo()
    # algo2.load_from_json("../data/test_on.json")
    # algo2.plot_graph()
    # print(algo.TSP(list2))
    # print(algo.centerPoint())




