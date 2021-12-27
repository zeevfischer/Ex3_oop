from typing import List
import pygame
from pygame import RESIZABLE

# these function are the input for every button after closing each one the input will be returned to the main function
def add_node() -> (int,tuple):
    pygame.init()
    clock =pygame.time.Clock()
    screen = pygame.display.set_mode((500, 250),flags=RESIZABLE)

    base_font =pygame.font.Font(None,32)
    head_font = pygame.font.Font(None,40)

    text_id =''
    text_x = ''
    text_y = ''
    text_z = ''



    inpur_rect_id = pygame.Rect(120, 35, 140, 32)
    inpur_rect_src = pygame.Rect(120, 80, 140, 32)
    inpur_rect_dest = pygame.Rect(120, 122, 140, 32)
    inpur_rect_weight = pygame.Rect(120, 165, 140, 32)


    color = pygame.Color('lightskyblue3')
    # color_passive = pygame.Color('gray15')
    active_id = False
    active_x = False
    active_y = False
    active_z = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pos = (int(text_x),int(text_y),int(text_z))
                return (int(text_id),pos)
                # pygame.quit()
                # sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if inpur_rect_id.collidepoint(event.pos):
                    active_id = True
                else:
                    active_id = False

                if inpur_rect_src.collidepoint(event.pos):
                    active_x = True
                else:
                    active_x = False

                if inpur_rect_dest.collidepoint(event.pos):
                    active_y = True
                else:
                    active_y = False

                if inpur_rect_weight.collidepoint(event.pos):
                    active_z = True
                else:
                    active_z = False

            if event.type == pygame.KEYDOWN:
                if active_id == True:
                    if event.key == pygame.K_BACKSPACE:
                        text_id = text_id[0:-1]
                    else:
                        text_id += event.unicode

                if active_x == True:
                    if event.key == pygame.K_BACKSPACE:
                        text_x = text_x[0:-1]
                    else:
                        text_x += event.unicode

                if active_y == True:
                    if event.key == pygame.K_BACKSPACE:
                        text_y = text_y[0:-1]
                    else:
                        text_y += event.unicode

                if active_z == True:
                    if event.key == pygame.K_BACKSPACE:
                        text_z = text_z[0:-1]
                    else:
                        text_z += event.unicode

        screen.fill((0,0,0))
        # if active_id:
        #     color = color_active
        # if active_id==False:
        #     color = color_passive
        #
        # if active_x:
        #     color = color_active
        # if active_x==False:
        #     color = color_passive
        #
        # if active_y:
        #     color = color_active
        # if active_y==False:
        #     color = color_passive
        #
        # if active_z:
        #     color = color_active
        # if active_z==False:
        #     color = color_passive


        pygame.draw.rect(screen, color, inpur_rect_id, 2)
        pygame.draw.rect(screen, color, inpur_rect_src, 2)
        pygame.draw.rect(screen, color, inpur_rect_dest, 2)
        pygame.draw.rect(screen, color, inpur_rect_weight, 2)

        # text input location
        test_surface = base_font.render(text_id,True,(255,255,255))
        screen.blit(test_surface,(inpur_rect_id.x+5,inpur_rect_id.y+5))
        inpur_rect_id.w = max(100, test_surface.get_width() + 10)

        test_surface = base_font.render(text_x, True, (255, 255, 255))
        screen.blit(test_surface, (inpur_rect_src.x + 5, inpur_rect_src.y + 5))
        inpur_rect_src.w = max(100, test_surface.get_width() + 10)

        test_surface = base_font.render(text_y, True, (255, 255, 255))
        screen.blit(test_surface, (inpur_rect_dest.x + 5, inpur_rect_dest.y + 5))
        inpur_rect_dest.w = max(100, test_surface.get_width() + 10)

        test_surface = base_font.render(text_z, True, (255, 255, 255))
        screen.blit(test_surface, (inpur_rect_weight.x + 5, inpur_rect_weight.y + 5))
        inpur_rect_weight.w = max(100, test_surface.get_width() + 10)


        # head line text location // prints
        test_surface = head_font.render("click, enter data and exit", True, (255, 255, 255))
        screen.blit(test_surface,(100,0))

        test_surface = head_font.render("enter id", True, (255, 255, 255))
        screen.blit(test_surface, (5, 39))

        test_surface = head_font.render("enter x", True, (255, 255, 255))
        screen.blit(test_surface, (5, 82))

        test_surface = head_font.render("enter y", True, (255, 255, 255))
        screen.blit(test_surface, (5, 125))

        test_surface = head_font.render("enter z", True, (255, 255, 255))
        screen.blit(test_surface, (5, 168))

        pygame.display.flip()
        clock.tick(60)

