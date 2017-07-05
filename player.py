import pygame

from map import Map
from settings import Settings

class Player():
	
	def __init__(self, settings, screen, map):
		"""initialize player"""
		self.settings = settings
		self.screen = screen
		self.map = map
		
		# load player image, get rect
		original_image = pygame.image.load("images/player.png")
		self.image = pygame.transform.scale(original_image,
									self.settings.player_dimensions)
		self.rect = self.image.get_rect()
		self.map_rect = map.rect

		# start player in center of map
		self.rect.centerx = self.map_rect.centerx
		self.rect.centery = self.map_rect.centery
		
		#  player movement flags
		self.moving_up = False
		self.moving_down = False
		self.moving_left = False
		self.moving_right = False
	
	def draw_player(self):
		"""draw player at current location"""
		self.screen.blit(self.image, self.rect)
	
	def update(self):
		"""update player position based on movement flag"""
		if self.moving_up and self.rect.top > self.map_rect.top:
			self.rect.centery -= 1
		if self.moving_down and self.rect.bottom < self.map_rect.bottom:
			self.rect.centery += 1
		if self.moving_left and self.rect.left > self.map_rect.left:
			self.rect.centerx -= 1
		if self.moving_right and self.rect.right < self.map_rect.right:
			self.rect.centerx += 1
	

