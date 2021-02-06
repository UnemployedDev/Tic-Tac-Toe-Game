import pygame

class Button:

	def __init__(self, screen, width, height, text="", font=None, color=(169, 169, 169)):
		self.screen = screen
		self.text = text
		self.font = pygame.font.SysFont(font, 50)
		self.color = color
		self.screen_rect = screen.get_rect()
		self.rect = pygame.Rect((self.screen_rect.width // 2) - width // 2, (self.screen_rect.height // 2) - height // 2, width, height)
	
	def on_mouse_click(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			x, y = pygame.mouse.get_pos()
			if x > self.rect.left and x < self.rect.right and y > self.rect.top and y < self.rect.bottom:
				return True

	def draw(self):
		pygame.draw.rect(self.screen, self.color, self.rect)

		screen_text = self.font.render(self.text, True, (0, 0, 0))
		self.screen.blit(screen_text, (self.rect.centerx - 90, self.rect.centery - 15))
