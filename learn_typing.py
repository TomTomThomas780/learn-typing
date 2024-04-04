import pygame
import button
import sys
import random
import time

class LearnTyping:
	def __init__(self):
		with open("./data/level_data.json") as f:
			file = f.read()
			self.level_data = eval(file)
		pygame.init()
		self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
		self.screen_width=self.screen.get_rect().width
		self.screen_height=self.screen.get_rect().height
		pygame.display.set_caption("打字宝典")
		self.screen_rect=self.screen.get_rect()
		self.bg_color=(20,170,197)
		self.quit_button=button.Button(self,"退出")
		self.quit_button.rect.top=self.screen_rect.top
		self.start_button=button.Button(self,"开始")
		self.start_button.rect.center=self.screen_rect.center
		self.game_mode='ready' #ready,select,play
		try:
			with open('data/level.json') as f:
				self.level_now=int(f.read())
		except:
			self.level_now=1
		self.answer=''
	
	def generate_level_string(self,level):
		level_name=f"level_{level}"
		data=self.level_data[level_name]
		if data['type'] == 'learn':
			k=""
			for i in range(50):
				k+=random.choice(data['new_key'])
			return k
		elif data['type'] == 'review':
			data1=[]
			for i in range(1,level):
				data1.extend(self.level_data[f"level_{i}"]['new_key'])
			k=""
			for i in range(50):
				k+=random.choice(data1)
			return k
		else:
			data1=[]
			for i in range(1,level):
				data1.extend(self.level_data[f"level_{i}"]['new_key'])
			k=""
			for i in range(10000):
				k+=random.choice(data1)
			return k


	def _check_event(self):
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				with open('data/level.json','w') as f:
					f.write(f'{self.level_now}')
				sys.exit()
			elif event.type==pygame.MOUSEBUTTONDOWN:
				mouse_pos=pygame.mouse.get_pos()
				self._check_quit_button(mouse_pos)
				self._check_start_button(mouse_pos)
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_ESCAPE:
					with open('data/level.json','w') as f:
						f.write(f'{self.level_now}')
					sys.exit()
				if self.game_mode=='select':
					if event.key==pygame.K_0:
						self.answer=self.answer+'0'
					elif event.key==pygame.K_BACKSPACE:
						if self.answer:
							self.answer=self.answer[:len(self.answer)-1]
						else:
							pass
					elif event.key==pygame.K_1:
						self.answer=self.answer+'1'
					elif event.key==pygame.K_2:
						self.answer=self.answer+'2'
					elif event.key==pygame.K_3:
						self.answer=self.answer+'3'
					elif event.key==pygame.K_4:
						self.answer=self.answer+'4'
					elif event.key==pygame.K_5:
						self.answer=self.answer+'5'
					elif event.key==pygame.K_6:
						self.answer=self.answer+'6'
					elif event.key==pygame.K_7:
						self.answer=self.answer+'7'
					elif event.key==pygame.K_8:
						self.answer=self.answer+'8'
					elif event.key==pygame.K_9:
						self.answer=self.answer+'9'
					elif event.key==pygame.K_F1:
						self.game_mode='play'
						if int(self.answer)<=self.level_now:
							self.str=self.generate_level_string(int(self.answer))
						else:
							self.screen.fill(self.bg_color)
							a=button.Button(self,"你输入的数字大于您所在关卡")
							a.rect.center=self.screen_rect.center
							a.draw_button()
							pygame.display.flip()
							time.sleep(3)
							self.game_mode='select'
				elif self.game_mode=='play':
					try:
						if chr(int(str(event.key)))==self.str[0]:
							self.str=self.str[1:]
						if self.str=='':
							self.game_mode='ready'
							self.level_now+=1
					except:
						pass


	def _check_quit_button(self,mouse_pos):
		if self.quit_button.rect.collidepoint(mouse_pos):
			with open('data/level.json','w') as f:
				f.write(f'{self.level_now}')
			sys.exit()

	def _check_start_button(self,mouse_pos):
		if self.start_button.rect.collidepoint(mouse_pos) and self.game_mode=='ready':
			self.game_mode='select'
			self.select_button=button.Button(self,f"请输入关卡编号(1~{self.level_now})")
			self.select_button.rect.center=self.screen_rect.center

	def _update_screen(self):
		self.screen.fill(self.bg_color)
		self.quit_button.draw_button()
		if self.game_mode=='ready':
			self.start_button.draw_button()
		if self.game_mode=='select':
			self.select_button.msg=f"请输入关卡编号(按F1结束 1~{self.level_now}){self.answer}"
			self.select_button.draw_button()
		if self.game_mode=='play':
			self.playing_button=button.Button(self,'    '.join(list(self.str)))
			self.playing_button.rect.center=self.screen_rect.center
			self.playing_button.rect.left=self.screen_rect.left
			self.playing_button.draw_button()
		pygame.display.flip()

	def run_game(self):
		while True:
			self._check_event()
			self._update_screen()


l=LearnTyping()
l.run_game()