import pygame
import colors
from pygame.locals import *
from random import randrange

class App:
    def __init__(self):
        self.running = True
        self.screen = None
        self.clock = pygame.time.Clock()
        self.width, self.height = 800, 800
        self.board = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]

    def start_game(self):
        self.on_init()
        self.spawn_piece()
        self.draw_board()
        self.main_loop()
        self.on_cleanup()

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.height, self.width))
        self.screen.fill(colors.BACKGROUND_COLOR)

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

        self.draw_numbers_on_board()

    def draw_numbers_on_board(self):
        for col in range(4):
            for row in range(4):

                val = self.board[col][row]

                if val != 0:
                    x = row * 150 + 145
                    y = col * 150 + 145
                    
                    rect = pygame.Rect(x-43, y-43, 147, 147)
                    if val == 2:
                        pygame.draw.rect(self.screen, colors.COLOR2, rect)
                        x+=17
                    if val == 4:
                        pygame.draw.rect(self.screen, colors.COLOR4, rect)
                        x+=17
                    if val == 8:
                        pygame.draw.rect(self.screen, colors.COLOR8, rect)
                        x+=17
                    if val == 16:
                        pygame.draw.rect(self.screen, colors.COLOR16, rect)
                    if val == 32:
                        pygame.draw.rect(self.screen, colors.COLOR32, rect)
                    if val == 64:
                        pygame.draw.rect(self.screen, colors.COLOR64, rect)
                    if val == 128:
                        pygame.draw.rect(self.screen, colors.COLOR128, rect)
                        x-=15
                    if val == 256:
                        pygame.draw.rect(self.screen, colors.COLOR256, rect)  
                        x-=15
                    if val == 512:
                        pygame.draw.rect(self.screen, colors.COLOR512, rect)
                        x-=15
                    if val == 1024:
                        pygame.draw.rect(self.screen, colors.COLOR1024, rect)
                        x-=30
                    if val == 2048:
                        pygame.draw.rect(self.screen, colors.COLOR2048, rect)
                        x-=30
                    
                    font = pygame.font.SysFont('arial', 55, False, False)
                    text = font.render(str(val), True, (0, 0, 0))
                    self.screen.blit(text, (x, y))

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            self.move_up()
            self.update()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            self.move_down()
            self.update()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            self.move_left()
            self.update()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:  
            self.move_right()
            self.update()

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
        if self.check_game_over():
            print("GameOver!!")
            
        else:        
            self.spawn_piece()
            self.print_board()
            self.render() 

    def check_game_over(self):
        pass

    def render(self):
        self.screen.fill(colors.BACKGROUND_COLOR)
        self.draw_board()

    def spawn_piece(self):
        valid = False
        
        while not valid:
            x = randrange(4)
            y = randrange(4)

            spawn_value = 2 if randrange(10) < 9 else 4

            if self.board[x][y] == 0:
                valid = True
                self.board[x][y] = spawn_value

    def print_board(self):
        for row in range(4):
            print(self.board[row])

    def main_loop(self):

        while( self.running ):
            
            for event in pygame.event.get():
                self.on_event(event)

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    theApp = App()
    theApp.start_game()
