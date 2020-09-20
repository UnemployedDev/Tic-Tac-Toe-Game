import pygame, sys

class Engine:
	def __init__(self, screen, settings, board, label, pieces):
		self.screen = screen
		self.settings = settings
		self.board = board
		self.label = label
		self.pieces = pieces

	def check_events(self):
		for event in pygame.event.get():
			self.on_close(event)
			if event.type == pygame.MOUSEBUTTONDOWN:
				x, y = pygame.mouse.get_pos()

				# Collision of the first square
				if x > self.board.screen_rect.left + self.settings.border and x < self.board.line_position_y and y > self.board.screen_rect.top + self.settings.border and y < self.board.line_position_x:
					self.check_availability(0)
				
				# Collision of the second square
				if x > self.board.line_position_y and x < self.board.line_position_y * 2 and y > self.board.screen_rect.top + self.settings.border and y < self.board.line_position_x:
					self.check_availability(1)

				# Collision of the third square
				if x > self.board.line_position_y * 2 and x < self.board.screen_rect.right - self.settings.border and y > self.board.screen_rect.top + self.settings.border and y < self.board.line_position_x:
					self.check_availability(2)

				# Collision of the forth square
				if x > self.board.screen_rect.left + self.settings.border and x < self.board.line_position_y and y > self.board.line_position_x and y < self.board.line_position_x * 2:
					self.check_availability(3)

				# Collision of the fifth square
				if x > self.board.line_position_y and x < self.board.line_position_y * 2 and y > self.board.line_position_x and y < self.board.line_position_x * 2:
					self.check_availability(4)

				# Collision of the sixth square
				if x > self.board.line_position_y * 2 and x < self.board.screen_rect.right - self.settings.border and y > self.board.line_position_x and y < self.board.line_position_x * 2:
					self.check_availability(5)

				# Collision of the seventh square
				if x > self.board.screen_rect.left + self.settings.border and x < self.board.line_position_y and y > self.board.line_position_x * 2 and y < self.board.screen_rect.bottom - self.settings.border:
					self.check_availability(6)

				# Collision of the eighth square
				if x > self.board.line_position_y and x < self.board.line_position_y * 2 and y > self.board.line_position_x * 2 and y < self.board.screen_rect.bottom - self.settings.border:
					self.check_availability(7)

				# Collision of the nineth square
				if x > self.board.line_position_y * 2 and x < self.board.screen_rect.right - self.settings.border and y > self.board.line_position_x * 2 and y < self.board.screen_rect.bottom - self.settings.border:
					self.check_availability(8)

	def check_victory(self):

		# Check victory for a line of O
		if self.board.positions[0].turn == 1 and self.board.positions[0].draw_piece == True and self.board.positions[1].turn == 1 and self.board.positions[1].draw_piece == True and self.board.positions[2].turn == 1 and self.board.positions[2].draw_piece == True or self.board.positions[3].turn == 1 and self.board.positions[3].draw_piece == True and self.board.positions[4].turn == 1 and self.board.positions[4].draw_piece == True and self.board.positions[5].turn == 1 and self.board.positions[5].draw_piece == True or self.board.positions[6].turn == 1 and self.board.positions[6].draw_piece == True and self.board.positions[7].turn == 1 and self.board.positions[7].draw_piece == True and self.board.positions[8].turn == 1 and self.board.positions[8].draw_piece == True:
			self.settings.state = 'end_game'
			self.label.text += 'Player 1 - O'
		
		# Check victory for a line of X
		elif self.board.positions[0].turn == -1 and self.board.positions[0].draw_piece == True and self.board.positions[1].turn == -1 and self.board.positions[1].draw_piece == True and self.board.positions[2].turn == -1 and self.board.positions[2].draw_piece == True or self.board.positions[3].turn == -1 and self.board.positions[3].draw_piece == True and self.board.positions[4].turn == -1 and self.board.positions[4].draw_piece == True and self.board.positions[5].turn == -1 and self.board.positions[5].draw_piece == True or self.board.positions[6].turn == -1 and self.board.positions[6].draw_piece == True and self.board.positions[7].turn == -1 and self.board.positions[7].draw_piece == True and self.board.positions[8].turn == -1 and self.board.positions[8].draw_piece == True:
			self.settings.state = 'end_game'
			self.label.text += 'Player 2 - X'
		
		# Check victory for a diagonal of O
		elif self.board.positions[0].turn == 1 and self.board.positions[0].draw_piece == True and self.board.positions[4].turn == 1 and self.board.positions[4].draw_piece == True and self.board.positions[8].turn == 1 and self.board.positions[8].draw_piece == True or self.board.positions[2].turn == 1 and self.board.positions[2].draw_piece == True and self.board.positions[4].turn == 1 and self.board.positions[4].draw_piece == True and self.board.positions[6].turn == 1 and self.board.positions[6].draw_piece == True:
			self.settings.state = 'end_game'
			self.label.text += 'Player 1 - O'

		# Check victory for a diagonal of X
		elif self.board.positions[0].turn == -1 and self.board.positions[0].draw_piece == True and self.board.positions[4].turn == -1 and self.board.positions[4].draw_piece == True and self.board.positions[8].turn == -1 and self.board.positions[8].draw_piece == True or self.board.positions[2].turn == -1 and self.board.positions[2].draw_piece == True and self.board.positions[4].turn == -1 and self.board.positions[4].draw_piece == True and self.board.positions[6].turn == -1 and self.board.positions[6].draw_piece == True:
			self.settings.state = 'end_game'
			self.label.text += 'Player 2 - X'
		elif self.board.positions[0].turn == 1 and self.board.positions[0].draw_piece == True and self.board.positions[3].turn == 1 and self.board.positions[3].draw_piece == True and self.board.positions[6].turn == 1 and self.board.positions[6].draw_piece == True or self.board.positions[1].turn == 1 and self.board.positions[1].draw_piece == True and self.board.positions[4].turn == 1 and self.board.positions[4].draw_piece == True and self.board.positions[7].turn == 1 and self.board.positions[7].draw_piece == True or self.board.positions[2].turn == 1 and self.board.positions[2].draw_piece == True and self.board.positions[5].turn == 1 and self.board.positions[5].draw_piece == True and self.board.positions[8].turn == 1 and self.board.positions[8].draw_piece == True:
			self.settings.state = 'end_game'
			self.label.text += 'Player 1 - O'
		elif self.board.positions[0].turn == -1 and self.board.positions[0].draw_piece == True and self.board.positions[3].turn == -1 and self.board.positions[3].draw_piece == True and self.board.positions[6].turn == -1 and self.board.positions[6].draw_piece == True or self.board.positions[1].turn == -1 and self.board.positions[1].draw_piece == True and self.board.positions[4].turn == -1 and self.board.positions[4].draw_piece == True and self.board.positions[7].turn == -1 and self.board.positions[7].draw_piece == True or self.board.positions[2].turn == -1 and self.board.positions[2].draw_piece == True and self.board.positions[5].turn == -1 and self.board.positions[5].draw_piece == True and self.board.positions[8].turn == -1 and self.board.positions[8].draw_piece == True:
			self.settings.state = 'end_game'
			self.label.text += 'Player 2 - X'
		elif self.board.positions[0].draw_piece and self.board.positions[1].draw_piece and self.board.positions[2].draw_piece and self.board.positions[3].draw_piece and self.board.positions[4].draw_piece and self.board.positions[5].draw_piece and self.board.positions[6].draw_piece and self.board.positions[7].draw_piece and self.board.positions[8].draw_piece:
			self.settings.state = 'end_game'
			self.label.text = 'The game is over'

	def check_availability(self, id):
		if self.board.positions[id].draw_piece == False and self.board.positions[id].available:
			# Make the move
			self.board.positions[id].turn = self.board.player_turn
			self.board.positions[id].draw_piece = True
			self.board.positions[id].available = False
			# Change the turn to the other player
			self.board.player_turn *= -1
			self.check_victory()
		else:
			print('Unavailable')

	def update_screen(self):
		self.screen.fill(self.settings.bg_color)
		self.board.draw_board()
		
		for piece in self.pieces:
			piece.draw()

		pygame.display.flip()

	def on_close(self, event):
		if event.type == pygame.QUIT:
			sys.exit()