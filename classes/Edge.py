class Edge:
    def __init__(self,data):
        self.src=data["src"]
        self.dest=data["dest"]
        self.weight=data["w"]

    def __init__(self,src = 0,dest = 0,weight = 0):
        self.src=src
        self.dest=dest
        self.weight=weight
    def getSrc(self):
        return self.src
    def getDest(self):
        return self.dest
    def getWeight(self):
        return self.weight