def remove_node() -> (int):
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((500, 250),flags=RESIZABLE)

    base_font = pygame.font.Font(None, 32)
    head_font = pygame.font.Font(None, 40)

    text_id = ''

    inpur_rect_id = pygame.Rect(120, 35, 140, 32)

    color = pygame.Color('lightskyblue3')
    # color_passive = pygame.Color('gray15')
    active_id = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return int(text_id)
                # pygame.quit()
                # sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if inpur_rect_id.collidepoint(event.pos):
                    active_id = True
                else:
                    active_id = False

            if event.type == pygame.KEYDOWN:
                if active_id == True:
                    if event.key == pygame.K_BACKSPACE:
                        text_id = text_id[0:-1]
                    else:
                        text_id += event.unicode

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, color, inpur_rect_id, 2)

        # text input location
        test_surface = base_font.render(text_id, True, (255, 255, 255))
        screen.blit(test_surface, (inpur_rect_id.x + 5, inpur_rect_id.y + 5))
        inpur_rect_id.w = max(100, test_surface.get_width() + 10)

        # head line text location // prints
        test_surface = head_font.render("click, enter data and exit", True, (255, 255, 255))
        screen.blit(test_surface, (100, 0))

        test_surface = head_font.render("enter id", True, (255, 255, 255))
        screen.blit(test_surface, (5, 39))

        pygame.display.flip()
        clock.tick(60)

def shortest_path() -> (int, int):
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((500, 250),flags=RESIZABLE)

    base_font = pygame.font.Font(None, 32)
    head_font = pygame.font.Font(None, 40)

    text_src = ''
    text_dest = ''

    inpur_rect_src = pygame.Rect(150, 35, 140, 32)
    inpur_rect_dest= pygame.Rect(150, 80, 140, 32)


    color = pygame.Color('lightskyblue3')
    # color_passive = pygame.Color('gray15')
    active_src = False
    active_dest = False


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return (int(text_src), int(text_dest))
                # pygame.quit()
                # sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if inpur_rect_src.collidepoint(event.pos):
                    active_src = True
                else:
                    active_src = False

                if inpur_rect_dest.collidepoint(event.pos):
                    active_dest = True
                else:
                    active_dest = False

            if event.type == pygame.KEYDOWN:
                if active_src == True:
                    if event.key == pygame.K_BACKSPACE:
                        text_src = text_src[0:-1]
                    else:
                        text_src += event.unicode

                if active_dest == True:
                    if event.key == pygame.K_BACKSPACE:
                        text_dest = text_dest[0:-1]
                    else:
                        text_dest += event.unicode

        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, color, inpur_rect_src, 2)
        pygame.draw.rect(screen, color, inpur_rect_dest, 2)

        # text input location
        test_surface = base_font.render(text_src, True, (255, 255, 255))
        screen.blit(test_surface, (inpur_rect_src.x + 5, inpur_rect_src.y + 5))
        inpur_rect_src.w = max(100, test_surface.get_width() + 10)

        test_surface = base_font.render(text_dest, True, (255, 255, 255))
        screen.blit(test_surface, (inpur_rect_dest.x + 5, inpur_rect_dest.y + 5))
        inpur_rect_dest.w = max(100, test_surface.get_width() + 10)


        # head line text location // prints
        test_surface = head_font.render("click, enter data and exit", True, (255, 255, 255))
        screen.blit(test_surface, (100, 0))

        test_surface = head_font.render("enter src", True, (255, 255, 255))
        screen.blit(test_surface, (5, 39))

        test_surface = head_font.render("enter dest", True, (255, 255, 255))
        screen.blit(test_surface, (5, 82))


        pygame.display.flip()
        clock.tick(60)

