import pygame, sys
from engine import Engine
from board import Board
from piece import Piece
from button import Button
from label import Label

class GameState:
	def __init__(self, screen, settings):
		self.screen = screen
		self.settings = settings 
		self.board = Board(self.screen, self.settings)
		self.button = Button(self.screen, 300, 100, 'Start Game')
		self.state = self.settings.state
		self.label = Label(self.screen, "The winner is ", self.screen.get_rect().width // 2, self.screen.get_rect().height // 2)
		self.button2 = Button(self.screen, 300, 100, 'Restart')
		self.winner = ''
		self.engine = Engine(self.screen, self.settings, self.board, self.label, self.board.positions)

	def main_game(self):
		self.engine.check_events()
		self.engine.update_screen()

	def intro(self):
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT:
				sys.exit()

			if self.button.on_mouse_click(event):
				self.settings.state = 'main_game'

		self.screen.fill(self.settings.bg_color)
		self.button.draw()
		pygame.display.flip()

	def end_game(self):
		for event in pygame.event.get():
			self.engine.on_close(event)
			if self.button2.on_mouse_click(event):
				self.reset_all_states()
				self.settings.state = 'main_game'

		self.screen.fill(self.settings.bg_color)
		self.label.draw()
		self.button2.draw()
		pygame.display.flip()

	def reset_all_states(self):
		for piece in self.board.positions:
			piece.reset()

	def state_manager(self):
		if self.settings.state == 'intro':
			self.intro()
		if self.settings.state == 'main_game':
			self.main_game()
		if self.settings.state == 'end_game':
			self.end_game()
