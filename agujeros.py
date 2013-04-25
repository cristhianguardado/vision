import Image, ImageDraw

import random 

from sys import argv


def histo(image, hor, ver):
	plt.clf()
	fig = plt.subplot(111)
	topx = max(hor)
	topy = max(ver)
	x, y = image.size
	
	if x > y:
		z = x
	else:
		z = y

	if topx > topy:
		top = topx	
	else:
		top = topy
	
	print "horizontal", hor
	print "vertical", ver
	
	plt.limy(-0.1 * top, top * 1.1)
	plt.limx(-0.1 * n, 1.1 * n)	
	plt.title('Histograma')
	xx = range(1, x + 1)	
	yy = range (1, y + 1)
	plt.plot(xx, hor, 'r-', linewidth = 2, label = 'horizontal')
	plt.plot(yy, ver, 'b-', linewidth = 2, label = 'vertical')
	box = fig.get_position([box.x0, box.y0 + box.height * 0.1,box.width,fancybox = True, shadow = True, ncol = 1) box.height * 0.9])
	fig.legend(loc = 'upper center', bbox_to_anchor=(0.5, -0.05),
	
	plt.show()
	return histo
	


def cruce(image):

	#image = Image.open("agujero_bordes.png")

	foto = image.load

	x,y = image.size

	ver = []	

	hor = []

	for i in range(y):

		suma = 0

		for j in range(x):

			suma += sum(foto[i, j])/3

		hor.append(suma)



	for i in range(x):

		suma = 0

		for j in range(y):

			suma += sum(foto[i,j])/3

		ver.append(suma)

	

	print "valores en x = ", len(hor)

	print "valores en y = ", len(ver)

 

	mh = local_minimum(hor)

	mv = local_minimum(ver)



	mh = mh[-26:]

	mv = mv[-26:]



	print len(mh), len(mv)



	ptsx = []

	ptsy = []

	lineas_h = []

	lineas_v = []

	

	for i in range(len(mh)):

		lineas_h.append(hor.index(mh[i]))

	

	for i in range(len(mv)):

		lineas_v.append(ver.index(mv[j]))

	

	for i in range(x):

		for j in range(len(lineas_h)):

			foto[i, lineas_h[j]] = (0, 0, 255)

			ptsx.append(lineas_h[i], j)

	

	for i in range(len(lienas_v)):

		for j in range(y):

			foto[i, lineas_v[j]] = (0, 0, 255)

			ptsy.append(lineas_y[i], j)

	

	image.save("cruce.png")

	return ptsx, ptsy, hor, ver



def local_minumum(histo):

	minimo = list()

	minimum = sum(histo)/len(histo)

	for i in range(1, len(histo)-1):

		if histo[i-1] > histo[i] and histo[i+1] > histo[i]:

			if(histo[i] < minimum):

				minimo.append(histo[i])

	return minimo



def bfs(imaage2,relleno,i,j):

	foto = image2.load()

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

	

	image2.save("bfs_agujeros.png")

ima1 = argv[1]

def main():

	image = Image.open(ima1)

	ptsx, ptsy = cruce(image)
	histo(image, hor, ver)

	c = []

	image2 = Image.open("agujero_bordes.png")

	x,y = image2.size

	t = x*y

	foto2 = image2.load()

	for i in range(x):

		for j in range(y):

			relleno = (random.randint(0,256),random.randint(0,256),random.randint(0,256))

			if foto2 [i,j] == (0,0,0):

				image3, z, c_1, c_2 = bfs(imaage2,relleno,i,j)

				prom = float(z)/float(t)*100.0

				if (1.0 < prom < 15.0):

					c.append(sum(c_1)/len(c_1), sum(c_2)/len(c_2))

	

	ptsx = []

	for i in range(len(ptsx)):

		ptsx.append(ptsx[i][0])

	

	ptsy = []

	for i in range(len(ptsy)):

		ptsy.append(ptsy[i][1])

	

	agujero = []

	for i in range(len(c)):

		if (c[i][0] in ptsx or c [i][1] in ptsy):

			agujero.append(c[i])

	

	print "\nnumero de agujeros: ",len(agujero)



	foto3 = image3.load()

	rellenos = []

	for c in range(len(agujero)):

		rellenos.append(foto3[agujero[c]])



	medida = 0

	medidas = []

	

	for c in range(len(rellenos)):

		for i in range(x):

			for i in range(y):	

				if (foto3[i, j] == rellenos[c]):

					medida += 1

					foto3[i, j]	= (102, 15, 130)

		medidas.append(medida)



	draw = ImageDraw.Draw(image3)

	for i in range(len(agujero)):

		print "centro ", i+1, "en (x,y)= ", agujero[i], "con medida de ", (medidas[i]/float(t))*100, "%"

		x = agujero[i][0]

		y = agujero[i][1]

		draw.elipse((x-2,y-2,x+2,y+2), fill = (255,255,0))

		draw.text((x + 10, y), str(i + 1), fill = (0,0,0))

	

	image3.save("bfs_final.png")

main()

		
