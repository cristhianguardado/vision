import pygame, sys, os

from pygame.locals import*

import Image

import random 

from time import *



def sal_pimienta():

	t = time()

	image = Image.open("tig.jpg")

	foto = image.load()

	x,y = image.size



	for i in range(x):

		for j in range(y):

			K = random.randint(0,255)		

			if (K%15 == 0):

				#cambio = 255

				foto[i,j] = (255,255,255)
				#print foto[i,j]

			elif(K%15 == 1):

				#cambio = 0

				foto[i,j] = (0,0,0)

				#print foto[i,j]	
		

	new = 'salpimienta4.jpg'

	image.save(new)

	ti = time()

   	tf = ti - t

    	print "Tiempo   "+str(tf)+" segundos"

	return new





def main():

	pygame.init()

	screen = pygame.display.set_mode((300,300))

	foto = sal_pimienta()

	imagen = pygame.image.load(foto)

	

	while True:

		for event in pygame.event.get():

				if event.type == pygame.QUIT:

					sys.exit()



		screen.blit(imagen,(0,0))

		pygame.display.update()

	





main()
