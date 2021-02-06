import pygame
from settings import Settings
from game_state import GameState

class Game:
	def __init__(self):
		pygame.init()
		pygame.font.init()

		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
		pygame.display.set_caption(self.settings.caption)
		self.game_state = GameState(self.screen, self.settings)

	def run_game(self):
		while True:
			self.game_state.state_manager()
			

if __name__ == '__main__':
	game = Game()
	game.run_game()