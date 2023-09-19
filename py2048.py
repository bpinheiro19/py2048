import pygame
from pygame.locals import *
from random import randrange


class App:
    def __init__(self):
        self.running = True
        self.screen = None
        self.clock = pygame.time.Clock()
        self.width, self.height = 800, 800
        self.board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.screen_color = pygame.Color(207, 195, 176)

    def start_game(self):
        self.on_init()
        self.spawn_tile()
        self.draw_board()
        self.main_loop()
        self.on_cleanup()

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.height, self.width))
        self.screen.fill(self.screen_color)

    def on_cleanup(self):
        pygame.quit()

    def draw_board(self):
        pass

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            self.move_up()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            self.move_down()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            self.move_left()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            self.move_right()

    def update(self):
        pass

    def render(self):
        pass

    def spawn_tile(self):
        pass

    def main_loop(self):
        while self.running:
            for event in pygame.event.get():
                self.on_event(event)

            self.update()
            self.render()

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    theApp = App()
    theApp.start_game()
