import Image, ImageDraw



image = Image.open("bfs_elipse_bordes.png")

ima1 = image.load()

alto, ancho = image.size

color = []

pto = []



for i in range(ancho):

  for j in range(alto):

		if (ima1[i, j] not in color):

			if (ima1[i, j] != (255,255,255)):

				color.append(ima1[i, j])

				color.append(1)

				pto.append((i, j))

		elif(ima1[i,j] in color):

			ps = color.index(ima1[i, j])

			color[ps + 1] += 1

dimencion = alto*ancho

print "\n", dimencion



dibujo = ImageDraw.Draw(image)

a = 0 

for i in range(0, len(color),2):

	dibujo.text(ps[a], (str(round((color[i+1]/float(dimencion))*100))+"%"), fill = "rgb(0,255,0)")

	a += 1

image.save("porcentaje_elipse_bordes.png")

			
