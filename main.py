import pygame
from settings import Settings
from board import Board
from piece import Piece
from game_state import GameState
from button import Button
from label import Label

class Game:
	def __init__(self):
		pygame.init()
		pygame.font.init()

		self.running = True
		self.screen = None
		self.settings = Settings() 
		self.game_state = GameState()

		self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
		pygame.display.set_caption(self.settings.caption)

		self.button = Button(self.screen, 300, 100, 'Start Game')
		self.board = Board(self.screen, self.settings)

		self.label = Label(self.screen, "The winner is ", self.screen.get_rect().width // 2, self.screen.get_rect().height // 2)
		self.button2 = Button(self.screen, 300, 100, 'Restart')
		#self.piece = Piece(self.board, 8)


	def run_game(self):
		while True:
			self.game_state.state_manager(self.screen, self.board, self.settings, self.button, self.game_state, self.label, self.button2)
			#self.game_state.main_game(self.screen, self.board, self.settings)
			


if __name__ == '__main__':
	game = Game()
	game.run_game()