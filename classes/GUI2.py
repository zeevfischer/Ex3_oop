import sys

import pygame
from pygame.constants import RESIZABLE
import pygame.gfxdraw
from classes.GraphAlgo import GraphAlgo
import math

pygame.font.init()
clock = pygame.time.Clock()
FONT = pygame.font.SysFont('comicsans', 20)

def scale(data: int, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimensions
    """
    return ((float(data) - float(min_data)) / (float(max_data)-float(min_data))) * (float(max_screen) - float(min_screen)) + float(min_screen)

min_x = sys.float_info.max
min_y = sys.float_info.max
max_x = 0
max_y = 0
def min_max(graph):

    global min_x,min_y,max_x,max_y
    for node in graph.Nodes.values():
        if float(node.pos.x) < float(min_x):
            min_x = node.pos.x

        if float(node.pos.x) > float(max_x):
            max_x = node.pos.x

        if float(node.pos.y) < float(min_y):
            min_y = node.pos.y

        if float(node.pos.y) > float(max_y):
            max_y = node.pos.y

class Button:
    def __init__(self, rect:pygame.Rect,color:tuple=(0,0,0)):
        self.rect=rect
        self.color=color
        self.pressed=False
    def press(self):
        self.pressed=not self.pressed


# class OnClick():
#     def __init__(self,algo:GraphAlgo):
#         self.algo = algo
#
#     def add_node(self, node_id: int, pos: tuple):
#         self.algo.graph.add_node(node_id,pos)

    # def remove_node(self):
    #
    # def add_Edge(self):
    #
    # def remove_edge(self):
    #
    # def TSP (self);
    #
    # def center(self):
    #
    # def shortest_path(self):

class Gui:
    def __init__(self,algo=None):
        self.algo=algo
        self.screen = pygame.display.set_mode((800, 600), depth=32, flags=RESIZABLE)
        min_max(algo.graph)
        self.button1 = Button(pygame.Rect(0, 0, 80, 50), (200, 200, 200))
        self.button2 = Button(pygame.Rect(85, 0, 80, 50), (200, 200, 200))
        self.button3 = Button(pygame.Rect(170, 0, 80, 50), (200, 200, 200))
        self.button4 = Button(pygame.Rect(255, 0, 80, 50), (200, 200, 200))

        self.list_of_algo=[]
        self.play()

    def arrow(self,start, end, d, h, color):
        dx = (end[0] - start[0])
        dy = (end[1] - start[1])
        D = (math.sqrt(dx * dx + dy * dy))
        xm = (D - d)
        xn = (xm)
        ym = (h)
        yn = -h
        sin = dy / D
        cos = dx / D
        x = xm * cos - ym * sin + start[0]
        ym = xm * sin + ym * cos + start[1]
        xm = x
        x = xn * cos - yn * sin + start[0]
        yn = xn * sin + yn * cos + start[1]
        xn = x
        points = [(end[0], end[1]), (int(xm), int(ym)), (int(xn), int(yn))]

        pygame.draw.line(self.screen, color, start, end, width=4)
        pygame.draw.polygon(self.screen, color, points)

    def my_scale(self,data, x=False, y=False):
        if x:
            return scale(data, 50, self.screen.get_width() - 50, min_x, max_x)
        if y:
            return scale(data, 50, self.screen.get_height() - 50, min_y, max_y)

    def draw(self):
        width = self.screen.get_width() / 10
        hight = self.screen.get_height() / 10

        # || lines
        for num in range(11):
            src_x = 0 + (num * width)
            src_y = 0
            dest_x = 0+(num*width)
            dest_y = self.my_scale(hight, y=True)
            Gui.arrow(self, (src_x, src_y), (dest_x, dest_y), 0, 0, color=(148, 148, 148))

            # text =str(num)
            # text_line= FONT.render(text, True, (0, 0, 0))
            # self.screen.blit(text_line, ( src_x,src_y ))

        # ---- lines
        for num in range(11):
            src_x = 0
            src_y = 0 +(num* hight)
            dest_x = self.my_scale(width,x =True)
            dest_y = 0+ (num*hight)
            Gui.arrow(self, (src_x, src_y), (dest_x, dest_y), 0, 0, color=(148, 148, 148))

            # text = str(num)
            # text_line = FONT.render(text, True, (0, 0, 0))
            # self.screen.blit(text_line, (src_x, src_y))

        # //////////////////////////////////////////////////////////////////////////////////////
        for edge in self.algo.graph.Edges.values():
            src = edge.src
            dest = edge.dest
            w = edge.weight
            src_x = self.my_scale(self.algo.graph.Nodes.get(src).pos.x, x=True)
            src_y = self.my_scale(self.algo.graph.Nodes.get(src).pos.y, y=True)
            dest_x = self.my_scale(self.algo.graph.Nodes.get(dest).pos.x, x=True)
            dest_y = self.my_scale(self.algo.graph.Nodes.get(dest).pos.y, y=True)

            Gui.arrow(self, (src_x, src_y), (dest_x, dest_y), 30, 8, color=(63,97, 235))

        for src in self.algo.graph.Nodes.values():
            x = self.my_scale(src.pos.x, x=True)
            y = self.my_scale(src.pos.y, y=True)
            radius = 15
            pygame.draw.circle(self.screen, color=(0, 0, 0), center=(x, y), radius=radius)
            node_text = FONT.render(str(src.id), True, (255, 255, 255))
            self.screen.blit(node_text, (x - 6, y - 13))

        pygame.draw.rect(self.screen, self.button1.color, self.button1.rect)
        button_text = FONT.render("ALGO", True, (0, 0, 0))
        self.screen.blit(button_text, (self.button1.rect.x + 10, self.button1.rect.y + 5))

        pygame.draw.rect(self.screen, self.button2.color, self.button2.rect)
        button_text = FONT.render("ALGO", True, (0, 0, 0))
        self.screen.blit(button_text, (self.button2.rect.x + 10, self.button2.rect.y + 5))

        pygame.draw.rect(self.screen, self.button3.color, self.button3.rect)
        button_text = FONT.render("ALGO", True, (0, 0, 0))
        self.screen.blit(button_text, (self.button3.rect.x + 10, self.button3.rect.y + 5))

        pygame.draw.rect(self.screen, self.button4.color, self.button4.rect)
        button_text = FONT.render("ALGO", True, (0, 0, 0))
        self.screen.blit(button_text, (self.button4.rect.x + 10, self.button4.rect.y + 5))

    # def on_click(self,event):

        # if event == "button1":


    def play(self):
        run=True
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
                if event.type==pygame.MOUSEBUTTONDOWN:
                    # button one action
                    if self.button1.rect.collidepoint(event.pos):
                        self.button1.press()
                        if self.button1.pressed:
                            self.on_click("button1")
                        else:
                            self.list_of_algo.clear()
                    # button tew action
                    if self.button2.rect.collidepoint(event.pos):
                        self.button2.press()
                        if self.button2.pressed:
                            self.on_click()
                        else:
                            self.list_of_algo.clear()
            self.screen.fill((255, 255, 255))
            self.draw()

            pygame.display.update()

if __name__ == '__main__':
    a=GraphAlgo()
    a.load_from_json("../data/A1.json")
    Gui(a)



