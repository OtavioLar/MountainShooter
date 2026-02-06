
import pygame.image
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_ORANGE, MENU_OPTION, C_WHITE, COLOR_YELLOW


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/MenuBg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer.music.load("./asset/Menu.mp3")
        pygame.mixer.music.play(-1)

        clock = pygame.time.Clock()  # cria o relógio
        delay = 200  # tempo mínimo entre movimentos
        last_move = 0  # armazena o último movimento

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=50, text="Mountain", text_color=COLOR_ORANGE, text_center_pos=((WIN_WIDTH /2),70))
            self.menu_text(text_size=50, text="Shooter", text_color=COLOR_ORANGE, text_center_pos=((WIN_WIDTH /2),120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=COLOR_YELLOW,
                                   text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=C_WHITE, text_center_pos=((WIN_WIDTH /2),200 + 25 * i))

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # close Window
                    quit() # end game
                if event.type == pygame.KEYDOWN:  # somente KEYDOWN tem "key"
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

            keys = pygame.key.get_pressed()
            current_time = pygame.time.get_ticks()

            if keys[pygame.K_DOWN]:
                if current_time - last_move > delay:
                    if menu_option < len(MENU_OPTION) - 1:
                        menu_option += 1
                    else:
                        menu_option = 0
                    last_move = current_time

            if keys[pygame.K_UP]:
                if current_time - last_move > delay:
                    if menu_option > 0:
                        menu_option -= 1
                    else:
                        menu_option = len(MENU_OPTION) - 1
                    last_move = current_time

            pygame.display.flip()
            clock.tick(60)  # 60 FPS

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.Font("./asset/font.ttf", text_size)
        text_surf = text_font.render(text, True, text_color)
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)


