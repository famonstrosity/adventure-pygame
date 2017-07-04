import pygame

import game_functions as functions
from settings import Settings
from map import Map
from player import Player
from objects import Object, Rock, House
from text_box import TextBox
from inventory import Inventory

def run_game():
	# initialize game; make settings, screen
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode(settings.screen_dimensions)
	pygame.display.set_caption("Adventure V3")
	
	# make things
	map = Map(settings, screen)
	text_box = TextBox(settings, screen)
	inventory = Inventory(settings, screen)
	
	player = Player(settings, screen, map)
	rock = Rock(settings, screen, map, 60, 60)
	house = House(settings, screen, map, 450, 250)
	objects = [rock, house]
	
	# main game loop
	while True:
		# look for events
		functions.check_events(settings, player, objects)
		# update object info
		player.update()
		# update/redraw screen
		functions.update_screen(settings, screen, map, player, objects,
									text_box, inventory)

run_game()
