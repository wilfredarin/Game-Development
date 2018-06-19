import pygame
import time
import random


x =pygame.init()

display_width = 800
display_height = 600


#color define RGB 256 choices
black = (0,0,0)  
white = (255,255,255)	
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
block_color = (51, 102, 255)











gameDisplay = pygame.display.set_mode((display_width ,display_height))
pygame.display.set_caption("A bit Racey")
#game clock 
clock = pygame.time.Clock()
#load image
carimg = pygame.image.load("car.png") 


car_width = 146 #pixels
car_height  = 189 
car_speed = 16


def things_doged(count):
	font = pygame.font.SysFont(None,25)
	text  = font.render("Doged: "+str(count),True,black)
	#display it
	gameDisplay.blit(text,(0,0))

def things(thingx,thingy,thingw,thingh,color):
	#things 
	pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])
	#where we want to draw gameDisplay

def car(x,y):
	gameDisplay.blit(carimg,(x,y))#it will display at x,y

def text_objects(text,font):
	textSurface  = font.render(text,True,black)
	return textSurface,textSurface.get_rect()#to get rect around the txt  to possition

def msg_display(text):
	largeText = pygame.font.Font("freesansbold.ttf",100)
	TextSurf,TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf,TextRect)
	#update
	pygame.display.update()

	time.sleep(2) #display for 2 seconds
	gameloop()

def crash():
	msg_display("you crashed")

def game_intro():
	intro = True

	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.fill(white)
		largeText = pygame.font.Font("freesansbold.ttf",100)
		TextSurf,TextRect = text_objects("A bit Racey", largeText)
		TextRect.center = ((display_width/2),(display_height/2))
		gameDisplay.blit(TextSurf,TextRect)
		pygame.display.update()
		clock.tick(15)










def gameloop():
	x = (display_width*0.45)
	y = (display_height*.78)



	#crashed = False 
	gameExit = False
	x_change = 0


	#random draw things
	thing_startx = random.randint(0,display_width)
	thing_starty = -600
	thing_speed = 4 #pix each time off
	thing_height = 100
	thing_width = 100

	count = 0

	
	while not gameExit:

		for event in pygame.event.get():
			#ask if user wants to quit

			if event.type == pygame.QUIT:
				#x pressed of window it will quit
				
				gameExit = True 
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -car_speed
				elif event.key == pygame.K_RIGHT:
					x_change = car_speed

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0


		x+=x_change


		#game background it should be before car else car white
		gameDisplay.fill(white)

		



		
		
		things(thing_startx,thing_starty,thing_width,thing_height,block_color)
		thing_starty+=thing_speed 
		car(x,y)
		things_doged(count)

	
		if thing_starty > display_height:#off the screen
			thing_starty = 0-thing_height
			thing_startx = random.randint(0,display_width-thing_width)#so comes at different places
			count+=1
			thing_speed+=1
			#thing_width+=(count)*1.2
		
		if x>display_width - car_width or x<0:
			crash()

		if y < thing_starty + thing_height 	:
			if x > thing_startx and x < thing_startx+thing_width or x + car_width>thing_startx and x + car_width< thing_startx+thing_width:
				crash()



		#we'll update our events
		pygame.display.update()

		

		clock.tick(60)

	


game_intro()
#uninitiate pygame
gameloop()
pygame.quit()#stops
quit()