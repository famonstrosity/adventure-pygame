import pygame

from objects import Object, Rock

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
		
		# track number of objects in inventory
		self.numobjects = 0

	def draw_inventory(self):
		# draw inventory
		self.screen.fill(self.inventory_color, self.rect)
	
	def has_object(self):
		# return true if has objects in inventory
		if self.numobjects == 0:
			return False
		else:
			return True
			
