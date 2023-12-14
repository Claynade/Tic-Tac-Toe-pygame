import pygame
screen=pygame.display.set_mode((1300,840))
screen_x, screen_y=screen.get_size()

def wood1(x,y,size_x,size_y):
	wood1Img=pygame.image.load('Assets/wood1.png')
	screen.blit(pygame.transform.scale(wood1Img, (size_x,size_y)),(x,y))
	
def wood2(x,y,size_x,size_y):
	wood2Img=pygame.image.load('Assets/wood2.png')
	screen.blit(pygame.transform.scale(wood2Img, (size_x,size_y)),(x,y))
	
def wood3(x,y,size_x,size_y):
	wood3Img=pygame.image.load('Assets/wood3.png')
	screen.blit(pygame.transform.scale(wood3Img, (size_x,size_y)),(x,y))
	
def wood4(x,y,size_x,size_y):
	wood4Img=pygame.image.load('Assets/wood4.png')
	screen.blit(pygame.transform.scale(wood4Img, (size_x,size_y)),(x,y))

#image and text drawing functions
def woodenBoard(x,y):
	woodenBoardImg=pygame.image.load('Assets/woodenboard.jpg')
	screen.blit(pygame.transform.scale(woodenBoardImg, (screen_x//3,screen_x//3)),(x,y))
		
def darkVectorBoard(x,y):
	darkVectorImg=pygame.image.load('Assets/darkVector.png')
	screen.blit(pygame.transform.scale(darkVectorImg, (screen_x//3,screen_x//3)),(x,y))
	
def imgBlitter(x,y,size_x,size_y,path):
	Img=pygame.image.load(path)
	screen.blit(pygame.transform.scale(Img, (size_x,size_y)),(x,y))
	
def drawText(x,y,color,size,text):
	font = pygame.font.Font('freesansbold.ttf', size)
	text_render= font.render(text, True, color)
	screen.blit(text_render, (x, y))

#changing theme and drawing board

def drawBoard(x,y,theme):
	if theme=='light':
		screen.fill((250,250,250))
		woodenBoard(0,(screen_y-screen_x)//2)
		woodenBoard(screen_x//3,(screen_y-screen_x)//2)
		woodenBoard(screen_x//3+screen_x//3,(screen_y-screen_x)//2)
		woodenBoard(0,(screen_y-screen_x)//2+screen_x//3)
		woodenBoard(screen_x//3,(screen_y-screen_x)//2+screen_x//3)
		woodenBoard(screen_x//3+screen_x//3,(screen_y-screen_x)//2+screen_x//3)
		woodenBoard(0,(screen_y-screen_x)//2+screen_x//3+screen_x//3)
		woodenBoard(0+screen_x//3,(screen_y-screen_x)//2+screen_x//3+screen_x//3)
		woodenBoard(screen_x//3+screen_x//3,(screen_y-screen_x)//2+screen_x//3+screen_x//3)
	if theme=='dark':
		screen.fill((0,0,0))
		woodenBoard(0,(screen_y-screen_x)//2)
		woodenBoard(screen_x//3,(screen_y-screen_x)//2)
		woodenBoard(screen_x//3+screen_x//3,(screen_y-screen_x)//2)
		woodenBoard(0,(screen_y-screen_x)//2+screen_x//3)
		woodenBoard(screen_x//3,(screen_y-screen_x)//2+screen_x//3)
		woodenBoard(screen_x//3+screen_x//3,(screen_y-screen_x)//2+screen_x//3)
		woodenBoard(0,(screen_y-screen_x)//2+screen_x//3+screen_x//3)
		woodenBoard(screen_x//3,(screen_y-screen_x)//2+screen_x//3+screen_x//3)
		woodenBoard(screen_x//3+screen_x//3,(screen_y-screen_x)//2+screen_x//3+screen_x//3)
	if theme=='darkVector':
		screen.fill((50,0,50))
		darkVectorBoard(0,(screen_y-screen_x)//2)
		darkVectorBoard(screen_x//3,(screen_y-screen_x)//2)
		darkVectorBoard(screen_x//3+screen_x//3,(screen_y-screen_x)//2)
		darkVectorBoard(0,(screen_y-screen_x)//2+screen_x//3)
		darkVectorBoard(screen_x//3,(screen_y-screen_x)//2+screen_x//3)
		darkVectorBoard(screen_x//3+screen_x//3,(screen_y-screen_x)//2+screen_x//3)
		darkVectorBoard(0,(screen_y-screen_x)//2+screen_x//3+screen_x//3)
		darkVectorBoard(screen_x//3,(screen_y-screen_x)//2+screen_x//3+screen_x//3)
		darkVectorBoard(screen_x//3+screen_x//3,(screen_y-screen_x)//2+screen_x//3+screen_x//3)

#Markers
def cross(x,y,theme):
	size_x,size_y=((screen_x//3)*8)//10,((screen_x//3)*8)//10
	if theme=='darkVector':
		Img=pygame.image.load('Assets/cross.png')
	elif theme=='light' or theme=='dark':
		Img=pygame.image.load('Assets/woodenCross.png')
	x,y=x+((screen_x//3)//10),y+((screen_x//3)//10)
	screen.blit(pygame.transform.scale(Img, (size_x,size_y)),(x,y))

def circle(x,y,theme):
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
