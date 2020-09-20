import pygame
from piece import Piece

class Board:
	def __init__(self, screen, settings):
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.settings = settings
		self.line_position_y = self.settings.width // 3
		self.line_position_x = self.settings.height // 3
		self.player_turn = 1

		self.positions = [
			Piece(self, 0, self.player_turn),
			Piece(self, 1, self.player_turn),
			Piece(self, 2, self.player_turn),
			Piece(self, 3, self.player_turn),
			Piece(self, 4, self.player_turn),
			Piece(self, 5, self.player_turn),
			Piece(self, 6, self.player_turn),
			Piece(self, 7, self.player_turn),
			Piece(self, 8, self.player_turn)
		]

	def draw_board(self):
		# Create the vertical lines
		pygame.draw.line(self.screen, self.settings.line_color, 
			(self.line_position_y, self.screen_rect.top + self.settings.border), 
			(self.line_position_y, self.screen_rect.bottom - self.settings.border), 
			self.settings.line_width)

		pygame.draw.line(self.screen, self.settings.line_color, 
			(self.line_position_y * 2, self.screen_rect.top + self.settings.border), 
			(self.line_position_y * 2, self.screen_rect.bottom - self.settings.border), 
			self.settings.line_width)

		# Create the horizontal line
		pygame.draw.line(self.screen, self.settings.line_color, 
			(self.screen_rect.left + self.settings.border, self.line_position_x), 
			(self.screen_rect.right - self.settings.border, self.line_position_x), 
			self.settings.line_width)
		
		pygame.draw.line(self.screen, self.settings.line_color, 
			(self.screen_rect.left + self.settings.border, self.line_position_x * 2), 
			(self.screen_rect.right - self.settings.border, self.line_position_x * 2), 
			self.settings.line_width)


	def draw_o(self, centerx, centery):
		pygame.draw.circle(self.screen, self.settings.line_color, (centerx, centery), 70, 15)

	def draw_x(self):
		pass

	def draw_o_x(self):
		pass
