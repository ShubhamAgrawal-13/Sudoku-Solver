import pygame
import random
import numpy as np
from time import sleep
import sys

n=9
width=n*55
pygame.init()
TIME=0.05
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 
dimgray=(105,105,105)
gray=(128,128,128)
lightgray=(200,200,200)
black = (0, 0, 0) 
red = (255, 0, 0) 
colors=[(255,0,0),(0,255,0),(0,0,255),(0,255,255),(255,0,255),(255,255,0)]

win = pygame.display.set_mode((width,width))
# win.fill((0,0,0))
pygame.display.set_caption("Sudoku")
f=pygame.font.SysFont("comicsans",30)
clock = pygame.time.Clock()

board_val=[['5','3','.','.','7','.','.','.','.'],
	   ['6','.','.','1','9','5','.','.','.'],
	   ['.','9','8','.','.','.','.','6','.'],

	   ['8','.','.','.','6','.','.','.','3'], 
	   ['4','.','.','8','.','3','.','.','1'], 
	   ['7','.','.','.','2','.','.','.','6'],

	   ['.','6','.','.','.','.','2','8','.'], 
	   ['.','.','.','4','1','9','.','.','5'], 
	   ['.','.','.','.','8','.','.','7','9']]

class cube(object):
	"""docstring for Cube"""
	def __init__(self, x, y, val,color):
		self.x=x
		self.y=y
		self.val=val
		self.color=color

	def draw_cube(self, win):
		global width, n
		t=width//n
		# pygame.draw.rect(win, white, (self.x*t+4,self.y*t+4,t,t))
		pygame.draw.rect(win, self.color,(self.x*t,self.y*t,t,t))
		if(self.val=='.'):
			p_label=f.render(f" ",1 ,(0,0,0))
		else:
			p_label=f.render(f"{self.val}",1 ,(0,0,0))

		win.blit(p_label,(self.x*t+t//2-6,self.y*t+t//2-6))
		draw_grid(win)
		pygame.display.update() 

	def draw_cube_light(self, win):
		global width, n
		t=width//n

		pygame.draw.rect(win, self.color,(self.x*t,self.y*t,t,t))
		if(self.val=='.'):
			p_label=f.render(f" ",1 ,red)
		else:
			p_label=f.render(f"{self.val}",1 ,red)

		win.blit(p_label,(self.x*t+t//2-6,self.y*t+t//2-6))
		draw_grid(win)
		pygame.display.update()

	def draw_cube_border_1(self, win):
		global width, n
		t=width//n
		pygame.draw.rect(win, green, (self.x*t,self.y*t,t,t))
		draw_grid(win)
		pygame.display.update()

def draw_grid(win):
	#draw the grid
	global width,n
	t=width//n
	xx=0
	yy=0
	for l in range(n):
		xx+=t
		yy+=t
		if(xx%3==0 and xx!=0):
			pygame.draw.line(win, black, (xx,0) , (xx,width),6)
			pygame.draw.line(win, black, (0,yy) , (width,yy),6)
		else:
			pygame.draw.line(win, black, (xx,0) , (xx,width),3)
			pygame.draw.line(win, black, (0,yy) , (width,yy),3)


def drawWindow(win):
	global width,n,board
	win.fill(white)
	for i in range(n):
		for j in range(n):
			board[i][j].draw_cube(win)
	draw_grid(win)
	pygame.display.update() 


def is_thik(r, c,choice):
	global board,n
	for i in range(n):
		if(board[i][c].val==choice):
			return False
	for i in range(n):
		if(board[r][i].val==choice):
			return False

	block_r=r%3
	block_c=c%3
	pr=0
	qr=0

	if(block_r==0 and block_c==0):
		pr=r
		qr=c
	elif(block_r==0 and block_c==1):
		pr=r
		qr=c-1
	elif(block_r==0 and block_c==2):
		pr=r
		qr=c-2
	elif(block_r==1 and block_c==0):
		pr=r-1
		qr=c
	elif(block_r==1 and block_c==1):
		pr=r-1
		qr=c-1
	elif(block_r==1 and block_c==2):
		pr=r-1
		qr=c-2
	elif(block_r==2 and block_c==0):
		pr=r-2
		qr=c
	elif(block_r==2 and block_c==1):
		pr=r-2
		qr=c-1
	elif(block_r==2 and block_c==2):
		pr=r-2
		qr=c-2

	for p in range(pr,pr+3):
		for q in range(qr,qr+3):
			if(board[p][q].val==choice):
				return False

	return True

def check():
	global board,n
	for j in range(n):
		for i in range(n):
			if(board[i][j].val=='.'):
				return (i,j)
	# board[i][j].draw_cube(win)
	return None

def print_board():
	global board,n
	for i in range(n):
		for j in range(n):
			sleep(TIME)
			print(board[i][j].val, end=" ")
		print()

def solve():
	global board,n,win
	empty_cell=check()
	sleep(TIME)
	if not empty_cell:
		return True
	else:
		i, j = empty_cell
		board[i][j].draw_cube_border_1(win)
		sleep(TIME)
		board[i][j].draw_cube(win)
		for choice in range(1,10):
			choice=str(choice)
			if(is_thik(i,j,choice)):
				board[i][j].val=choice
				board[i][j].draw_cube_light(win)
				pygame.display.update()
				if(solve()):
					return True
				board[i][j].val='.'
				board[i][j].draw_cube_light(win)
				pygame.display.update()	
	return False
	


board=[]
for i in range(n):
	row=[]
	bi=i//3
	for j in range(n):
		bj=j//3
		s=bi+bj
		if(s%2==1):
			row.append(cube(i,j,board_val[i][j],lightgray))
		else:
			row.append(cube(i,j,board_val[i][j],white))
	board.append(row)


drawWindow(win)
sleep(1)
solve()
# print_board()
# drawWindow(win)
sleep(5)
pygame.quit()

