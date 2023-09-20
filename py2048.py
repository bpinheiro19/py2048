import pygame
from pygame.locals import *
from random import randrange


class App:
    def __init__(self):
        self.running = True
        self.screen = None
        self.clock = pygame.time.Clock()
        self.width, self.height = 800, 800
        self.board = [[2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
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
        x,y = 100,100
        for i in range (3):
            x += 150##height / 4
            y += 150##width / 4
            pygame.draw.line(self.screen, (0,0,0), (x,100), (x, self.height-100), width=3)
            pygame.draw.line(self.screen, (0,0,0), (100,y), (self.width-100, y), width=3)

        pygame.draw.line(self.screen, (0,0,0), (100,100), (100, self.height-100), width=3)
        pygame.draw.line(self.screen, (0,0,0), (100,self.height-100), (self.width-100, self.height-100), width=3)
        pygame.draw.line(self.screen, (0,0,0), (self.width-100, self.height-100), (self.width-100, 100), width=3)
        pygame.draw.line(self.screen, (0,0,0), (100,100), (self.width-100, 100), width=3)

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

    def move_up(self):
        for col in range(4):
            row = 0
            while row < 4:
                current = self.board[row][col]
                if current != 0 and row-1 >= 0:
                    if not self.piece_has_value(row-1, col):
                        self.move_piece(row, col, row-1, col)
                        row-=2
                    else:
                        if self.board[row][col] == self.board[row-1][col]:
                            self.board[row-1][col] = 2 * self.board[row][col]
                            self.board[row][col] = 0
                row+=1   
    
    def move_down(self):
        for col in range(4):
            row = 3
            while row >= 0:
                current = self.board[row][col]
                if current != 0 and row+1 < 4:
                    if not self.piece_has_value(row+1, col):
                        self.move_piece(row, col, row+1, col)
                        row+=2
                    else:
                        if self.board[row][col] == self.board[row+1][col]:
                            self.board[row+1][col] = 2 * self.board[row][col]
                            self.board[row][col] = 0
                row-=1             
 
    def move_left(self):
        for row in range(4):
            col = 0
            while col < 4:
                current = self.board[row][col]
                if current != 0 and col-1 >= 0:
                    if not self.piece_has_value(row, col-1):
                        self.move_piece(row, col, row, col-1)
                        col-=2
                    else:
                        if self.board[row][col] == self.board[row][col-1]:
                            self.board[row][col-1] = 2 * self.board[row][col]
                            self.board[row][col] = 0
                col+=1

    def move_right(self):
        for row in range(4):
            col = 3
            while col >= 0:
                current = self.board[row][col]
                if current != 0 and col+1 < 4:
                    if not self.piece_has_value(row, col+1):
                        self.move_piece(row, col, row, col+1)
                        col+=2
                    else:
                        if self.board[row][col] == self.board[row][col+1]:
                            self.board[row][col+1] = 2 * self.board[row][col]
                            self.board[row][col] = 0
                col-=1  

    def piece_has_value(self, x, y):
        return self.board[x][y] != 0
    
    def move_piece(self, x, y, z, w):
        val = self.board[x][y]
        self.board[x][y] = 0
        self.board[z][w] = val

    def update(self):
        pass

    def render(self):
        pass

    def spawn_tile(self):
        pass

    def print_board(self):
        for row in range(4):
            print(self.board[row])

    def main_loop(self):
        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
                self.print_board()

            self.update()
            self.render()

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    theApp = App()
    theApp.start_game()
