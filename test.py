import pygame
import math
from settings import Settings
pygame.init()

def drawLine(background):
	pygame.draw.line(background,(255,0,0),(100,300),(1100,300),3)
	pygame.draw.line(background,(255,0,0),(100,400),(1100,400),3)
	pygame.draw.line(background,(255,0,0),(250,300),(300,200),3)
	pygame.draw.line(background,(255,0,0),(300,200),(900,200),3)
	pygame.draw.line(background,(255,0,0),(900,200),(950,300),3)
	
def main():
	ai_settings=Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))	#界面
	pygame.display.set_caption("Track_Line")	#命名
	
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((255, 255, 255))#背景板参数
	
	drawLine(background)
	
	clock = pygame.time.Clock()
	keepGoing = True
	while keepGoing:
		clock.tick(30)
		for event in pygame.event.get():	#事件监听
			if event.type == pygame.QUIT:
				keepGoing = False
			elif event.type == pygame.MOUSEBUTTONUP:	#记录鼠标点击位置
				print(pygame.mouse.get_pos())
		screen.blit(background, (0, 0))
		pygame.display.flip()
		
main()