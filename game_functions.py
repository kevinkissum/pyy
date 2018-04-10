import sys
import pygame

def check_events(ship):
	""" 响应按键和鼠标事件 """
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				ship.moving_right = True
			if event.key == pygame.K_LEFT:
				ship.moving_left = True

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				ship.moving_right = False
			if event.key == pygame.K_LEFT:
				ship.moving_left = False

def update_screen(ai_settings, screen, ship):
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	# let the draw visable
	pygame.display.flip()
		


