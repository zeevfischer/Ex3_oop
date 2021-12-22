import json
from queue import PriorityQueue

from DiGraph import DiGraph
from classes import Node
from classes import Edge
from src.GraphAlgoInterface import GraphAlgoInterface


class graphAlgo(GraphAlgoInterface):
    def __init__(self):
        self.graph = DiGraph()

    #
    # def __init__(self, g: DiGraph):
    #     self.graph = g

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

    def dikjestra(self, src: int) -> (list, list):
        visited = {v: False for v in (self.graph.Nodes.values())}
        DistanceDist = {v: float('inf') for v in (self.graph.Nodes.values())}
        DistanceDist[src] = 0
        DistancePath = {path: "" for path in (self.graph.Nodes.values())}
        DistancePath[self.graph.Nodes[src]] += str(src)
        pq = PriorityQueue()
        pq.put((0, src))
        while not pq.empty():
            (dist, current_vertex) = pq.get()
            visited[self.graph.Nodes[current_vertex]] = True
            cur = self.graph.Nodes[current_vertex]
            for neighbor in cur.get_out():
                distance = self.graph.Edges[str(src) + "," + str(neighbor)].getWeight()
                if not visited[self.graph.Nodes[neighbor]]:
                    if neighbor not in visited:
                        new_path = DistancePath[self.graph.Nodes[current_vertex]]
                        new_path+=str(neighbor)
                        old_cost = DistanceDist[self.graph.Nodes[neighbor]]
                        new_cost = DistanceDist[self.graph.Nodes[current_vertex]] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            DistanceDist[neighbor] = new_cost
                            DistancePath[neighbor] = new_path
        return DistanceDist, DistancePath

    def plot_graph(self) -> None:
        pass


if __name__ == '__main__':
    ga = graphAlgo()
    ga.load_from_json("C:\\Users\\Liavm\\Desktop\\Ex3\\data\\A0.json")
    (dist,path)=ga.dikjestra(0)
    print(dist)
    ga.save_to_json("C:\\Users\\Liavm\\Desktop\\Ex3\\data\\out.json")
