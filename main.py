import pygame
import json
from TwoPlayers import twoPlayer
from functions import *
from setting import Setting
from computer import vsComputer
pygame.init()
import pygame
screen=pygame.display.set_mode((1300,840))
screen_x, screen_y=screen.get_size()

#functions
def bg(x,y):
	bgImg=pygame.image.load('Assets/bg.png')
	screen.blit(pygame.transform.scale(bgImg,(screen_x,int(screen_y*0.7))),(x,y))

#main_screen
playing=True
while playing:
	click=False
	#loads json file
	with open('gamedata.json') as myfile:
		data=json.load(myfile)
		myfile.close()
		theme=data['theme']
	two_player_btn=pygame.Rect(screen_x//10,(screen_y*6)//10,(screen_x*8)//10,(screen_y*2)//10)
	vsComputer_btn=pygame.Rect((screen_x*6)//30,(screen_y*8)//10,(screen_x*18)//30,(screen_y*2)//10)
	theme_btn=pygame.Rect(screen_x-(screen_x*2)//10,(screen_y*17)//20,(screen_x*2)//10,(screen_x)*2//10)
	setting_btn=pygame.Rect(screen_x//50,(screen_y*17)//20,(screen_x*2)//10,(screen_x)*2//10)
	pos=pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			playing=False
		if event.type==pygame.MOUSEBUTTONDOWN:
			click=True
		if event.type==pygame.MOUSEBUTTONUP:
			click=False
	if two_player_btn.collidepoint((pos)):
		twoPlayer(theme)
	if vsComputer_btn.collidepoint((pos)):
		vsComputer(theme)
	if setting_btn.collidepoint((pos)):
		Setting(theme)
	if theme_btn.collidepoint((pos)):
		if click:
			if theme=='dark':
				theme='light'
			elif theme=='light':
				theme='darkVector'
			elif theme=='darkVector':
				theme='dark'
	data['theme']=theme
	if theme=='dark':
		screen.fill((0,0,0))
	if theme=='light':
		screen.fill((250,240,240))
	if theme=='darkVector':
		screen.fill((50,0,50))
	wood1(screen_x//10,(screen_y*6)//10,(screen_x*8)//10,(screen_y*2)//10)
	wood2((screen_x*6)//30,(screen_y*8)//10,(screen_x*18)//30,(screen_y*2)//10)
	wood3(0,0,screen_x,screen_y*3//20)
	wood4(screen_x-(screen_x*2)//10,(screen_y*17)//20,(screen_x*2)//10,(screen_x)*2//10)
	wood4(screen_x//50,(screen_y*17)//20,(screen_x*2)//10,(screen_x)*2//10)
	#changing json values
	with open('gamedata.json','w') as myfile:
		json.dump(data,myfile)
		myfile.close()
	bg(0,50)
	pygame.display.update()
