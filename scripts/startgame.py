import pygame
from scripts.settings import *
from scripts.scene import Scene
from scripts.menu import Menu
from scripts.game import Game
from scripts.gameover import GameOver

class StartGame:

    def __init__(self):
        # padrão iniciar font, sound, video
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        self.display = pygame.display.set_mode([WIDTH, HEIGHT])
        self.campo_img = pygame.image.load("assets/bg.png")
        self.campo = campo_img.get_rect()

        player1_img = pygame.image.load("assets/player1.png")
        player1 = player1_img.get_rect()

        player2_img = pygame.image.load("assets/player2.png")
        player2 = player1_img.get_rect(right=WIDTH)

        player1_velocidade = 6
        player1_score = 0
        player2_score = 0

        ball_img = pygame.image.load("assets/ball.png")
        ball = ball_img.get_rect(center=[WIDTH / 2, HEIGHT / 2])

        ball_dir_x = 6
        ball_dir_y = 6

        font = pygame.font.Font(None, 50)
        placar_player1 = font.render(str(player1_score), True, "white")
        placar_player2 = font.render(str(player2_score), True, "white")

        menu_img = pygame.image.load("assets/menu.png")
        menu = menu_img.get_rect()

        gameover_img = pygame.image.load("assets/gameover.png")
        gameover = gameover_img.get_rect()

        fade_img = pygame.Surface((1280, 720)).convert_alpha()
        fade = fade_img.get_rect()
        self.fade_img.fill("black")
        fade_alpha = 255

        music = pygame.mixer.Sound("assets/music.ogg")
        music.play(-1)
        # loop do game

        self.scene = "menu"
        loop = True
        fps = pygame.time.Clock()

        self.current_scene = Menu()

    def run(self):

        while True:

            if self.scene == "menu" and self.current_scene.active == False:

                self.scene = "game"
                self.current_scene = Game()

                self.display.fill((0, 0, 0))
                self.display.blit(menu_img, menu)
                self.display.blit(fade_img, fade)

            elif self.scene == "game" and self.current_scene.active == False:
                self.scene = "gameover"
                self.current_scene = GameOver()

                self.display.fill((0, 0, 0))
                self.display.blit(campo_img, campo)
                self.display.blit(player1_img, player1)
                self.display.blit(player2_img, player2)
                self.display.blit(ball_img, ball)
                self.display.blit(placar_player1, (500, 50))
                self.display.blit(placar_player2, (780, 50))

            elif self.scene == "gameover" and self.current_scene.active == False:
                self.scene = "menu"
                self.current_scene = Menu()

                self.display.fill((0, 0, 0))
                self.display.blit(gameover_img, gameover)
                self.display.blit(fade_img, fade)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                self.current_scene.events(event)

            self.display.fill("black")
            self.current_scene.draw()
            self.current_scene.update()
            pygame.display.flip()
