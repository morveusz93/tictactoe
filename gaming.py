import pygame
import board

class Gaming:
    def __init__(self):
        pygame.init()
        self.board = board.Board(600)

    def get_coords(self, z):
        if z in range(0, self.board.width//3):
            return 0
        elif z in range(self.board.width//3, self.board.width//3*2):
            return 1
        else:
            return 2

    def check_win(self):
        winner_check = self.board.winner_check()
        if winner_check == 1:
            self.board.draw_game_over(1)
            pygame.time.wait(1000)
        elif winner_check == 2:
            self.board.draw_game_over(2)
            pygame.time.wait(1000)
        elif winner_check == 'tie':
            self.board.draw_game_over(0)
            pygame.time.wait(1000)


    def run_game(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise SystemExit
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    y, x = event.pos
                    self.board.save_the_move(self.get_coords(x), self.get_coords(y))

            self.board.draw()
            self.check_win()
