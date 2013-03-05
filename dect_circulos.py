import pygame, sys, os
from pygame.locals import*
import Image
from sys import argv
from math import sqrt, sin, cos, fabs
import numpy
import math

def circulos():
  
	image=Image.open("circulo_bordes.jpg")
	foto=image.load()
	x,y=image.size
	r=int(argv[1])
	vote = numpy.empty((x,y))
	
	sobelx = ([-1,0,1],[-2,0,2],[-1,0,1])
	sobely = ([1,2,1],[0,0,0],[-1,-2,-1]) 
    
	for i in range(x):
		for j in range (y):
			sx=0.0
			sy=0.0
			for a in range(len(sobelx)):
				for b in range(len(sobely)):
					try:
						m_x = sobelx[a][b] * image[i+a, j+b][0]
						m_y = sobely[a][b] * image [i+a, j+b][0]
					except:
						m_x = 0
						m_y = 0
					sx = m_x + sx						 	
					sy = m_y + sy
			gradiantx = pow(sx,2)
			gradianty = pow(sy,2)
			gradiant = int(math.sqrt(gradiantx + gradianty))
			
			if fabs (gradiant) > 0:
				costh = (float(sx/gradiant)) 
				senth = (float(sy/gradiant))
				xg = int(round(i - r * costh))
				yg = int(round(j - r * senth))
				
				if xg >= 0 and xg < x and yg >= 0 and yg < y:
					vote [xg][yg] += 1		
			
	maximo = 0
	suma = 0.0
	print "suma"
	for  i in range (y):
		for j in range (x):
			vo = vote [j][i]
			suma += vo
			if vo > maximo: 
				maximo = vo
	prom =  suma / (x*y)
	um  = maximo - prom 
	print "detected"
	for i in range (y):
		for j in range (x):
			vo = vote [j][i]
			if vo > um:
				print 'centro en (%d ,%d) ' %(i,j)	
				image [i,j] = (255,0,0)

	new = 'circulos_new.jpg'
 	d = image.save(new)
	return new, gradiantx, gradianty
 			
def main():

    pygame.init()
    screen = pygame.display.set_mode((300,300))
    foto = circulos()
    imagen = pygame.image.load(foto)

    while True:
  	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()



        screen.blit(imagen,(0,0))
        pygame.display.update()

main()