def print(text,titel) -> bool:
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((500, 250),flags=RESIZABLE)

    base_font = pygame.font.Font(None, 32)
    head_font = pygame.font.Font(None, 40)

    color = pygame.Color('lightskyblue3')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
                # pygame.quit()
                # sys.exit()

        screen.fill((0, 0, 0))
        # head line text location // prints
        test_surface = head_font.render(str(titel), True, (255, 255, 255))
        screen.blit(test_surface, (140, 0))

        test_surface = head_font.render(str(text), True, (255, 255, 255))
        screen.blit(test_surface, (5, 50))

        test_surface = head_font.render("to return to graph Exit", True, (255, 255, 255))
        screen.blit(test_surface, (105, 220))

        pygame.display.flip()
        clock.tick(60)

def add_Edge()->(int,int,float):
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((500, 250), flags=RESIZABLE)

    base_font = pygame.font.Font(None, 32)
    head_font = pygame.font.Font(None, 40)

    text_src = ''
    text_dest = ''
    text_weight = ''

    inpur_rect_src = pygame.Rect(150, 35, 140, 32)
    inpur_rect_dest = pygame.Rect(180, 80, 140, 32)
    inpur_rect_weight = pygame.Rect(210, 122, 140, 32)

    color = pygame.Color('lightskyblue3')
    active_src = False
    active_dest = False
    active_weight = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return (int(text_src),int(text_dest),int(text_weight))
                # pygame.quit()
                # sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if inpur_rect_src.collidepoint(event.pos):
                    active_src = True
                else:
                    active_src = False

                if inpur_rect_dest.collidepoint(event.pos):
                    active_dest = True
                else:
                    active_dest = False

                if inpur_rect_weight.collidepoint(event.pos):
                    active_weight = True
                else:
                    active_weight = False

            if event.type == pygame.KEYDOWN:
                if active_src == True:
                    if event.key == pygame.K_BACKSPACE:
                        text_src = text_src[0:-1]
                    else:
                        text_src += event.unicode

                if active_dest == True:
                    if event.key == pygame.K_BACKSPACE:
                        text_dest = text_dest[0:-1]
                    else:
                        text_dest += event.unicode

                if active_weight == True:
                    if event.key == pygame.K_BACKSPACE:
                        text_weight = text_weight[0:-1]
                    else:
                        text_weight += event.unicode

        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, color, inpur_rect_src, 2)
        pygame.draw.rect(screen, color, inpur_rect_dest, 2)
        pygame.draw.rect(screen, color, inpur_rect_weight, 2)

        # text input location
        test_surface = base_font.render(text_src, True, (255, 255, 255))
        screen.blit(test_surface, (inpur_rect_src.x + 5, inpur_rect_src.y + 5))
        inpur_rect_src.w = max(100, test_surface.get_width() + 10)

        test_surface = base_font.render(text_dest, True, (255, 255, 255))
        screen.blit(test_surface, (inpur_rect_dest.x + 5, inpur_rect_dest.y + 5))
        inpur_rect_dest.w = max(100, test_surface.get_width() + 10)

        test_surface = base_font.render(text_weight, True, (255, 255, 255))
        screen.blit(test_surface, (inpur_rect_weight.x + 5, inpur_rect_weight.y + 5))
        inpur_rect_weight.w = max(100, test_surface.get_width() + 10)

        # head line text location // prints
        test_surface = head_font.render("click, enter data and exit", True, (255, 255, 255))
        screen.blit(test_surface, (100, 0))

        test_surface = head_font.render("enter src", True, (255, 255, 255))
        screen.blit(test_surface, (5, 39))

        test_surface = head_font.render("enter dest", True, (255, 255, 255))
        screen.blit(test_surface, (5, 82))

        test_surface = head_font.render("enter weight", True, (255, 255, 255))
        screen.blit(test_surface, (5, 125))

        pygame.display.flip()
        clock.tick(60)

