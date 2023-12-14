import json
import pygame
from functions import *
screen=pygame.display.set_mode((1300,800))
#with open(r'gamedata.json','r') as myfile:
#	data=json.load(myfile)
def Setting(theme):
	running=True
	while running:
		if theme=='dark':
			screen.fill((30,0,0))
		if theme=='light':
			screen.fill((250,250,250))
		if theme=='darkVector':
			screen.fill((50,0,50))
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
		pygame.display.update()

