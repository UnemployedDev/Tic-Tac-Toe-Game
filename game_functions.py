import pygame, sys

def check_events(board, screen, state, label):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			x, y = pygame.mouse.get_pos()

			# 1, 0, 0,
			# 0, 0, 0,
			# 0, 0, 0
			if x > board.screen_rect.left + board.settings.border and x < board.line_position_y and y > board.screen_rect.top + board.settings.border and y < board.line_position_x:
				check_availability(0, board, screen, state, label)

			# 0, 1, 0,
			# 0, 0, 0,
			# 0, 0, 0
			if x > board.line_position_y and x < board.line_position_y * 2 and y > board.screen_rect.top + board.settings.border and y < board.line_position_x:
				check_availability(1, board, screen, state, label)

			# 0, 0, 1,
			# 0, 0, 0,
			# 0, 0, 0
			if x > board.line_position_y * 2 and x < board.screen_rect.right - board.settings.border and y > board.screen_rect.top + board.settings.border and y < board.line_position_x:
				check_availability(2, board, screen, state, label)

			# 0, 0, 0,
			# 1, 0, 0,
			# 0, 0, 0
			if x > board.screen_rect.left + board.settings.border and x < board.line_position_y and y > board.line_position_x and y < board.line_position_x * 2:
				check_availability(3, board, screen, state, label)

			# 0, 0, 0,
			# 0, 1, 0,
			# 0, 0, 0
			if x > board.line_position_y and x < board.line_position_y * 2 and y > board.line_position_x and y < board.line_position_x * 2:
				check_availability(4, board, screen, state, label)

			# 0, 0, 0,
			# 0, 0, 1,
			# 0, 0, 0
			if x > board.line_position_y * 2 and x < board.screen_rect.right - board.settings.border and y > board.line_position_x and y < board.line_position_x * 2:
				check_availability(5, board, screen, state, label)

			# 0, 0, 0,
			# 0, 0, 0,
			# 1, 0, 0
			if x > board.screen_rect.left + board.settings.border and x < board.line_position_y and y > board.line_position_x * 2 and y < board.screen_rect.bottom - board.settings.border:
				check_availability(6, board, screen, state, label)

			# 0, 0, 0,
			# 0, 0, 0,
			# 0, 1, 0
			if x > board.line_position_y and x < board.line_position_y * 2 and y > board.line_position_x * 2 and y < board.screen_rect.bottom - board.settings.border:
				check_availability(7, board, screen, state, label)

			# 0, 0, 0,
			# 0, 0, 0,
			# 0, 0, 1
			if x > board.line_position_y * 2 and x < board.screen_rect.right - board.settings.border and y > board.line_position_x * 2 and y < board.screen_rect.bottom - board.settings.border:
				check_availability(8, board, screen, state, label)

