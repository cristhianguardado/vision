import pygame, sys, os

from pygame.locals import*

import Image



def escalagris():

	

	image = Image.open("imagen.jpg")

	foto = image.load()

	x,y = image.size

	for i in range(x):

		for j in range(y):

			a = foto[i,j]

			rgb = (a[0] + a[1] + a[2])/3			

			foto[i,j] = (rgb, rgb, rgb)

	new = 'escalagris.jpg'

	image.save(new)
	return new



def umbral():

	image1 = Image.open("imagen.jpg")

	foto1 = image1.load()

	x1,y1 = image1.size

	for i in range(x1):

		for j in range(y1):

			a1 = foto1[i,j]

			rgb = (a1[0] + a1[1] + a1[2])/3			
			if rgb < 75:

				foto1 [i,j] = (0,0,0)

			else:

				foto1 [i,j] = (255,255,255)

	new = 'binarizacion75.jpg'

	image1.save(new)

	return new

 			



def main():

	pygame.init()

	screen = pygame.display.set_mode((300,300))

	foto = escalagris()
	foto1 = umbral()
	imagen = pygame.image.load(foto)

	imagen1 = pygame.image.load(foto1)
	while True:

		for event in pygame.event.get():

				if event.type == pygame.QUIT:

					sys.exit()



		screen.blit(imagen,(0,0))

		screen.blit(imagen1,(0,0))

		pygame.display.update()

	





main()
