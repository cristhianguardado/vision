import sys, pygame
import Image
from sys import argv
from math import sqrt, sin, cos, fabs
import numpy
from time import*
import math
import ImageDraw
import random



def circulos(imagen):

    image = Image.open(imagen)

	#image=Image.open("muestra_bordes.jpg")

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

			for a in range(len(sobelx[0])):

				for b in range(len(sobely[0])):

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

				xc = int(round(i - r * costh))

				yc = int(round(j - r * senth))
				xcg = (xc + y)/2
				ycg = (x/2)-yc				



				if ycg >= 0 and xcg < y and xcg >= 0 and ycg < x:

					vote [xcg][ycg] += 1		



	for z in range(1,int(round(y*0.1))):
		cont = True
		while cont:
			cont = False 
			for cx in range(x):
				for cy in range(y):
					vo = vote [j][i]
					if vo > 0:
						for  xx in range(-z,z):
							for yy in range(-z,z):
								if not (xx == 0 and yy == 0):
									if cx + yy < x and cx + yy >= 0 and cy + xx >=0 and cy + xx < x:
										vot = vote [cx+yy][cy+xx]
										if vot > o:
											if vo-r>=vot:
												vote[xx][yy] = vo-vot
												vote [cx+yy][cy+xx] = 0
												cont = True
	maximo = 0

	suma = 0.0

	for  i in range (y):

		for j in range (x):

			vo = vote [j][i]

			suma += vo

			if vo > maximo: 

				maximo = vo

	prom =  suma / (x*y)

	um  = (maximo - prom)/2.0
	centro = [] 

	for i in range (y):

		for j in range (x):

			vo = vote [j][i]
			if vo > um:

				print 'centro en (%d ,%d) ' %(i,j)	
				centro.append(i,j)

				image [i,j] = (255,0,0)
	
	draw = ImageDraw.Draw(image)

	x,y = image.size
	m = 0
	for b in range(len(centro)):
		p = centro [c][0]
		q = centro [c][1]
		draw.elipse((p-r, q-r, p+r, q+r),fill=None)
		r += 1
	m += 1
	new = 'circulos_new.jpg'

 	d = image.save(new)

	return new, gradiantx, gradianty

 			

def main():

	imagen = circulos("cir.jpg")

    #pygame.init()

    #screen = pygame.display.set_mode((300,300))

    #foto = circulos()

    #imagen = pygame.image.load(foto)



    #while True:

  	#for event in pygame.event.get():

	#	if event.type == pygame.QUIT:

	#		sys.exit()

	#	screen.blit(imagen,(0,0))

     #   pygame.display.update()



main()

