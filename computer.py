import pygame
from functions import *
from random import randint
import time
boardlst=[[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
board={'a1':' ', 'a2':' ','a3':' ','b1':' ','b2':' ','b3':' ','c1':' ', 'c2':' ', 'c3':' '}
playerTurn=True
def Player(screen, board,pos,click,option,theme):
	screen_x, screen_y=screen.get_size()
	global playerTurn
	drawBoard(screen, 0,screen_y-screen_x//2, theme)
	button1=pygame.Rect(0,(screen_y-screen_x)//2,screen_x//3,screen_x//3)
	button2=pygame.Rect(screen_x//3,(screen_y-screen_x)//2,screen_x//3,screen_x//3)
	button3=pygame.Rect(screen_x//3+screen_x//3,(screen_y-screen_x)//2,screen_x//3,screen_x//3)
	button4=pygame.Rect(0,(screen_y-screen_x)//2+screen_x//3,screen_x//3,screen_x//3)
	button5=pygame.Rect(screen_x//3,(screen_y-screen_x)//2+screen_x//3,screen_x//3,screen_x//3)
	button6=pygame.Rect(screen_x//3+screen_x//3,(screen_y-screen_x)//2+screen_x//3,screen_x//3,screen_x//3)
	button7=pygame.Rect(0,(screen_y-screen_x)//2+screen_x//3+screen_x//3,screen_x//3,screen_x//3)
	button8=pygame.Rect(screen_x//3,(screen_y-screen_x)//2+screen_x//3+screen_x//3,screen_x//3,screen_x//3)
	button9=pygame.Rect(screen_x//3+screen_x//3,(screen_y-screen_x)//2+screen_x//3+screen_x//3,screen_x//3,screen_x//3)
	if button1.collidepoint((pos)):
		if board['a1']==' ':
			if click:
				if option=='X':
					board['a1']='X'
				elif option=='O':
					board['a1']='O'
				playerTurn=True
	if button2.collidepoint((pos)):
		if board['a2']==' ':
			if click:
				if option=='X':
					board['a2']='X'
				elif option=='O':
					board['a2']='O'
				playerTurn=True
	if button3.collidepoint((pos)):
		if board['a3']==' ':
			if click:
				if option=='X':
					board['a3']='X'
				elif option=='O':
					board['a3']='O'
				playerTurn=True
	if button4.collidepoint((pos)):
		if board['b1']==' ':
			if click:
				if option=='X':
					board['b1']='X'
				elif option=='O':
					board['b1']='O'
				playerTurn=True
	if button5.collidepoint((pos)):
		if board['b2']==' ':
			if click:
				if option=='X':
					board['b2']='X'
				elif option=='O':
					board['b2']='O'
				playerTurn=True
	if button6.collidepoint((pos)):
		if board['b3']==' ':
			if click:
				if option=='X':
					board['b3']='X'
				elif option=='O':
					board['b3']='O'
				playerTurn=True
	if button7.collidepoint((pos)):
		if board['c1']==' ':
			if click:
				if option=='X':
					board['c1']='X'
				elif option=='O':
					board['c1']='O'
				playerTurn=True
	if button8.collidepoint((pos)):
		if board['c2']==' ':
			if click:
				if option=='X':
					board['c2']='X'
				elif option=='O':
					board['c2']='O'
				playerTurn=True
	if button9.collidepoint((pos)):
		if board['c3']==' ':
			if click:
				if option=='X':
					board['c3']='X'
				elif option=='O':
					board['c3']='O'
				playerTurn=True

def firstmove(board,computerMarker):
    for x in board.values():
        if x!=' ':
            return False
    return True
    			
def AI(board,computerMarker):
    global playerTurn
    if firstmove(board,computerMarker):
        board['a1']=computerMarker
    else:
        bestscore=-1000
        for i in ['a','b','c']:
            for j in range(1,4):
                if board[str(i)+str(j)]==' ':
                    board[str(i)+str(j)]=computerMarker
                    newBoard=board.copy()
                    score=minimax(newBoard,computerMarker,False)
                    board[str(i)+str(j)]=' '
                    if score>bestscore:
                        bestmove=str(i)+str(j)
                        bestscore = score
                        board[bestmove]=computerMarker
    playerTurn=False
def minimax(board,computerMarker,isMaximising):
    if computerMarker=='Y':
        playerMarker='X'
    else:
        playerMarker='Y'
    if Xwin(board):
        return 1
    elif Owin(board):
        return -1
    elif gameOver(board):
        return 0
    if isMaximising:
        bestscore=-1000
        for i in ['a','b','c']:
            for j in range(1,4):
                if board[str(i)+str(j)]==' ':
                    board[str(i)+str(j)]='computerMarker'
                    score=minimax(board.copy(), computerMarker,False)
                    board[str(i)+str(j)]=' '
                    bestscore=max(score,bestscore)
        return bestscore                
    else:
        bestscore=1000
        for i in ['a','b','c']:
            for j in range(1,4):
                if board[str(i)+str(j)]==' ':
                    board[str(i)+str(j)]='playerMarker'
                    score=minimax(board.copy(), computerMarker,True)
                    board[str(i)+str(j)]=' '
                    bestscore=min(score,bestscore)
        return bestscore
    
def start(screen):
    screen_x, screen_y=screen.get_size()
    screen.fill((50,0,50))
    bgImg=pygame.image.load('Assets/WoodenFrame.png')
    yes=pygame.image.load('Assets/Wood4.png')
    no=pygame.image.load('Assets/Wood4.png')
    screen.blit(pygame.transform.scale(bgImg,(screen_x,300)),(0,screen_x//2 + 100))
    screen.blit(pygame.transform.rotate(yes,180), (50,screen_x//2 + 300))
    screen.blit(pygame.transform.rotate(no,180), (screen_x-200,screen_x//2 + 300))
    drawText(screen, 100,screen_x//2 + 200,(163,105,47),28,'Would you like to start?')
    drawText(screen, 94,screen_x//2 + 315,(118, 97, 135),28,'YES')
    drawText(screen, screen_x-150,screen_x//2 + 315,(118, 97, 135),28,'NO')
    buttonYes=pygame.Rect(50,screen_x//2 + 300,140,50)
    buttonNo=pygame.Rect(screen_x-200,screen_x//2 + 300,140,50)
    while True:
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                click=True
            if event.type==pygame.MOUSEBUTTONUP:
                click=False
        if buttonYes.collidepoint((pos)) and click:
            return False
        elif buttonNo.collidepoint((pos)) and click:
            return True
        pygame.display.update()
        
#main loop
def vsComputer(screen, theme):
    # Reset the board if new game
    board={'a1':' ', 'a2':' ','a3':' ','b1':' ','b2':' ','b3':' ','c1':' ', 'c2':' ', 'c3':' '}
    screen_x, screen_y=screen.get_size()
    global playerTurn
    playerTurn = start(screen)
    player='X'
    AImarker='O'
    running=True
    click=False
    playable=True
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
        drawBoard(screen, 0,screen_y-screen_x//2, theme)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                click=True
            if event.type==pygame.MOUSEBUTTONUP:
                click=False
        if playable:
            if not playerTurn:
                Player(screen, board,pos,click,player,theme)
        if Xwin(board):
            drawText(screen, screen_x//5,screen_y/10,(200,200,200),150,'X won!')
            playable=False
        if Owin(board):
            drawText(screen, screen_x//5,screen_y/10,(200,200,200),150,'O won!')
            playable=False
        if gameOver(board) and not Xwin(board)and not Owin(board):
            drawText(screen, screen_x//3,screen_y/10,(200,200,200),150,'Tie!')
            playable=False
        if playable:
            if playerTurn!=False:
                AI(board,AImarker)
        for i in board.keys():
            if board[i]=='X':
                if i=='a1':
                    cross(screen, coor_a1[0],coor_a1[1], theme)
                if i=='a2':
                    cross(screen, coor_a2[0],coor_a2[1], theme)
                if i=='a3':
                    cross(screen, coor_a3[0],coor_a3[1], theme)
                if i=='b1':
                    cross(screen, coor_b1[0],coor_b1[1], theme)
                if i=='b2':
                    cross(screen, coor_b2[0],coor_b2[1], theme)
                if i=='b3':
                    cross(screen, coor_b3[0],coor_b3[1], theme)
                if i=='c1':
                    cross(screen, coor_c1[0],coor_c1[1], theme)
                if i=='c2':
                    cross(screen, coor_c2[0],coor_c2[1], theme)
                if i=='c3':
                    cross(screen, coor_c3[0],coor_c3[1], theme)
            elif board[i]=='O':
                if i=='a1':
                    circle(screen, coor_a1[0],coor_a1[1], theme)
                if i=='a2':
                    circle(screen, coor_a2[0],coor_a2[1], theme)
                if i=='a3':
                    circle(screen, coor_a3[0],coor_a3[1], theme)
                if i=='b1':
                    circle(screen, coor_b1[0],coor_b1[1], theme)
                if i=='b2':
                    circle(screen, coor_b2[0],coor_b2[1], theme)
                if i=='b3':
                    circle(screen, coor_b3[0],coor_b3[1], theme)
                if i=='c1':
                    circle(screen, coor_c1[0],coor_c1[1], theme)
                if i=='c2':
                    circle(screen, coor_c2[0],coor_c2[1], theme)
                if i=='c3':
                    circle(screen, coor_c3[0],coor_c3[1], theme)
        pygame.display.update()
if __name__=='__main__':
	pygame.init()
	vsComputer('darkVector')