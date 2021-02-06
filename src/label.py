import pygame

class Label:
	def __init__(self, screen, text, xpos, ypos):
		self.screen = screen
		self.xpos = xpos
		self.ypos = ypos
		self.font = pygame.font.SysFont(None, 50)
		self.text = text

	def draw(self):
		screen_text = self.font.render(self.text, True, (0, 0, 0))
		self.screen.blit(screen_text, (self.xpos - 120, self.ypos - 100))