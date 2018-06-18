import pygame

x =pygame.init()


#dont name your game as pygame ur system gets confused!!!!

#serve a window for the game 
#this is a surface 
#width n height :tuple


#display.set_method used



gameDisplay = pygame.display.set_mode((800,600))

#title of window  .set_caption() method
pygame.display.set_caption("A bit Racey")


#game clock 
clock = pygame.time.Clock()

#

crashed = False


while not crashed:

	#pygame.event.get() gets all the event mouse movement
	#key pressing and stuff alll the events 
	#it creates the list of event per frame per second



	for event in pygame.event.get():
		#ask if user wants to quit

		if event.type == pygame.QUIT:
			#x pressed of window it will quit
			
			crashed = True #out of loop

		print(event) #prints all the event being tracked
					#this will work only for a single frame

#you do a lot of thing in background
#then you push it on screen 
#when all computation is done you display it

	
	#we'll update our events

	pygame.display.update()

	#or u can put a parameter in update(a para) it will update that thing only
	#pygame.display.flip() updates all

	#set frame per second clock.tick(fps) speed controll
	#how fast things move

	clock.tick(60)

	#uninitiate pygame

	pygame.quit()#stops
	quit()







