from classes.Location import Location


class Node:
    def __init__(self, id, pos: tuple) -> None:
        # x,y,z = pos
        # self.pos = Location(x,y,z)
        self.pos = Location(pos)
        self.id = id

        self.weight = -1
        self.tag = 0

        # this will hold a list of all nodes going in to this Node
        # this is a list of src that i am the dest to
        self.into = []
        # this will hold a list of all nodes going out of this Node
        # this is a list of dest where i am the src to
        self.out = []

    def __repr__(self) -> str:
        return str(self.id)+": |edges out| "+str(len(self.out))+" |edges in| "+str(len(self.into))


    def get_into(self):
        return self.into

    def get_out(self):
        return self.out

    def get_key(self):
        return self.id

    def get_pos(self):
        return self.pos
