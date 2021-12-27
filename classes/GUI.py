import sys

import pygame
from pygame.constants import RESIZABLE
import pygame.gfxdraw
# from classes.GraphAlgo import GraphAlgo
import math
from tkinter import *
from classes import GUI_functions

pygame.font.init()
clock = pygame.time.Clock()
FONT = pygame.font.SysFont('comicsans', 20)


def scale(data: int, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimensions
    """
    return ((float(data) - float(min_data)) / (float(max_data) - float(min_data))) * (
            float(max_screen) - float(min_screen)) + float(min_screen)


min_x = sys.float_info.max
min_y = sys.float_info.max
max_x = 0
max_y = 0

def min_max(graph):
    global min_x, min_y, max_x, max_y
    min_x = sys.float_info.max
    min_y = sys.float_info.max
    max_x = 0
    max_y = 0
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
    def __init__(self, rect: pygame.Rect, color: tuple = (0, 0, 0)):
        self.rect = rect
        self.color = color
        self.pressed = False

    def press(self):
        self.pressed = not self.pressed


class Gui:
    pygame.font.init()
    clock = pygame.time.Clock()
    FONT = pygame.font.SysFont('comicsans', 20)

    def __init__(self, algo=None):
        self.algo = algo
        self.screen = pygame.display.set_mode((800, 600), depth=32, flags=RESIZABLE)
        min_max(algo.graph)
        self.button1 = Button(pygame.Rect(0, 0, 100, 50), (200, 200, 200))
        self.button2 = Button(pygame.Rect(105, 0, 100, 50), (200, 200, 200))
        self.button3 = Button(pygame.Rect(210, 0, 140, 50), (200, 200, 200))
        self.button4 = Button(pygame.Rect(355, 0, 80, 50), (200, 200, 200))
        self.button5 = Button(pygame.Rect(440, 0, 100, 50), (200, 200, 200))
        self.button6 = Button(pygame.Rect(545, 0, 100, 50), (200, 200, 200))
        self.button7 = Button(pygame.Rect(650, 0, 70, 50), (200, 200, 200))

        self.list_of_algo = []
        self.play()

    def arrow(self, start, end, d, h, color):
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

    def my_scale(self, data, x=False, y=False):
        if x:
            return scale(data, 100, self.screen.get_width() - 100, min_x, max_x)
        if y:
            return scale(data, 100, self.screen.get_height() - 100, min_y, max_y)

    def draw(self):
        width = self.screen.get_width() / 10
        hight = self.screen.get_height() / 10

        # || lines
        for num in range(11):
            src_x = 0 + (num * width)
            src_y = 0
            dest_x = 0 + (num * width)
            dest_y = self.my_scale(hight, y=True)
            Gui.arrow(self, (src_x, src_y), (dest_x, dest_y), 0, 0, color=(148, 148, 148))

            # text =str(num)
            # text_line= FONT.render(text, True, (0, 0, 0))
            # self.screen.blit(text_line, ( src_x,src_y ))

        # ---- lines
        for num in range(11):
            src_x = 0
            src_y = 0 + (num * hight)
            dest_x = self.my_scale(width, x=True)
            dest_y = 0 + (num * hight)
            Gui.arrow(self, (src_x, src_y), (dest_x, dest_y), 0, 0, color=(148, 148, 148))

            # text = str(num)
            # text_line = FONT.render(text, True, (0, 0, 0))
            # self.screen.blit(text_line, (src_x, src_y))

        # //////////////////////////////////////////////////////////////////////////////////////
        # this prints the Nodes and the Edges
        for edge in self.algo.graph.Edges.values():
            src = edge.src
            dest = edge.dest
            w = edge.weight
            src_x = self.my_scale(self.algo.graph.Nodes.get(src).pos.x, x=True)
            src_y = self.my_scale(self.algo.graph.Nodes.get(src).pos.y, y=True)
            dest_x = self.my_scale(self.algo.graph.Nodes.get(dest).pos.x, x=True)
            dest_y = self.my_scale(self.algo.graph.Nodes.get(dest).pos.y, y=True)

            Gui.arrow(self, (src_x, src_y), (dest_x, dest_y), 25, 6, color=(63, 97, 235))

            FONT = pygame.font.SysFont('comicsans', 10)
            text_surface = FONT.render(str(round(w, 2)), True, (0, 0, 0))
            self.screen.blit(text_surface, ((src_x * 0.25 + dest_x * 0.75), (src_y * 0.25 + dest_y * 0.75)))

        for src in self.algo.graph.Nodes.values():
            x = self.my_scale(src.pos.x, x=True)
            y = self.my_scale(src.pos.y, y=True)
            radius = 10
            FONT = pygame.font.SysFont('comicsans', 10)
            pygame.draw.circle(self.screen, color=(0, 0, 0), center=(x, y), radius=radius)
            node_text = FONT.render(str(src.id), True, (255, 255, 255))
            self.screen.blit(node_text, (x - 6, y - 10))

        # self.screen.blit(pygame.transform.rotate(self.screen,180),(0,0))
        FONT = pygame.font.SysFont('comicsans', 20)
        # button activation here i set all the buttons on the graph
        # here you can also see what each button dose acording to its string
        pygame.draw.rect(self.screen, self.button1.color, self.button1.rect)
        button_text = FONT.render("add node", True, (0, 0, 0))
        self.screen.blit(button_text, (self.button1.rect.x + 10, self.button1.rect.y + 5))

        pygame.draw.rect(self.screen, self.button2.color, self.button2.rect)
        button_text = FONT.render("RM node", True, (0, 0, 0))
        self.screen.blit(button_text, (self.button2.rect.x + 10, self.button2.rect.y + 5))

        pygame.draw.rect(self.screen, self.button3.color, self.button3.rect)
        button_text = FONT.render("shortest path", True, (0, 0, 0))
        self.screen.blit(button_text, (self.button3.rect.x + 10, self.button3.rect.y + 5))

        pygame.draw.rect(self.screen, self.button4.color, self.button4.rect)
        button_text = FONT.render("center", True, (0, 0, 0))
        self.screen.blit(button_text, (self.button4.rect.x + 10, self.button4.rect.y + 5))

        pygame.draw.rect(self.screen, self.button5.color, self.button5.rect)
        button_text = FONT.render("add Edge", True, (0, 0, 0))
        self.screen.blit(button_text, (self.button5.rect.x + 10, self.button5.rect.y + 5))

        pygame.draw.rect(self.screen, self.button6.color, self.button6.rect)
        button_text = FONT.render("RM Edge", True, (0, 0, 0))
        self.screen.blit(button_text, (self.button6.rect.x + 10, self.button6.rect.y + 5))

        pygame.draw.rect(self.screen, self.button7.color, self.button7.rect)
        button_text = FONT.render("TSP", True, (0, 0, 0))
        self.screen.blit(button_text, (self.button7.rect.x + 10, self.button7.rect.y + 5))

    def on_click(self, event):
        try:
            if event == "button1":
                try:
                    id, pos = GUI_functions.add_node()
                    self.algo.graph.add_node(id, pos)
                    Gui.play(self)
                except Exception:
                    GUI_functions.print("due to your last action", "error occurred")

            if event == "button2":
                try:
                    id = GUI_functions.remove_node()
                    self.algo.graph.remove_node(id)
                    Gui.play(self)
                except Exception:
                    GUI_functions.print("due to your last action", "error occurred")

            if event == "button3":
                src, dest = GUI_functions.shortest_path()
                sum, path = self.algo.shortest_path(src, dest)
                GUI_functions.print("the path is " + str(path), "shortest path ")
                Gui.play(self)

            if event == "button4":
                id, sum = self.algo.centerPoint()
                GUI_functions.print("the center Node is " + str(id), "center")
                Gui.play(self)

            if event == "button5":
                src, dest, weight = GUI_functions.add_Edge()
                self.algo.graph.add_edge(src, dest, weight)
                Gui.play(self)

            if event == "button6":
                src, dest = GUI_functions.remove_Edge()
                self.algo.graph.remove_edge(src, dest)
                Gui.play(self)

            if event == "button7":
                run_list = GUI_functions.TSP()
                change1 = run_list.split(',')
                change2 = map(int, change1)
                change3 = list(change2)
                print_tsp = self.algo.TSP(change3)
                GUI_functions.print(print_tsp, "Tsp")
                Gui.play(self)
        except Exception:
            GUI_functions.print("due to your last action", "error occurred")

    def play(self):
        min_max(self.algo.graph)
        run = True
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
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
                            self.on_click("button2")
                        else:
                            self.list_of_algo.clear()
                    # button 3 action
                    if self.button3.rect.collidepoint(event.pos):
                        self.button3.press()
                        if self.button3.pressed:
                            self.on_click("button3")
                        else:
                            self.list_of_algo.clear()
                    # button 4
                    if self.button4.rect.collidepoint(event.pos):
                        self.button4.press()
                        if self.button4.pressed:
                            self.on_click("button4")
                        else:
                            self.list_of_algo.clear()
                    # button 5
                    if self.button5.rect.collidepoint(event.pos):
                        self.button5.press()
                        if self.button5.pressed:
                            self.on_click("button5")
                        else:
                            self.list_of_algo.clear()
                    # button 6
                    if self.button6.rect.collidepoint(event.pos):
                        self.button6.press()
                        if self.button6.pressed:
                            self.on_click("button6")
                        else:
                            self.list_of_algo.clear()
                    # button 7
                    if self.button7.rect.collidepoint(event.pos):
                        self.button7.press()
                        if self.button7.pressed:
                            self.on_click("button7")
                        else:
                            self.list_of_algo.clear()

            pygame.display.set_mode((800, 600), depth=32, flags=RESIZABLE)
            self.screen.fill((255, 255, 255))
            self.draw()
            pygame.display.update()

# if __name__ == '__main__':
#     a=GraphAlgo()
#     a.load_from_json("../data/A1.json")
#     Gui(a)
