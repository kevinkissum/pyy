import pygame

class Ship():

	def __init__(self, ai_settings, screen):
		"""init ship and set it location"""
		self.screen = screen    	# self screen is your ship screen and screen is the outside
		# load ship 
		self.image = pygame.image.load('ship.bmp')
		self.rect = self.image.get_rect()		# get rect, your can use other parameters in rect, 
		self.screen_rect = screen.get_rect()

		# set the ship in the middle
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.moving_right = False
		self.moving_left = False
		self.center = float(self.rect.centerx)

		self.ai_settings = ai_settings


	def blitme(self):
		""" 在指定位置绘制飞船 """
		self.screen.blit(self.image, self.rect)

	def update(self):
		if self.moving_right:
			self.center += self.ai_settings.ship_speed_factor

		if self.moving_left:
			self.center -= self.ai_settings.ship_speed_factor

		self.rect.centerx = self.center
