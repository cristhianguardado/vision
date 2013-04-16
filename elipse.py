import Image, ImageDraw

from sys import argv

import math
import random 

def elipse(imagen):

  ima1 = imagen.load()

	alto, ancho = imagen.size

	cen =  dict()

	centro = []

	frec = dict()

	mat_x = ([-1,0,1],[-2,0,2],[-1,0,1])

	mat_y = ([1,2,1],[0,0,0],[-1,-2,-1])

	Z = []

	Y = []

	

	for i in range(ancho):

		x = []

		y = []

		for j in range(alto):

			gx, gy = 0, 0

			

			for a in range(len(mat_x[0])):

				for b in range(len(mat_y[0])):

                    

					try:

						mul_x = mat_x[a][b] * ima1[i+a, j+b][0]

						mul_y = mat_y[a][b] * ima1[i+a, j+b][0]

                    

					except:

						mul_x = 0

						mul_y = 0

                    

					#sumx = mul_x+sumx

					#sumy = mul_y+sumy

			#sumx = pow(sumx,2)

			#sumy = pow(sumy,2)

			#grad = int(math.sqrt(sumx + sumy))
			gx.append(mul_x)
			gy.append(mul_y)	
			

	return gx,gy

def bfs(imagen, rcolor, alto, ancho, px):
	ima1 = imagen.load()
	(x, y) = px
	original = ima1[x, y]
	cola = [(x, y)] 
	ptos = []
	while len(cola)>0:
		x, y = cola.pop(0)
		real = ima1[x, y]
		if real == original or real == rcolor:
			for dx in [-1, 0, 1]:
				for dy in [-1, 0, 1]:
					selec = (x + dy, y + dx)
					if selec[0] >= 0 and selec[0] < alto and selec[1] >= 0 and selec[1] < ancho:
						contenido = ima1[selec[0], selec[1]]
						if contenido == original:
							ima1[selec[0], selec[1]] = rcolor
							cola.append(selec)
							ptos.append((selec[0], selec[1]))
                            
	return imagen, ptos


def puntos(gx, gy, ptos):
	cont = 0
	for i in range(0, len(gx)):
		if(gx[i] == 0):
			gx.pop(i)
		if(gy[i] == 0):
			gy.pop(i)
	while(cont == 0):
		pto1 = random.randint(0,len(gx)-1)

		pto2 = random.randint(0,len(gx)-1)
		x1, y1 = puntos[pto1]
		x2, y2 = puntos[pto2]
		print x1, y1
		print x2, y2

		m_1 = gy[pto1] / gx[pto1]
		m_2 = gy[pto2] / gx[pto2]

		if (m_1 != 0 and m_2 != 0 and m_1 != m_2):
			cont = 1

	return pend1, pend2		

def main():

	imagen = Image.open("elipse.png")
	gx, gy = elipse(imagen)

	ima1 = imagen.load()
	ancho, alto = imagen.size

	for i in range(ancho):
		for j in range(alto):
			if ima1[i,j] == (0,0,0):
				rcolor = (random.randint(0,256), random.randint(0,256), random.randint(0, 256))
				ima2, ptos = bfs(imagen, rcolor, (i, j), ancho, alto)
	
	
	m_1, m_2 =  ptos_random(gx, gy, ptos)
	print m_1, m_2	

	image.save("elipse_final.png")			

main()
