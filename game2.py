#0,0

import pygame

x =pygame.init()

display_width = 800
display_height = 600


#color define RGB 256 choices
black = (0,0,0)  #abscence of color
white = (255,255,255)			# all color
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)








#dont name your game as pygame ur system gets confused!!!!

#serve a window for the game 
#this is a surface 
#width n height :tuple


#display.set_method used



gameDisplay = pygame.display.set_mode((display_width ,display_height))

#title of window  .set_caption() method
pygame.display.set_caption("A bit Racey")


#game clock 
clock = pygame.time.Clock()

#
#load image

carimg = pygame.image.load("car.png") 
car_width = 146 #pixels
car_height  = 189 #pixels

#display it where to display?

def car(x,y):
	gameDisplay.blit(carimg,(x,y))#it will display at x,y

def gameloop():
	x = (display_width*0.45)
	y = (display_height*.7)



	#crashed = False 
	gameExit = False
	x_change = 0







	while not gameExit:

		#pygame.event.get() gets all the event mouse movement
		#key pressing and stuff alll the events 
		#it creates the list of event per frame per second



		for event in pygame.event.get():
			#ask if user wants to quit

			if event.type == pygame.QUIT:
				#x pressed of window it will quit
				
				gameExit = True #out of loop as when crash can play again

			#print(event) #prints all the event being tracked
			#this will work only for a single frame



			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0

	#change x 
		x+=x_change















	#you do a lot of thing in background
	#then you push it on screen 
	#when all computation is done you display it

		#game background it should be before car else car white
		gameDisplay.fill(white)
		
		#show car
		car(x,y)

		if x>display_width - car_width or x<0:
			gameExit = True
		#we'll update our events
		pygame.display.update()

		#or u can put a parameter in update(a para) it will update that thing only
		#pygame.display.flip() updates all

		#set frame per second clock.tick(fps) speed controll
		#how fast things move

		clock.tick(60)

	



	#uninitiate pygame
gameloop()
pygame.quit()#stops
quit()







