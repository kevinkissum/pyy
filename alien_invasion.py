# import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():

	ai_settings = Settings()
	# init game and create a screen class
	pygame.init()
	# screen = pygame.display.set_mode((1200, 800))
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_hight))
	pygame.display.set_caption("Alien Invasion")
	# bg_color = (230, 230, 230)

	ship = Ship(ai_settings, screen)

	while True:
		# monitor keyboard and mounce event
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings, screen, ship)
		

run_game()