import pygame
import time
import random

pygame.init()

ScreenHeight = 800
ScreenWidth = 600

gameDisplay = pygame.display.set_mode((ScreenHeight, ScreenWidth))
pygame.display.set_caption("surprise :D")

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (66, 179, 244)

clock = pygame.time.Clock()

carImg = pygame.image.load("racecar.png")
car_width = 100
#print(carImg)

def thingsDodged(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render("Score: "+str(count), True, red)
	gameDisplay.blit(text, (0,0))

def Things(thingX, thingY, thingH, thingW, color):
	pygame.draw.rect(gameDisplay, color, [thingX, thingY, thingW, thingH])

def Car(x,y):
	gameDisplay.blit(carImg, (x,y))

def crash():
    message_display('You Crashed')

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',100)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((ScreenWidth/1.5),(ScreenHeight/3))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def game_loop():
	x = (ScreenWidth * 0.45)
	y = (ScreenHeight * 0.6)
	xChange = 0
	carSpeed = 0
	gameExit = False

	thing_startx = random.randrange(0, ScreenWidth)
	thing_starty = -600
	thing_speed = 5
	thing_width = 100
	thing_height = 100
	dodged = 0

	while not gameExit:
		for event in pygame.event.get():
			#print(event)
			if event.type == pygame.QUIT:
				print "Game exited by user"
				pygame.quit()
				quit()


			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					xChange = -5
				elif event.key == pygame.K_RIGHT:
					xChange = 5


			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					xChange = 0

		x += xChange
		#print(x)

		gameDisplay.fill(white)
		Things(thing_startx, thing_starty, thing_width, thing_height, blue)
		thing_starty += thing_speed
		Car(x,y)
		thingsDodged(dodged)

		if x > ScreenWidth + car_width or x < 0:
			crash()

		if thing_starty > ScreenHeight:
			thing_starty = 0
			thing_startx = random.randrange(0,ScreenWidth)
			dodged += 1
			thing_speed += 1

		if y < thing_starty + thing_height:
			if (x > thing_startx and x < thing_startx + thing_width) or (x+car_width > thing_startx and x + car_width < thing_startx+thing_width):
				crash()

		pygame.display.flip()
		clock.tick(60)

game_loop()

pygame.quit()