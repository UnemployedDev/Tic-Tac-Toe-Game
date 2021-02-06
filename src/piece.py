import pygame

class Piece:
	def __init__(self, board, p_id, turn):

		self.width = (board.line_position_y) - (board.screen_rect.left + board.settings.border)
		self.height = (board.line_position_x) - (board.screen_rect.top + board.settings.border)
		self.p_id = p_id
		self.turn = turn
		self.draw_piece = False
		self.available = True
		self.top = 0
		self.left = 0
		self.board = board

		if p_id in range(0,3):
			self.top = board.screen_rect.top + board.settings.border
		if p_id in range(3, 6):
			self.top = board.line_position_x + 11
		if p_id in range(6, 9):
			self.top = board.line_position_x * 2
		if p_id == 0 or p_id == 3 or p_id == 6:
			self.left = board.screen_rect.left + board.settings.border
		if p_id == 1 or p_id == 4 or p_id == 7:
			self.left = board.line_position_y + 11
		if p_id == 2 or p_id == 5 or p_id == 8:
			self.left = board.line_position_y * 2

		self.rect = pygame.Rect(self.left, self.top, self.width, self.height)

	def reset(self):
		self.width = (self.board.line_position_y) - (self.board.screen_rect.left + self.board.settings.border)
		self.height = (self.board.line_position_x) - (self.board.screen_rect.top + self.board.settings.border)
		self.p_id = self.p_id
		self.turn = self.turn
		self.draw_piece = False
		self.available = True
		self.top = 0
		self.left = 0
		self.board = self.board

	def draw(self):
		pygame.draw.rect(self.board.screen, (255, 255, 255, 0), self.rect)

		if self.draw_piece:
			if self.turn == 1:
				pygame.draw.circle(self.board.screen, (0, 0, 0), (self.rect.centerx, self.rect.centery), self.rect.right - self.rect.centerx - 70, 10)
			if self.turn == -1:
				pygame.draw.line(self.board.screen, (0, 0, 0), (self.rect.left + 70, self.rect.top + 20), (self.rect.right - 70, self.rect.bottom - 20), 10)
				pygame.draw.line(self.board.screen, (0, 0, 0), (self.rect.left + 70, self.rect.bottom - 20), (self.rect.right - 70, self.rect.top + 20), 10)