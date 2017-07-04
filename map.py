import pygame

class Map():

	def __init__(self, settings, screen):
		"""initialize map attributes"""
		self.settings = settings
		self.screen = screen
		
		# set map dimensions
		self.height = settings.map_height
		self.width = settings.map_width
		# set map location on screen
		self.x = settings.map_x
		self.y = settings.map_y
		# set map color
		self.map_color = settings.map_color
		
		# make map rect
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

	def draw_map(self):
		# draw map
		self.screen.fill(self.map_color, self.rect)
