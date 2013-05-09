import Image

import ImageDraw

from sys import argv

from time import * 

import numpy

import PIL

from math import floor

import math

import random



def binarizar(image):

  foto = image.load()

	x,y = image.size

	mini = int(argv[2])

	for i in range(x):

		for j in range(y):

			if foto [i,j][1]<mini:

				p=0

	image.save('bin.png')

	return image



def normalizar(image):

	foto = imagen.load()

	c = maxi-mini

	prop = 255.0/c

	x,y = imagen.size

	for i in range(x):

		for j in range(y):

			if foto[i,j][0]=!0:

				p=int(flor(foto[i,j][0]-mini)*prop)

				foto[i,j]=(p,p,p)

	imagen.save('normaliza.png')

	return image

	

def diferencia(filtro,escala,mediana):	

	foto = escala.load()

	x,y = escala.size

	minimo=255

	maximo=0

	for i in range(x):

		for j in range(y):

			diferencia=0

			diferencia=medianas[i,j]-matriz[i,j]

			diferencia=int(diferencia)

			foto[i,j]=(diferencia,diferencia,diferencia)

			if diferencia<minimo

				minimo=diferencia

			if diferencia>maximo

				maximo=diferencia

	escala.save('diferencia.png')

	return escala



def esquinas(image):

	ima =Image.open("esquina.png")

	foto = image.load()

	x,y = image.size

	filtro = numpy.empty((x,y))

	lista = [-1,0,1]

	p_medios = numpy.empty((x,y))

	for i in range(x):

		for j in range(y):

			pix=vecindad(i,j,lista,matriz)

			mediana=int(mediana)

			filtro_medio[i,j]=(mediana)			

			foto[i,j] = (mediana,mediana,mediana)

	image.save('esquinas.png')

	return image



def promedio(pix)

	a=len(pix)

	b=sorted(pix)

	if a%2=!0:

		mediana = b[a/2]

	else:

		median=(b[a/2-1]+b[a/2])/2

	return mediana



def vecinos(i,j,lista,matriz):

	pix = []

	for i in lista:

		for j in lista:	

			a = x+i

			b = y+j

			try:

				if a>o and b>0:

					pix.append(matriz[a,b])

			except IndexError:

				pass

	return pix

def funciones():

	image = filtro()

	ima=image.save('filtrada.jpg')

	img = mascara(image)

	id = img.save('mascara.png')

	img= normalizar(img)

	img2 = img.save('normalizada.png')

	im_bin = binarizar(img)

	imbin=img.save('binarizada.png')

	img = cargar_imagen(im_bin)

	return im_bin



def color():

	image = c_color()

	image cargar_imagen(image)

	

def bfs(pix,origen,image,fondo):

	foto=image.load()

	cola=list()

	lista=[-1,0,1]

	abscisa=[]

	ordenada=[]

	cola.append(origen)

	original = foto[origen]

	num=1

	while len(cola) > 0:

		(i,j)=cola.pop(0)

		actual = foto[i,j]

		if actual == original or actual==fondo:

			for x in lista:

				for y in lista:

					a= i+x

					b = j+y 

					try:

						if foto[a,b]:

							contenido = foto[a,b]

							if contenido == original:

								foto[a,b] = fondo

								abscisa.append(a)

								ordenada.append(b)

								num +=1

								cola.append((a,b))

					except IndexError:

						pass

	image.save('bfs.png')

	return num,abscisa,ordenada



def centro_masa(image,centro):

	draw = ImageDraw.Draw(image)

		for i pto in enumerate(centro):

			draw.ellipse(pto[0]-2,pto[1]-2,pto[0]+2,pto[1]+2,fill=(0,0,0)

	image.save('centro,png')

	return



def colocar_gris(image,porcentaje,fondos):

	foto = image.load()

	x,y=image.size

	p = porcentaje.index(max(porcentajes))

	color=fondos[p]

	for i in range(x):

		for j in range(y):

			if foto[i,j] == color:

				foto[i,j]=(95,95,95)

	image.save('grisesss.png')

	return



def colorear(image):

	foto=image.load()

	porcentajes=[]

	fondos=[]

	cen=[]

	x,y=image.size

	t_pixels=x*y

	c=0

	for i in range(x):

		for j in range(y):

			pix = foto[i,j]

			r,g,b= random.randint(0,255),random.randint(0,255),random.randint(0,255)

	fondo=(r,g,b)

	if (pix==(0,0,0)):

	c +=1

	origen=(i,j)

	n,a,m=bfs(pix,origen,image,fondo)

	p=(num_pixels/float(t_pixels))*100

	if p>.10:

		porcentajes.append(p)

		fondos.append(fondo)

		cen.append((sum(a)/float(n),sum(m)/float(n)))

		colocar_gris(image,porcentajes,fondos)

		centro_masa(image,cen)

		imprimir_porcentajes(porcentajes)

	image.save('final.jpg')

	return image



def mascara(image):

	s_x = ([-1,0,1],[-2,0,2],[-1,0,1]) 

	s_y = ([1,2,1],[0,0,0],[-1,-2,-1])     

	ima=convolucion(sobelx,sobely,image)

	return img



def convolucion(h1,h2,image):

        foto = image.load()

        x,y = image.size 

        a=len(h1[0])

        conv = numpy.empty((x,y))

        minimo = 255

        maximo = 0

        for x in range(x):

            for y in range(y):

                sumax = 0.0

                sumay = 0.0

                for i in range(a): 

                    for j in range(a): 

                        try:

                            sumax +=(pixels[x+i,y+j][0]*h1[i][j])

                            sumay +=(pixels[x+i,y+j][0]*h2[i][j])



                        except:

                            pass

                gradiente = math.sqrt(pow(sumax,2)+pow(sumay,2))

                	conv[x,y]=gradiente

                gradiente = int(gradiente)

                pixels[x,y] = (gradiente,gradiente,gradiente)

                p = gradiente

                if p < minimo:

                    minimo = p

                if  p > maximo:

                    maximo = p

        return image



def main():

	image_escala = escala()

		image_filtro, mediana = filtro(image_escala)

		image_dif = diferencia(image_filtro, image_escala,mediana)

		image_norm = normalizar(image_dif)

		image_bin = binarizar(image_norm)

main()
