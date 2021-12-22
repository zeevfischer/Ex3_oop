import json
from queue import PriorityQueue

from classes.DiGraph import DiGraph
from classes.Edge import Edge
from classes.Node import Node
from classes.Location import Location
# import matplotlib.pyplot as plt
from src.GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):
    def __init__(self):
        self.graph=DiGraph()

    def __init__(self,g: DiGraph()):
        self.graph = g

    #
    # def __init__(self, g: DiGraph):
    #     self.graph = g

    # def get_graph(self) -> GraphInterface:
    #     """
    #     :return: the directed graph on which the algorithm works on.
    #     """

    def load_from_json(self, file_name: str) -> bool:
        try:
            file = open(file_name)
            data = json.load(file)
            g = DiGraph()
            nodes = data["Nodes"]
            for v in nodes:
                g.add_node(v["id"], v["pos"])
            edges = data["Edges"]
            for e in edges:
                g.add_edge(e["src"], e["dest"], e["w"])
            self.graph = g
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
                pos = v.get_pos()
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
            with open(file_name, 'w') as j:
                json.dump(file, j)
            return True

        except Exception:
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        (dist, path) = self.dikjestra(id1)
        return (dist[id2], dist[id2])

    # def TSP(self, node_lst: List[int]) -> (List[int], float):
    #     """
    #     Finds the shortest path that visits all the nodes in the list
    #     :param node_lst: A list of nodes id's
    #     :return: A list of the nodes id's in the path, and the overall distance
    #     """

    def centerPoint(self) -> (int, float):
        """
        Finds the node that has the shortest distance to it's farthest node.
        :return: The nodes id, min-maximum distance
        """
        maxDist={}
        maxSize='inf'
        maxId=-1
        for v in self.graph.Nodes.values():
            (dist,path)=self.dikjestra(v)
            check=max(dist,key=lambda x:float (x))
            if check<maxSize:
                maxId=v.get_key
                maxSize=check
        return (maxId,maxSize)




    # def plot_graph(self) -> None:
    #     for v in self.graph.Nodes.values():
    #         pos = v.pos.getpos()
    #         x, y = pos[0] , pos[1]
    #         print(x, y)
    #         plt.plot(x, y, markersize=4, marker='o', color='blue')
    #         plt.text(x, y, str(v.id), color="red", fontsize=12)
    #     for E in self.graph.Edges.values():
    #         src = self.graph.Nodes.get(Edge(E).src)
    #         x_src = Node(src).pos['x']
    #         y_src = Node(src).pos['y']
    #
    #         dest = self.graph.Nodes.get(Edge(E).dest)
    #         x_dest = Node(dest).pos.getpos()
    #         y_dest = Node(dest).pos['y']
    #         plt.annotate("", xy=(x_src, y_src), xytext=(x_dest, y_dest), arrowprops=dict(arrowstyle="<-"))
    #
    #     plt.show()

    def dikjestra(self, src: int) -> (list, list):

        visited = {v.get_key(): False for v in (self.graph.Nodes.values())}
        DistanceDist = {v.get_key(): float('inf') for v in (self.graph.Nodes.values())}
        DistanceDist[src] = 0
        DistancePath = {path.get_key(): "" for path in (self.graph.Nodes.values())}
        DistancePath[src] += str(src)
        pq = PriorityQueue()
        pq.put((0,src))
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
                        new_path += "," +str(neighbor)
                        old_cost = DistanceDist[neighbor]
                        new_cost = DistanceDist[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            DistanceDist[neighbor] = new_cost
                            DistancePath[neighbor] = new_path
        return DistanceDist, DistancePath

if __name__ == '__main__':
    ga = GraphAlgo()
    ga.load_from_json("C:\\Users\\Liavm\\Desktop\\Ex3\\data\\A5.json")
    (dist,path)=ga.dikjestra(0)
    print(path[2])
    ga.save_to_json("C:\\Users\\Liavm\\Desktop\\Ex3\\data\\out.json")
