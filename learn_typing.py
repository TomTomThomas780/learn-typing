import pygame

class LearnTyping:
	def __init__(self):
		with open("./data/level_data.json") as f:
			file = f.read()
			self.level_data = eval(file)
			print(self.level_data)
l=LearnTyping()