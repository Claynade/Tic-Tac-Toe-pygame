import pygame

""" screen_info = pygame.display.Info()
print(screen_info.current_w)
screen=pygame.display.set_mode((screen_info.current_w, screen_info.current_h))
screen_x, screen_y=screen.get_size()
if screen_x>480:
	screen_x=460 """

def wood1(screen, x,y,size_x,size_y):
	wood1Img=pygame.image.load('Assets/wood1.png')
	screen.blit(pygame.transform.scale(wood1Img, (size_x,size_y)),(x,y))
	
def wood2(screen, x,y,size_x,size_y):
	wood2Img=pygame.image.load('Assets/wood2.png')
	screen.blit(pygame.transform.scale(wood2Img, (size_x,size_y)),(x,y))
	
def wood3(screen, x,y,size_x,size_y):
	wood3Img=pygame.image.load('Assets/wood3.png')
	screen.blit(pygame.transform.scale(wood3Img, (size_x,size_y)),(x,y))
	
def wood4(screen, x,y,size_x,size_y):
	wood4Img=pygame.image.load('Assets/wood4.png')
	screen.blit(pygame.transform.scale(wood4Img, (size_x,size_y)),(x,y))

#image and text drawing functions
def drawCell(screen, x,y, theme): #size_x, size_y
	screen_x, screen_y=screen.get_size()
	if theme == "darkVector":
		Img=pygame.image.load('Assets/darkVector.png')
	else:
		Img=pygame.image.load('Assets/woodenboard.jpg')
	screen.blit(pygame.transform.scale(Img, (screen_x//3,screen_x//3)),(x,y)) #screen_x//3,screen_x//3 earlier
	
def imgBlitter(screen, x,y,size_x,size_y,path):
	Img=pygame.image.load(path)
	screen.blit(pygame.transform.scale(Img, (size_x,size_y)),(x,y))
	
def drawText(screen, x,y,color,size,text):
	font = pygame.font.Font('freesansbold.ttf', size)
	text_render= font.render(text, True, color)
	screen.blit(text_render, (x, y))

#changing theme and drawing board

def drawBoard(screen, x, y, theme):
	screen_x, screen_y=screen.get_size() # need to fix this
	if theme=='light':
		screen.fill((250,250,250))
	elif theme=='dark':
		screen.fill((0,0,0))
	elif theme=='darkVector':
		screen.fill((50,0,50))
	drawCell(screen, 0,(screen_y-screen_x)//2, theme)
	drawCell(screen, screen_x//3,(screen_y-screen_x)//2, theme)
	drawCell(screen, screen_x//3+screen_x//3,(screen_y-screen_x)//2, theme)
	drawCell(screen, 0,(screen_y-screen_x)//2+screen_x//3, theme)
	drawCell(screen, screen_x//3,(screen_y-screen_x)//2+screen_x//3, theme)
	drawCell(screen, screen_x//3+screen_x//3,(screen_y-screen_x)//2+screen_x//3, theme)
	drawCell(screen, 0,(screen_y-screen_x)//2+screen_x//3+screen_x//3, theme)
	drawCell(screen, screen_x//3,(screen_y-screen_x)//2+screen_x//3+screen_x//3, theme)
	drawCell(screen, screen_x//3+screen_x//3,(screen_y-screen_x)//2+screen_x//3+screen_x//3, theme)

#Markers
def cross(screen, x,y,theme):
	screen_x, screen_y=screen.get_size() # need to fix this
	size_x,size_y=((screen_x//3)*8)//10,((screen_x//3)*8)//10
	if theme=='darkVector':
		Img=pygame.image.load('Assets/cross.png')
	elif theme=='light' or theme=='dark':
		Img=pygame.image.load('Assets/woodenCross.png')
	x,y=x+((screen_x//3)//10),y+((screen_x//3)//10)
	screen.blit(pygame.transform.scale(Img, (size_x,size_y)),(x,y))

def circle(screen, x,y,theme):
	screen_x, screen_y=screen.get_size() # need to fix this
	size_x,size_y=((screen_x//3)*8)//10,((screen_x//3)*8)//10
	if theme=='darkVector':
		Img=pygame.image.load('Assets/circle.png')
	elif theme=='light' or theme=='dark':
		Img=pygame.image.load('Assets/woodenCircle.png')
	x,y=x+((screen_x//3)//10),y+((screen_x//3)//10)
	screen.blit(pygame.transform.scale(Img, (size_x,size_y)),(x,y))
		
		
#Game deciding functions
def gameOver(dictionary):
	if ' ' not in dictionary.values():
		return True
#Win
def Xwin(dictionary):
	if (dictionary['a1']==dictionary['a2']==dictionary['a3']=='X') or (dictionary['b1']==dictionary['b2']==dictionary['b3']=='X') or (dictionary['c1']==dictionary['c2']==dictionary['c3']=='X') or (dictionary['a1']==dictionary['b1']==dictionary['c1']=='X') or (dictionary['a2']==dictionary['b2']==dictionary['c2']=='X') or (dictionary['a3']==dictionary['b3']==dictionary['c3']=='X') or (dictionary['a1']==dictionary['b2']==dictionary['c3']=='X') or (dictionary['a3']==dictionary['b2']==dictionary['c1']=='X'):
		return True

def Owin(dictionary):
	if (dictionary['a1']==dictionary['a2']==dictionary['a3']=='O') or (dictionary['b1']==dictionary['b2']==dictionary['b3']=='O') or (dictionary['c1']==dictionary['c2']==dictionary['c3']=='O') or (dictionary['a1']==dictionary['b1']==dictionary['c1']=='O') or (dictionary['a2']==dictionary['b2']==dictionary['c2']=='O') or (dictionary['a3']==dictionary['b3']==dictionary['c3']=='O') or (dictionary['a1']==dictionary['b2']==dictionary['c3']=='O') or (dictionary['a3']==dictionary['b2']==dictionary['c1']=='O'):
		return True
