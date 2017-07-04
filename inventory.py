import pygame

class Inventory():

	def __init__(self, settings, screen):
		"""initialize inventory attributes"""
		self.settings = settings
		self.screen = screen
		
		# set inventory dimensions
		self.height = settings.inventory_height
		self.width = settings.inventory_width
		# set inventory location on screen
		self.x = settings.inventory_x
		self.y = settings.inventory_y
		# set inventory color
		self.inventory_color = settings.inventory_color
		
		# make inventory rect
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

	def draw_inventory(self):
		# draw inventory
		self.screen.fill(self.inventory_color, self.rect)
