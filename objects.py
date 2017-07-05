import pygame

from map import Map
from settings import Settings

class Object():
	"""object or location"""
	def __init__(self, settings, screen, map, x, y):
		"""initialize object"""
		self.settings = settings
		self.screen = screen
		self.map = map

	def draw_object(self):
		"""draw player at current location"""
		self.screen.blit(self.image, self.rect)
	
	def move_object(self, x, y):
		self.rect.x = x
		self.rect.y = y


class Rock(Object):
	"""rock object"""
	def __init__(self, settings, screen, map, x, y):
		super().__init__(settings, screen, map, x, y)
		self.image_path = "images/rock.png"
		self.scale = (50, 50)
		self.map_rect = map.rect
		
		# load object image, get rect
		original_image = pygame.image.load(self.image_path)
		self.image = pygame.transform.scale(original_image, self.scale)
		self.rect = self.image.get_rect()

		# place object at certain location
		self.rect.x = x
		self.rect.y = y
		
		# indicates if you can pick up this object
		self.can_take = True


class House(Object):
	"""house location"""
	def __init__(self, settings, screen, map, x, y):
		super().__init__(settings, screen, map, x, y)
		self.image_path = "images/house.png"
		self.scale = (70, 70)
		self.map_rect = map.rect
		
		# load object image, get rect
		original_image = pygame.image.load(self.image_path)
		self.image = pygame.transform.scale(original_image, self.scale)
		self.rect = self.image.get_rect()

		# place object at certain location
		self.rect.x = x
		self.rect.y = y

		# indicates if you can pick up this object
		self.can_take = False
