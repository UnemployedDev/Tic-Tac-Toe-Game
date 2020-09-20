import pygame

class Button:
	def __init__(self, screen, width, height, text):
		self.screen = screen
		self.text = text
		self.font = pygame.font.SysFont(None, 50)
		self.screen_rect = screen.get_rect()
		self.rect = pygame.Rect((self.screen_rect.width // 2) - width // 2, (self.screen_rect.height // 2) - height // 2, width, height)
	def draw(self):
		pygame.draw.rect(self.screen, (169,169,169), self.rect)

		screen_text = self.font.render(self.text, True, (0, 0, 0))
		self.screen.blit(screen_text, (self.rect.centerx - 90, self.rect.centery - 15))
