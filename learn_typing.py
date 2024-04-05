import pygame
import button
import sys
import random
import time
from heart import Heart
from scoreboard import Scoreboard as sb
import music

class LearnTyping:
	def __init__(self):
		with open("./data/level_data.json",encoding="utf-8") as f:
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
		self.quit_button.rect.bottom=self.screen_rect.bottom
		self.start_button=button.Button(self,"开始")
		self.start_button.rect.center=self.screen_rect.center
		self.game_mode='ready' #ready,select,pre-play,play
		self.right=[]
		self.health=5
		self.board=sb(self)
		self.sheet_of_typing=pygame.image.load("images/sheet_of_typing.bmp")
		self.rect_of_SFT=self.sheet_of_typing.get_rect()
		self.rect_of_SFT.center=self.screen_rect.center
		self.rect_of_SFT.top=self.screen_rect.top
		self.go_back_button=button.Button4(self,'返回')
		self.go_back_button.rect.top=self.screen_rect.top
		self.go_back_button.rect.right=self.screen_rect.right
		self.SFT_button=button.Button4(self,'指法表')
		self.SFT_button.rect.top=self.screen_rect.top
		self.SFT_button.rect.right=self.screen_rect.right
		self.music=music.Music()
		self.music.play()
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
			data1=[]
			for i in range(1,level+1):
				data1.extend(self.level_data[f"level_{i}"]['new_key'])
			k=""
			for i in range(50):
				k+=random.choice(data['new_key'])
			for i in range(20):
				k+=random.choice(data1)
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
			for i in range(10):
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
				self._check_go_back_or_SFT_button(mouse_pos)
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
							self.all=list(self.str)[:10]
							self.type=self.level_data[f"level_{self.answer}"]['type']
							stay_in=True
							while stay_in:
								for event in pygame.event.get():
									if event.type==pygame.QUIT:
										with open('data/level.json','w') as f:
											f.write(f'{self.level_now}')
											sys.exit()
									elif event.type==pygame.MOUSEBUTTONDOWN:
										mouse_pos=pygame.mouse.get_pos()
										self._check_quit_button(mouse_pos)
										self._check_go_back_or_SFT_button(mouse_pos)
										stay_in=False
									if event.type==pygame.KEYDOWN:
										if event.key==pygame.K_ESCAPE:
											with open('data/level.json','w') as f:
												f.write(f'{self.level_now}')
												sys.exit()

								self.screen.fill(self.bg_color)
								self.quit_button.draw_button()
								self.go_back_button.draw_button()
								sth=self.level_data[f'level_{self.answer}']
								if self.type=='learn':
									string_show=f"这关要学习的是{sth['new_key'][0]},{sth['new_key'][1]},分别用{sth['msg'][0][0]}{sth['msg'][0][1]}{sth['msg'][0][2]}和{sth['msg'][1][0]}{sth['msg'][1][1]}{sth['msg'][1][2]}来打。"
									button_show=button.Button2(self,string_show)
									button_show.rect.center=self.screen_rect.center
								else:
									string_show=f"这关是{sth['msg'][0]}。"
									button_show=button.Button2(self,string_show)
									button_show.rect.center=self.screen_rect.center
								button_show.draw_button()
								button_tip=button.Button3(self,'(鼠标单击继续)')
								button_tip.rect.center=self.screen_rect.center
								button_tip.rect.top=button_show.rect.bottom
								button_tip.draw_button()
								self.screen.blit(self.sheet_of_typing,self.rect_of_SFT)
								pygame.display.flip()
							if self.level_data[f"level_{self.answer}"]['type'] != 'endless':
								self.time=self.level_data[f"level_{self.answer}"]['time']
							else:
								self.health=self.level_data[f"level_{self.answer}"]['health']
							self.time_typed=time.time()
							self.start_time=time.time()
						else:
							self.screen.fill(self.bg_color)
							a=button.Button(self,"你输入的数字大于您所在关卡")
							a.rect.center=self.screen_rect.center
							a.rect.left=self.screen_rect.left
							a.draw_button()
							pygame.display.flip()
							time.sleep(3)
							self.game_mode='select'
				elif self.game_mode=='play':
					if self.type=='endless':
						self.time_typed=time.time()
					try:
						if chr(int(str(event.key)))==self.str[0]:
							self.music.play_effect(1)
							self.str=self.str[1:]
							self.right.append(chr(int(str(event.key))))
							self.all.remove(chr(int(str(event.key))))
							self.typed+=1
							if self.all==[]:
								self.all=list(self.str)[:10]
								self.right=[]
						else:
							self.music.play_effect(3)
							if self.type != 'endless':
								self.plus_time+=1
							else:
								self.health-=1
								self.board.prep_hearts()
								if self.health<=0:
									self.game_mode='ready'
									self.end_time=time.time()
									c=button.Button2(self,f'你打对了{self.typed}个字,花了{round(self.end_time-self.start_time)}秒。')
									self.screen.fill(self.bg_color)
									b.rect.center=self.screen_rect.center
									b.draw_button()
									self.music.play_effect(4)
									pygame.display.flip()
									time.sleep(3)

						if self.str=='' and self.type!='endless':
							self.end_time=time.time()
							self.game_mode='ready'
							if round(self.end_time-self.start_time+self.plus_time)<=self.time:
								b=button.Button2(self,f'恭喜你！你用了{round(self.end_time-self.start_time)}+{self.plus_time}(打错惩罚)秒通过了这关。')
								if int(self.answer)==self.level_now and self.type!='endless':
									self.level_now+=1
								self.music.play_effect(2)
							else:
								b=button.Button2(self,f'你用了{round(self.end_time-self.start_time)}+{self.plus_time}(打错惩罚)秒完成了这关,但超过了{self.time}秒。')
								self.music.play_effect(4)
							self.screen.fill(self.bg_color)
							b.rect.center=self.screen_rect.center
							b.draw_button()
							pygame.display.flip()
							time.sleep(3)
						if self.str=='' and self.type=='endless':
							self.str=self.generate_level_string(int(self.answer))
							self.all=list(self.str)[:10]
					except:
						if event.key:
							self.music.play_effect(3)
							if self.type != 'endless':
								self.plus_time+=1
							else:
								self.health-=1
								self.board.prep_hearts()
								if self.health<=0:
									self.game_mode='ready'
									self.end_time=time.time()
									c=button.Button2(self,f'你打对了{self.typed}个字,花了{round(self.end_time-self.start_time)}秒。')
									self.screen.fill(self.bg_color)
									c.rect.center=self.screen_rect.center
									c.draw_button()
									self.music.play_effect(4)
									pygame.display.flip()
									time.sleep(3)



	def _check_quit_button(self,mouse_pos):
		if self.quit_button.rect.collidepoint(mouse_pos):
			with open('data/level.json','w') as f:
				f.write(f'{self.level_now}')
			sys.exit()

	def _check_start_button(self,mouse_pos):
		if self.start_button.rect.collidepoint(mouse_pos) and self.game_mode=='ready':
			self.time_typed=time.time()
			self.typed=0
			self.type=''
			self.time=0
			self.plus_time=0
			self.answer=''
			self.right=[]
			self.all =[]
			self.game_mode='select'
			self.select_button=button.Button(self,f"请输入关卡编号(1~{self.level_now})")
			self.select_button.rect.center=self.screen_rect.center
			self.select_button.rect.left=self.screen_rect.left

	def _check_go_back_or_SFT_button(self,mouse_pos):
		if self.go_back_button.rect.collidepoint(mouse_pos) and self.game_mode!='ready':
			if self.game_mode=='select':
				self.game_mode='ready'
			elif self.game_mode=='play':
				self.game_mode='select'
		elif self.SFT_button.rect.collidepoint(mouse_pos) and self.game_mode=='ready':
			stay_in=True
			while stay_in:
				for event in pygame.event.get():
					if event.type==pygame.QUIT:
						with open('data/level.json','w') as f:
							f.write(f'{self.level_now}')
							sys.exit()
					elif event.type==pygame.MOUSEBUTTONDOWN:
						mouse_pos=pygame.mouse.get_pos()
						self._check_quit_button(mouse_pos)
						stay_in=False
				self.screen.fill(self.bg_color)
				self.quit_button.draw_button()
				sth=button.Button3(self,'（鼠标单击继续）')
				sth.rect.center=self.screen_rect.center
				sth.draw_button()
				self.screen.blit(self.sheet_of_typing,self.rect_of_SFT)
				pygame.display.flip()




	def _update_screen(self):
		self.screen.fill(self.bg_color)
		self.quit_button.draw_button()
		if self.game_mode=='ready':
			self.start_button.draw_button()
		if self.game_mode=='select':
			self.select_button.msg=f"请输入关卡编号(按F1结束 1~{self.level_now}){self.answer}"
			self.select_button.draw_button()
		if self.game_mode=='play':
			self.playing_button=button.Button1(self,'    '.join(self.right))
			self.playing_button.rect.center=self.screen_rect.center
			self.playing_button.rect.left=self.screen_rect.left
			self.playing_button.draw_button()
			if self.right:
				self.playing_button1=button.Button(self,'    '+'    '.join(self.all))
			else:
				self.playing_button1=button.Button(self,'    '.join(self.all))
			self.playing_button1.rect.center=self.screen_rect.center
			self.playing_button1.rect.left=self.playing_button.msg_image_rect.right
			self.playing_button1.draw_button()
			if self.type=='endless':
				if (time.time()-self.time_typed)>=3:
					self.health-=1
					self.board.prep_hearts()
					self.time_typed=time.time()
					if self.health<=0:
						self.game_mode='ready'
						self.end_time=time.time()
						c=button.Button2(self,f'你打对了{self.typed}个字,花了{round(self.end_time-self.start_time)}秒。')
						self.screen.fill(self.bg_color)
						c.rect.center=self.screen_rect.center
						c.draw_button()
						pygame.display.flip()
						time.sleep(3)
				self.board.show_score()
		if self.game_mode!='ready':
			self.go_back_button.draw_button()
		else:
			self.SFT_button.draw_button()
		if self.game_mode=='play':
			if self.type!='endless':
				show_the_button=button.Button2(self,f'{round(time.time()-self.start_time)}+{self.plus_time}秒')
			else:
				show_the_button=button.Button2(self,f'请在{round(3-(time.time()-self.time_typed))}秒内打字。你已用{round(time.time()-self.start_time)}秒。')				
			show_the_button.rect.center=self.screen_rect.center
			show_the_button.rect.top=self.screen_rect.top
			show_the_button.draw_button()
		pygame.display.flip()

	def run_game(self):
		while True:
			self._check_event()
			self._update_screen()


l=LearnTyping()
l.run_game()