def remove_Edge() ->(int,int):
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((500, 250), flags=RESIZABLE)

    base_font = pygame.font.Font(None, 32)
    head_font = pygame.font.Font(None, 40)

    text_src = ''
    text_dest = ''

    inpur_rect_src = pygame.Rect(150, 35, 140, 32)
    inpur_rect_dest = pygame.Rect(150, 80, 140, 32)

    color = pygame.Color('lightskyblue3')
    active_src = False
    active_dest = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return (int(text_src), int(text_dest))
                # pygame.quit()
                # sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if inpur_rect_src.collidepoint(event.pos):
                    active_src = True
                else:
                    active_src = False

                if inpur_rect_dest.collidepoint(event.pos):
                    active_dest = True
                else:
                    active_dest = False

            if event.type == pygame.KEYDOWN:
                if active_src == True:
                    if event.key == pygame.K_BACKSPACE:
                        text_src = text_src[0:-1]
                    else:
                        text_src += event.unicode

                if active_dest == True:
                    if event.key == pygame.K_BACKSPACE:
                        text_dest = text_dest[0:-1]
                    else:
                        text_dest += event.unicode

        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, color, inpur_rect_src, 2)
        pygame.draw.rect(screen, color, inpur_rect_dest, 2)

        # text input location
        test_surface = base_font.render(text_src, True, (255, 255, 255))
        screen.blit(test_surface, (inpur_rect_src.x + 5, inpur_rect_src.y + 5))
        inpur_rect_src.w = max(100, test_surface.get_width() + 10)

        test_surface = base_font.render(text_dest, True, (255, 255, 255))
        screen.blit(test_surface, (inpur_rect_dest.x + 5, inpur_rect_dest.y + 5))
        inpur_rect_dest.w = max(100, test_surface.get_width() + 10)

        # head line text location // prints
        test_surface = head_font.render("click, enter data and exit", True, (255, 255, 255))
        screen.blit(test_surface, (100, 0))

        test_surface = head_font.render("enter src", True, (255, 255, 255))
        screen.blit(test_surface, (5, 39))

        test_surface = head_font.render("enter dest", True, (255, 255, 255))
        screen.blit(test_surface, (5, 82))

        pygame.display.flip()
        clock.tick(60)

def TSP()-> (List[int]):
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((500, 250), flags=RESIZABLE)

    base_font = pygame.font.Font(None, 32)
    head_font = pygame.font.Font(None, 40)

    text_id = ''

    inpur_rect_id = pygame.Rect(0, 100, 300, 32)

    color = pygame.Color('lightskyblue3')
    # color_passive = pygame.Color('gray15')
    active_id = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return text_id
                # pygame.quit()
                # sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if inpur_rect_id.collidepoint(event.pos):
                    active_id = True
                else:
                    active_id = False

            if event.type == pygame.KEYDOWN:
                if active_id == True:
                    if event.key == pygame.K_BACKSPACE:
                        text_id = text_id[0:-1]
                    else:
                        text_id += event.unicode

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, color, inpur_rect_id, 2)

        # text input location
        test_surface = base_font.render(text_id, True, (255, 255, 255))
        screen.blit(test_surface, (inpur_rect_id.x + 5, inpur_rect_id.y + 5))
        inpur_rect_id.w = max(200, test_surface.get_width() + 10)

        # head line text location // prints
        test_surface = head_font.render("click, enter data and exit", True, (255, 255, 255))
        screen.blit(test_surface, (100, 0))

        test_surface = head_font.render("enter citiys devided by ',' ", True, (255, 255, 255))
        screen.blit(test_surface, (5, 39))

        pygame.display.flip()
        clock.tick(60)

