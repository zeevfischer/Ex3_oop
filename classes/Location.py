class Location:
   # def __init__(self,x = 0,y = 0,z = 0) -> None:
   #    self.x = x
   #    self.y = y
   #    self.z = z

   # def __init__(self,pos: tuple) -> None:
   #    self.x ,self.y ,self.z = pos

    def __init__(self,pos: tuple) -> None:
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]

    def getpos(self) -> tuple:
        pos = (self.x,self.y,self.z)
        return  pos



