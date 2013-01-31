import pygame, sys, os
from pygame.locals import*
from sys import argv
import Image

def main():
	pygame.init()
	screen = pygame.display.set_mode((300,300))
	imagen = pygame.image.load('descarga.jpg')
	screen = pygame.display.get_surface()
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		screen.blit(imagen,(0,0))
		pygame.display.update()

main()
