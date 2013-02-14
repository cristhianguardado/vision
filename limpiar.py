import pygame, sys, os

import pygame, sys, os

from pygame.locals import*

import Image

import random 

from time import *



def eliminar():

	t1 = time()

	image = Image.open("salpimienta4.jpg")

	foto1 = image.load()

	x,y = image.size

	b = 0

	 

	for i in range(x):

		for j in range(y):

		  prom = 0

		  b = 0

		  

		  

		  if(foto1[i,j] == (255,255,255) or foto1[i,j] == (0,0,0)):

			#print '*'

			try: 

			   if (foto1[i-1,j]):
				#print '*'

				if(foto1[i-1,j]==(255,255,255) or foto1[i-1,j] == (0,0,0)):

					prom+=0
					#print '*'

				else:

					prom += foto1[i-1,j][0]

					b += 1
					#print '*'

			except:

			   pass



			try: 

			   if (foto1[i+1,j]):

				if(foto1[i+1,j]==(255,255,255) or foto1[i+1,j] == (0,0,0)):

					prom += 0

				else:

					prom += foto1[i+1,j][0]

					b += 1 

			except:

			   pass

			try: 

			   if (foto1[i,j-1]):

				if(foto1[i,j-1]==(255,255,255) or foto1[i,j-1] == (0,0,0)):

					prom += 0

				else:

					prom += foto1[i,j-1][0]

					b += 1

			except:

			   pass

			try: 

			   if (foto1[i,j+1]):

				if(foto1[i,j+1]==(255,255,255) or foto1[i,j+1] == (0,0,0)):

					prom+=0

				else:

					prom += foto1[i,j+1][0]

					b += 1

			except:

			   pass

				

			try:

			    nuevo = prom/b

			    foto1[i,j]=(nuevo,nuevo,nuevo)

			except:

			   pass
			#print nuevo

			#print b	

			#print prom

	

	#print nuevo

	#print b

	#print prom	

	new = 'sinsalpimienta.jpg'

	image.save(new)

	ti = time()

   	tf = ti - t1

    	print "Tiempo"+str(tf)+" segundos"

	return new





def main():

	pygame.init()

	screen = pygame.display.set_mode((300,300))

	foto1 = eliminar()

	imagen1 = pygame.image.load(foto1)

	

	while True:

		for event in pygame.event.get():

				if event.type == pygame.QUIT:

					sys.exit()



		screen.blit(imagen1,(0,0))

		pygame.display.update()

	





main()
