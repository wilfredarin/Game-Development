import pygame

pygame.init()

white = (255,255,255)
black  = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.fill(black)


#pixel by pixel drawing
pixAr = pygame.PixelArray(gameDisplay)#entire displays pixel
pixAr[10][20] = green

pygame.draw.line(gameDisplay,blue,(100,200),(300,450),5)
#start end width

pygame.draw.rect(gameDisplay,red,(400,400,50,25))
#where u want to draw gameDisplay   startx,y width height

pygame.draw.circle(gameDisplay,white,(150,150),75)
#center n radius

pygame.draw.polygon(gameDisplay,green,((25,75),(76,125),(250,375),(400,25),(65,40)))
#points in tuple

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

	pygame.display.update()
