import pygame, sys, os

from pygame.locals import*

import Image

from math import*

import random

import ImageDraw





def image():

  

	image = Image.open("binarizacion.jpg")

	foto = image.load()

	x,y = image.size

	a = x*y

	porc = []

	foco = []

	tiene = 0

	print x

	print y

	for i in range(x):

		for j in range(y):

			if foto[i,j] == (0,0,0):

				relleno = random.randint(0,255),random.randint(0,255),random.randint(0,255)

				z ,c_1,c_2 = bfs(image,relleno,i,j)

				d = (float(z)/float(a)) * 100.0	

				#print "a"			

				if d > 0.5:

					foco.append((sum(c_1)/len(c_1),sum(c_2)/len(c_2)))

					porc.append([d, (relleno)])

					print "pintar %s"%tiene

					tiene += 1

					#print "a1"

					print 'termino1'



	nuevo = porc.index (max(porc))

	mc = porc[nuevo][1]

	for i in range(x):	

		for j in range(y):

			if foto	[i,j] == mc:

				foto[i,j] = (120,120,120)

	

				#print "a2"

	nueva = 'fondo.jpg'

	image.save(nueva)

	print foco



	draw = ImageDraw.Draw(image)

	r = 0 

	for i in foco:

		draw.ellipse((i[0]-2, i[1]-2,i[0]+2,i[1]+2), fill=(0,0,0))

		draw.text(((i[0]+4,i[1]+4),), str(r), fill=(0,0,0))

		r += 1

		#print "a3"	

	tiene = 0

	for d in porc: 

		print "Porcentaje %d: %.2f"%(tiene, d[0])

		tiene += 1

		#print "a4"

	

	new_1 = 'fondo.jpg'

	image.save(new_1)

	return new_1

	



def bfs(image,relleno,i,j):

	foto = image.load()

	x,y = image.size

	prim = foto[i,j]

	c=[]

	c_1=[]

	c_2=[]

	c.append((i,j))

	z = 0

	while len(c)>0:

		(p,q) = c.pop(0)

		real = foto[p,q]

		if real == prim or real == relleno:

			for px in [-1,0,1]:

				for py in [-1,0,1]:

					xx, zz = (p + px, q + py)

					#print "a5"

					if xx >= 0 and xx < x and zz >= 0 and zz < y: 

						tiene = foto[xx,zz]

						#print "a6"

						if tiene == prim:

							foto[xx,zz] = relleno 

							c_1.append(xx)

							c_2.append(zz)

							z += 1

							c.append((xx,zz))

							#print "a7"

	forma = image.save('formas.jpg')

	return z, c_1,c_2

						

		



def main():

	pygame.init()

	screen = pygame.display.set_mode((300,300))

	foto = image()

	imagen = pygame.image.load(foto)

	

	while True:

		for event in pygame.event.get():

				if event.type == pygame.QUIT:

					sys.exit()



		screen.blit(imagen,(0,0))

		pygame.display.update()

	





main()
