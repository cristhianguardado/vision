import pygame, sys, os
from pygame.locals import*
import Image
from time import *
import math

TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

def turn (pto1,pto2,pto3):
  return cmp((pto2[0] - pto1[0])*(pto3[1] - pto1[1]) - (pto3[0] - pto1[0])*(pto2[1] - pto1[1]), 0)

def convex_hull(pto):
	convex = [min(ptos)]
	for i in range (len(pto)):
		a = [0]
		for j in range (len(pto)):
			b = turn(pto[j], conv[i],)
			if a == conv[i] or b == TURN_LEFT:	
				a = pto [j]
		conv.append(a)
		if a == conv_1[0]:
			break
		return conv			
			
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
					
					if xx >= 0 and xx < x and zz >= 0 and zz < y: 
						tiene = foto[xx,zz]
						
						if tiene == prim:
							foto[xx,zz] = relleno 
							c_1.append(xx)
							c_2.append(zz)
							z += 1
							c.append((xx,zz))
							
	forma = image.save('formas.jpg')
	return z, c_1,c_2
					
def convex():
	image = Image.open("estrella_binarizacion.jpg")

	foto = image.load()

	x,y = image.size
	h = []
	for i in range(x):

		for j in range(y):

			if foto [i,j] == (255,255,255):
				z, c = bfs(image,i,j,(255,0,0))
				h.apppend(conv(c))
		for h in h:
			for pto in h:
				foto[pto] = (0,255,0)
	
	new = 'estrella_escalagris.jpg'

	image.save(new)

	return new	


def main():

	pygame.init()

	screen = pygame.display.set_mode((300,300))

	foto = convex()

	imagen = pygame.image.load(foto)

	while True:

		for event in pygame.event.get():

				if event.type == pygame.QUIT:

					sys.exit()



		screen.blit(imagen,(0,0))

		pygame.display.update()

	





main()
