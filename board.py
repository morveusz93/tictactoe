import pygame


class Board:
    def __init__(self, width):
        self.width = width
        self.screen_size = (self.width, self.width)
        # colors:
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.blue = (0, 0, 255)
        self.green = (0, 255, 0)
        self.img_size = (self.width//3-4, self.width//3-4)
        self.ximg = pygame.transform.scale(pygame.image.load('img/x-img.png'), self.img_size)
        self.oimg = pygame.transform.scale(pygame.image.load('img/o-img.png'), self.img_size)
        self.pre_ximg = pygame.transform.scale(pygame.image.load('img/pre-x-img.png'), self.img_size)
        self.pre_oimg = pygame.transform.scale(pygame.image.load('img/pre-x-img.png'), self.img_size)

        pygame.font.init()
        self.myfont = pygame.font.SysFont('arial', 30)

        self.screen = pygame.display.set_mode(self.screen_size)
        self.screen.fill(self.black)
        pygame.display.set_caption("TicTacToe by Morvy")
        self.game = [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]
        self.round = 1

    def draw_grid(self):
        for i in range(1, 3):
            for j in range(1, 3):
                pygame.draw.line(self.screen, self.white, (self.width / 3 * i, 0), (self.width / 3 * i, self.width))
                pygame.draw.line(self.screen, self.white, (0, self.width / 3 * j), (self.width, self.width / 3 * j))

    def draw(self):
        self.draw_grid()
        self.draw_circles()
        pygame.display.flip()

    def draw_circles(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.game[i][j] == 1:
                    self.screen.blit(self.ximg, (2 + self.width // 3 * j, 2 + self.width // 3 * i))
                elif self.game[i][j] == 2:
                    self.screen.blit(self.oimg, (2 + self.width // 3 * j, 2 + self.width // 3 * i))

    def save_the_move(self, x, y):
        if self.game[x][y] == 0:
            if self.round == 1:
                self.game[x][y] = 1
                self.round = 2
            elif self.round == 2:
                self.game[x][y] = 2
                self.round = 1

    def winner_check(self):
        for i in range(0, 3):
            row = {self.game[i][0], self.game[i][1], self.game[i][2]}
            if len(row) == 1 and self.game[i][0] != 0:
                return self.game[i][0]
        for i in range(0, 3):
            column = {self.game[0][i], self.game[1][i], self.game[2][i]}
            if len(column) == 1 and self.game[0][i] != 0:
                return self.game[0][i]
        diagonal1 = {self.game[0][0], self.game[1][1], self.game[2][2]}
        diagonal2 = {self.game[0][2], self.game[1][1], self.game[2][0]}
        if len(diagonal1) == 1 and self.game[1][1] != 0 or len(diagonal2) == 1 and self.game[1][1] != 0:
            return self.game[1][1]
        if 0 not in self.game[1] and 0 not in self.game[2] and 0 not in self.game[0]:
            return "tie"
