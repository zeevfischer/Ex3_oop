class Location:
    def __init__(self,pos: tuple) -> None:
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]

    def getpos(self) -> tuple:
        pos = (self.x,self.y,self.z)
        return pos