def check_victory(board, screen, game_state, label):

	# O, O, O,
	# 0, 0, 0,
	# 0, 0, 0
	if board.positions[0].turn == 1 and board.positions[0].draw_piece == True and board.positions[1].turn == 1 and board.positions[1].draw_piece == True and board.positions[2].turn == 1 and board.positions[2].draw_piece == True or board.positions[3].turn == 1 and board.positions[3].draw_piece == True and board.positions[4].turn == 1 and board.positions[4].draw_piece == True and board.positions[5].turn == 1 and board.positions[5].draw_piece == True or board.positions[6].turn == 1 and board.positions[6].draw_piece == True and board.positions[7].turn == 1 and board.positions[7].draw_piece == True and board.positions[8].turn == 1 and board.positions[8].draw_piece == True:
		print("O's win")
		game_state.state = 'end_game'
		label.text += 'Player 1 - O'
	# X, X, X,
	# 0, 0, 0,
	# 0, 0, 0
	elif board.positions[0].turn == -1 and board.positions[0].draw_piece == True and board.positions[1].turn == -1 and board.positions[1].draw_piece == True and board.positions[2].turn == -1 and board.positions[2].draw_piece == True or board.positions[3].turn == -1 and board.positions[3].draw_piece == True and board.positions[4].turn == -1 and board.positions[4].draw_piece == True and board.positions[5].turn == -1 and board.positions[5].draw_piece == True or board.positions[6].turn == -1 and board.positions[6].draw_piece == True and board.positions[7].turn == -1 and board.positions[7].draw_piece == True and board.positions[8].turn == -1 and board.positions[8].draw_piece == True:
		print("X's win")
		game_state.state = 'end_game'
		label.text += 'Player 2 - X'
	# O, 0, 0,
	# 0, O, 0,
	# 0, 0, O
	elif board.positions[0].turn == 1 and board.positions[0].draw_piece == True and board.positions[4].turn == 1 and board.positions[4].draw_piece == True and board.positions[8].turn == 1 and board.positions[8].draw_piece == True or board.positions[2].turn == 1 and board.positions[2].draw_piece == True and board.positions[4].turn == 1 and board.positions[4].draw_piece == True and board.positions[6].turn == 1 and board.positions[6].draw_piece == True:
		print("O's win")
		game_state.state = 'end_game'
		label.text += 'Player 1 - O'

	elif board.positions[0].turn == -1 and board.positions[0].draw_piece == True and board.positions[4].turn == -1 and board.positions[4].draw_piece == True and board.positions[8].turn == -1 and board.positions[8].draw_piece == True or board.positions[2].turn == -1 and board.positions[2].draw_piece == True and board.positions[4].turn == -1 and board.positions[4].draw_piece == True and board.positions[6].turn == -1 and board.positions[6].draw_piece == True:
		print("X's win")
		game_state.state = 'end_game'
		label.text += 'Player 2 - X'
	elif board.positions[0].turn == 1 and board.positions[0].draw_piece == True and board.positions[3].turn == 1 and board.positions[3].draw_piece == True and board.positions[6].turn == 1 and board.positions[6].draw_piece == True or board.positions[1].turn == 1 and board.positions[1].draw_piece == True and board.positions[4].turn == 1 and board.positions[4].draw_piece == True and board.positions[7].turn == 1 and board.positions[7].draw_piece == True or board.positions[2].turn == 1 and board.positions[2].draw_piece == True and board.positions[5].turn == 1 and board.positions[5].draw_piece == True and board.positions[8].turn == 1 and board.positions[8].draw_piece == True:
		print("O's win")
		game_state.state = 'end_game'
		label.text += 'Player 1 - O'
	elif board.positions[0].turn == -1 and board.positions[0].draw_piece == True and board.positions[3].turn == -1 and board.positions[3].draw_piece == True and board.positions[6].turn == -1 and board.positions[6].draw_piece == True or board.positions[1].turn == -1 and board.positions[1].draw_piece == True and board.positions[4].turn == -1 and board.positions[4].draw_piece == True and board.positions[7].turn == -1 and board.positions[7].draw_piece == True or board.positions[2].turn == -1 and board.positions[2].draw_piece == True and board.positions[5].turn == -1 and board.positions[5].draw_piece == True and board.positions[8].turn == -1 and board.positions[8].draw_piece == True:
		print("X's win")
		game_state.state = 'end_game'
		label.text += 'Player 2 - X'
	elif board.positions[0].draw_piece and board.positions[1].draw_piece and board.positions[2].draw_piece and board.positions[3].draw_piece and board.positions[4].draw_piece and board.positions[5].draw_piece and board.positions[6].draw_piece and board.positions[7].draw_piece and board.positions[8].draw_piece:
		print('The game is over')
		game_state.state = 'end_game'
		label.text = 'The game is over'

def check_availability(id, board, screen, state, label):
	if board.positions[id].draw_piece == False and board.positions[id].available:
		print('Available')
		# Make the move
		board.positions[id].turn = board.player_turn
		board.positions[id].draw_piece = True
		board.positions[id].available = False
		# Change the turn to the other player
		board.player_turn *= -1
		check_victory(board, screen, state, label)
	else:
		print('Unavailable')

def update_screen(screen, settings, board, pieces):
	screen.fill(settings.bg_color)

	# Drawing Logic Here
	board.draw_board()
	
	for piece in pieces:
		piece.draw()

	pygame.display.flip()