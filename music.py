import pygame.mixer

class Music:
	def __init__(self):
		pygame.mixer.init()
		pygame.mixer.Channel(0).set_volume(0.3)
		pygame.mixer.Channel(1).set_volume(0.5)
		
		
	def play(self):
		pygame.mixer.Channel(0).play(pygame.mixer.Sound("sounds/background.wav"),loops=-1)
		

	def play_effect(self,number):
		if number==1:
			pygame.mixer.Channel(1).play(pygame.mixer.Sound("sounds/sucessful_letter.wav"))
		if number==2:
			pygame.mixer.Channel(1).play(pygame.mixer.Sound("sounds/sucessful_level.wav"))
		if number==3:
			pygame.mixer.Channel(1).play(pygame.mixer.Sound("sounds/fail_letter.wav"))
		if number==4:
			pygame.mixer.Channel(1).play(pygame.mixer.Sound("sounds/fail_level.wav"))
		




