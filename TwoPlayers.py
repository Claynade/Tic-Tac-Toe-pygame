from functions import *

def imgBlitter(x,y,size_x,size_y,path):
	Img=pygame.image.load(path)
	screen.blit(pygame.transform.scale(Img, (size_x,size_y)),(x,y))
	
def drawText(x,y,color,size,text):
	font = pygame.font.Font('freesansbold.ttf', size)
	text_render= font.render(text, True, color)
	screen.blit(text_render, (x, y))

def twoPlayer(theme):
	board={'a1':' ', 'a2':' ','a3':' ','b1':' ','b2':' ','b3':' ','c1':' ', 'c2':' ', 'c3':' '}
	click=False
	option='X' #to swap between X and Y i.e cross or circle
	running=True#controlling main loop of play
	
	playable=True #After win: player shouldn't be able to check squares any further"
	#coordinates
	coor_a1=(0,(screen_y-screen_x)//2)
	coor_a2=(screen_x//3,(screen_y-screen_x)//2)
	coor_a3=(screen_x//3+screen_x//3,(screen_y-screen_x)//2)
	coor_b1=(0,(screen_y-screen_x)//2+screen_x//3)
	coor_b2=(screen_x//3,(screen_y-screen_x)//2+screen_x//3)
	coor_b3=(screen_x//3+screen_x//3,(screen_y-screen_x)//2+screen_x//3)
	coor_c1=(0,(screen_y-screen_x)//2+screen_x//3+screen_x//3)
	coor_c2=(screen_x//3,(screen_y-screen_x)//2+screen_x//3+screen_x//3)
	coor_c3=(screen_x//3+screen_x//3,(screen_y-screen_x)//2+screen_x//3+screen_x//3)
	while running:
		pos=pygame.mouse.get_pos()
		button1=pygame.Rect(0,(screen_y-screen_x)//2,screen_x//3,screen_x//3)
		button2=pygame.Rect(screen_x//3,(screen_y-screen_x)//2,screen_x//3,screen_x//3)
		button3=pygame.Rect(screen_x//3+screen_x//3,(screen_y-screen_x)//2,screen_x//3,screen_x//3)
		button4=pygame.Rect(0,(screen_y-screen_x)//2+screen_x//3,screen_x//3,screen_x//3)
		button5=pygame.Rect(screen_x//3,(screen_y-screen_x)//2+screen_x//3,screen_x//3,screen_x//3)
		button6=pygame.Rect(screen_x//3+screen_x//3,(screen_y-screen_x)//2+screen_x//3,screen_x//3,screen_x//3)
		button7=pygame.Rect(0,(screen_y-screen_x)//2+screen_x//3+screen_x//3,screen_x//3,screen_x//3)
		button8=pygame.Rect(screen_x//3,(screen_y-screen_x)//2+screen_x//3+screen_x//3,screen_x//3,screen_x//3)
		button9=pygame.Rect(screen_x//3+screen_x//3,(screen_y-screen_x)//2+screen_x//3+screen_x//3,screen_x//3,screen_x//3)
		if playable:
			if button1.collidepoint((pos)):
				if board['a1']==' ':
					if click:
						if option=='X':
							board['a1']='X'
							option='O'
						elif option=='O':
							board['a1']='O'
							option='X'
			if button2.collidepoint((pos)):
				if board['a2']==' ':
					if click:
						if option=='X':
							board['a2']='X'
							option='O'
						elif option=='O':
							board['a2']='O'
							option='X'
			if button3.collidepoint((pos)):
				if board['a3']==' ':
					if click:
						if option=='X':
							board['a3']='X'
							option='O'
						elif option=='O':
							board['a3']='O'
							option='X'
			if button4.collidepoint((pos)):
				if board['b1']==' ':
					if click:
						if option=='X':
							board['b1']='X'
							option='O'
						elif option=='O':
							board['b1']='O'
							option='X'
			if button5.collidepoint((pos)):
				if board['b2']==' ':
					if click:
						if option=='X':
							board['b2']='X'
							option='O'
						elif option=='O':
							board['b2']='O'
							option='X'
			if button6.collidepoint((pos)):
				if board['b3']==' ':
					if click:
						if option=='X':
							board['b3']='X'
							option='O'
						elif option=='O':
							board['b3']='O'
							option='X'
			if button7.collidepoint((pos)):
				if board['c1']==' ':
					if click:
						if option=='X':
							board['c1']='X'
							option='O'
						elif option=='O':
							board['c1']='O'
							option='X'
			if button8.collidepoint((pos)):
				if board['c2']==' ':
					if click:
						if option=='X':
							board['c2']='X'
							option='O'
						elif option=='O':
							board['c2']='O'
							option='X'
			if button9.collidepoint((pos)):
				if board['c3']==' ':
					if click:
						if option=='X':
							board['c3']='X'
							option='O'
						elif option=='O':
							board['c3']='O'
							option='X'
						
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
			if event.type==pygame.MOUSEBUTTONDOWN:
				click=True
			if event.type==pygame.MOUSEBUTTONUP:
				click=False
		drawBoard(0,(screen_y-screen_x)//2,theme)
		#draw markers on board
		for i in board.keys():
			if board[i]=='X':
				if i=='a1':
					cross(coor_a1[0],coor_a1[1], theme)
				if i=='a2':
					cross(coor_a2[0],coor_a2[1], theme)
				if i=='a3':
					cross(coor_a3[0],coor_a3[1], theme)
				if i=='b1':
					cross(coor_b1[0],coor_b1[1], theme)
				if i=='b2':
					cross(coor_b2[0],coor_b2[1], theme)
				if i=='b3':
					cross(coor_b3[0],coor_b3[1], theme)
				if i=='c1':
					cross(coor_c1[0],coor_c1[1], theme)
				if i=='c2':
					cross(coor_c2[0],coor_c2[1], theme)
				if i=='c3':
					cross(coor_c3[0],coor_c3[1], theme)
			elif board[i]=='O':
				if i=='a1':
					circle(coor_a1[0],coor_a1[1], theme)
				if i=='a2':
					circle(coor_a2[0],coor_a2[1], theme)
				if i=='a3':
					circle(coor_a3[0],coor_a3[1], theme)
				if i=='b1':
					circle(coor_b1[0],coor_b1[1], theme)
				if i=='b2':
					circle(coor_b2[0],coor_b2[1], theme)
				if i=='b3':
					circle(coor_b3[0],coor_b3[1], theme)
				if i=='c1':
					circle(coor_c1[0],coor_c1[1], theme)
				if i=='c2':
					circle(coor_c2[0],coor_c2[1], theme)
				if i=='c3':
					circle(coor_c3[0],coor_c3[1], theme)
		if Xwin(board):
			playable=False
			drawText(screen_x//3,screen_x//3,(240,240,240),100,'X won!')
		elif Owin(board):
			playable=False
			drawText(screen_x//3,screen_x//3,(240,240,240),100,'O won!')
		elif gameOver(board):
			playable=False
			drawText(screen_x//3,screen_x//3,(240,240,240),100,'Tie!')
		pygame.display.update()