import pygame

class TextBox():

	def __init__(self, settings, screen):
		"""initialize text box attributes"""
		self.settings = settings
		self.screen = screen
		
		# set text box dimensions
		self.height = settings.text_height
		self.width = settings.text_width
		# set text box location on screen
		self.x = settings.text_x
		self.y = settings.text_y
		# set text box color
		self.textbox_color = settings.textbox_color
		
		# make text box rect
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
	
	def draw_text_box(self):
		# draw text box
		self.screen.fill(self.textbox_color, self.rect)
	
	def get_rect(self):
		return self.rect
