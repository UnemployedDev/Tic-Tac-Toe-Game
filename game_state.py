import pygame
import game_functions as gf
import sys

class GameState:
	def __init__(self):
		self.state = 'intro'
		self.winner = ''

	def main_game(self, screen, board, settings, state, label):
		gf.check_events(board, screen, state, label)
		gf.update_screen(screen, settings, board, board.positions)

	def intro(self, screen, settings, button):
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				x, y = pygame.mouse.get_pos()
				if x > button.rect.left and x < button.rect.right and y > button.rect.top and y < button.rect.bottom:
					self.state = 'main_game'

		screen.fill(settings.bg_color)
		button.draw()
		pygame.display.flip()

	def end_game(self, screen, settings, label, button2, board):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				x, y = pygame.mouse.get_pos()
				if x > button2.rect.left and x < button2.rect.right and y > button2.rect.top and y < button2.rect.bottom:
					self.reset_all_states(board)
					self.state = 'main_game'

		screen.fill(settings.bg_color)
		label.draw()
		button2.draw()
		pygame.display.flip()

	def reset_all_states(self, board):
		for piece in board.positions:
			piece.reset()

	def state_manager(self, screen, board, settings, button, state, label, button2):
		if self.state == 'intro':
			self.intro(screen, settings, button)
		if self.state == 'main_game':
			self.main_game(screen, board, settings, state, label)
		if self.state == 'end_game':
			self.end_game(screen, settings, label, button2, board)
