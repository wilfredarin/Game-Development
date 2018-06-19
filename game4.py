#0,0

import pygame
import time
import random


x =pygame.init()

display_width = 800
display_height = 600


#color define RGB 256 choices
black = (0,0,0)  #abscence of color
white = (255,255,255)			# all color
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
block_color = (51, 102, 255)








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
car_speed = 16


def things_doged(count):
	font = pygame.font.SysFont(None,25)
	text  = font.render("Doged: "+str(count),True,black)
	#display it
	gameDisplay.blit(text,(0,0))






#display it where to display?

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

		#pygame.event.get() gets all the event mouse movement
		#key pressing and stuff alll the events 
		#it creates the list of event per frame per second



		for event in pygame.event.get():
			#ask if user wants to quit

			if event.type == pygame.QUIT:
				#x pressed of window it will quit
				
				gameExit = True #out of loop as when crash can play again
				pygame.quit()
				quit()

			#print(event) #prints all the event being tracked
			#this will work only for a single frame



			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -car_speed
				elif event.key == pygame.K_RIGHT:
					x_change = car_speed

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

		



		#after filling the background
		
		#things(thingx,thingy,thingw,thingh,color)
		
		things(thing_startx,thing_starty,thing_width,thing_height,block_color)
		thing_starty+=thing_speed #change y cordinates

		#show car
		
		car(x,y)
		things_doged(count)

		#thing has to start again else gone
		if thing_starty > display_height:#off the screen
			thing_starty = 0-thing_height
			thing_startx = random.randint(0,display_width-thing_width)#so comes at different places
			count+=1
			thing_speed+=1
			#thing_width+=(count)*1.2
		

		if x>display_width - car_width or x<0:
			crash()

					#collison
			
			#if the tip of car 
		if y < thing_starty + thing_height 	:
			#print("y crosover")\\\\
			#leftmost sec of car
			if x > thing_startx and x < thing_startx+thing_width or x + car_width>thing_startx and x + car_width< thing_startx+thing_width:
				#print("x")
				crash()



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







