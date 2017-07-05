class Settings():

	def __init__(self):
		"""stores settings for adventure game"""
		
		# screen settings
		self.screen_dimensions = (600, 600)
		self.mode = 1
		
		# map settings
		self.map_height = 300
		self.map_width = 500
		self.map_x = 50
		self.map_y = 50
		self.map_color = (0, 255, 0)
		
		# text box settings
		self.text_height = 150
		self.text_width = 500
		self.text_x = 50
		self.text_y = 400
		self.textbox_color = (255, 255, 0)
		
		# inventory settings
		self.inventory_height = 50
		self.inventory_width = 500
		self.inventory_x = 50
		self.inventory_y = 350
		self.inventory_color = (0, 0, 255)
		
		# player settings
		self.player_dimensions = (40, 40)
