import sys
import pygame

from settings import Settings
from map import Map
from player import Player

mode = 1 #initialize in map mode

def check_events(settings, player, objects):
	"""respond to keypress and mouse events"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown(event, settings, player, objects)
		elif event.type == pygame.KEYUP:
			check_keyup(event, settings, player)


def check_keydown(event, settings, player, objects):
	"""respond to keydown events"""
	if settings.mode == 1: #map
		if event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_i:
			#inventory mode
			mode = 3
		elif event.key == pygame.K_RETURN:
			#interact with object if player rect collides w object rect
			check_interactions(player, objects)
			#text mode
			mode = 2
		elif event.key == pygame.K_UP:
			player.moving_up = True
		elif event.key == pygame.K_DOWN:
			player.moving_down = True
		elif event.key == pygame.K_LEFT:
			player.moving_left = True
		elif event.key == pygame.K_RIGHT:
			player.moving_right = True
	elif mode == 2: #text
		if event.key == pygame.K_UP:
			#move text select up
			mode = 1
		elif event.key == pygame.K_DOWN:
			#move text select down
			mode = 1
		elif event.key == pygame.K_RETURN:
			#select text
			#show text if necessary
			#return to map mode
			mode = 1
	elif mode == 3: #inventory
		if event.key == pygame.K_LEFT:
			#move inventory select left
			mode = 1
		elif event.key == pygame.K_RIGHT:
			#move inventory select right
			mode = 1
		elif event.key == pygame.K_RETURN:
			#select item
			#show item info
			#return to map mode
			mode = 1

def check_keyup(event, settings, player):
	"""respond to keyup events"""
	if settings.mode == 1: #map
		if event.key == pygame.K_UP:
			player.moving_up = False
		elif event.key == pygame.K_DOWN:
			player.moving_down = False
		elif event.key == pygame.K_LEFT:
			player.moving_left = False
		elif event.key == pygame.K_RIGHT:
			player.moving_right = False

def update_screen(settings, screen, map, player, objects, text_box, inventory):
	screen.fill((0, 0, 0))
	map.draw_map()
	for object in objects:
		object.draw_object()
	player.draw_player()
	inventory.draw_inventory()
	text_box.draw_text_box()
	pygame.display.flip()

def get_mode():
	return settings.mode
	
def check_interactions(player, objects):
	for object in objects:
		if player.rect.colliderect(object.rect) == True:
			if object.can_take == True:
				# pick up the object
				print("pick up object")
			else:
				# put down the object
				print("put down object")
				
