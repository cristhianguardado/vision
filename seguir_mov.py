import pygame, sys, time
from pygame.locals import *
import Image
import numpy

img='movimiento.png'
ancho = 500
alto = 500
ventana = None
 
def abrir_imagen():
  imagen = Image.open('movimiento.png')
	foto = imagen.load()
	return foto

def detectar_mov(pix1,pix2):
	global img,ancho,alto
	pix=[pix1,pix2]
	for p in pix:
		obt_pix(p)
	return

def formas(pix):
	image = filtro(pix)
	image_c,minimo,maximo,gx,gy,conv = mascara(image)
	pix_n = normalizar(image_c,minimo,maximo,conv)
	pix_b = binarizar(pix_n)
	deteccion(pix_b,pix_b)

def deteccion(img,im):
	imagen,masa,centros = colorear(img,im)
	return masa,imagen,centros

def colorear(im,imag):
    foto = im.load()
    global ancho,alto
    porc=[]
    fondos=[]
    centro=[]
    masa=[]
    ancho,alto = im.size
    pixeles = ancho*alto
    c = 0
    pintar = []
    f = 0
    m = []
    for i in range(ancho):
        for j in range(alto):
            pix = foto[i,j]
            r,g,b= random.randint(0,255),random.randint(0,255), random.randint(0,255)
            fondo = (r,g,b)
            if (pix==(0,0,0)):
                c +=1
                origen=(i,j)
                num_pixeles,abscisa,ordenada,puntos=bfs(pix,origen,imag,fondo)
                p=(num_pixels/float(pixeles))*100
                if p>.3:
                    centro=(sum(abscisa)/float(num_pixeles),sum(ordenada)/float(num_pixeles))
                    masa.append(num_pixeles)
                    porcentajes.append(p)
                    fondos.append(fondo)
                    centro_masa.append(centro)
    print centro
    im.save('formas.png')
    return im,m,centro_masa

def bfs(pix,origen,im,fondo):
    foto = im.load()
    cola=list()
    lista = [-1,0,1]
    abscisa = []
    ordenada = []
    pts = []
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
                                puntos.append((a,b))
                    except IndexError:
                        pass
    return num,abscisa,ordenada,puntos

def obtener_pix(m):
	global ancho,alto
	analis=numpy.empty((ancho, alto))
	for i in range(ancho):
		for j in range(alto):
			print analis[i,j]
			print 'i',i
			print 'j',j
			r,g,b = m[i,j]
			print type(r)
			print type(g)
			print type(b)
			raw_input()
			analis[i,j]=(r,g,b)
	return analis

def filtro(pix):
    escala(pix)
    raw_input()
    foto = image.load()
    ancho, alto =image.size
    lista = [-1,0,1]
    for i in range(ancho):
        for j in range(alto):
            prom = self.vecino(i,j,listas,self.analis)
            foto[i,j] = (prom,prom,prom)
    return image
    image = filtro(pix)

def normalizar(image,minimo,maximo,conv):
    foto = image.load()
    global anocho,alto
    r = maximo-minimo
    prop = 255.0/r
    for i in range(ancho):
        for j in range(alto):
            p =int(floor((conv[i,j]-minimo)*prop))
            foto[i,j]=(p,p,p);
    image.save('normalizar.png')
    return image

def binarizar(img):
    global anocho,alto
    foto=img.load()
    img.save('para.png')
    minimo = int(argv[1])
    for i in range(ancho):
        for j in range(alto):
         	if pixels[i,j][0] < minimo:
                p=0
            else:
                p= 255
            foto[i,j]=(p,p,p)
    img.save('binarizar.png')
    return img

def mascara(image):
    sobelx = ([-1,0,1],[-2,0,2],[-1,0,1]) 
    sobely = ([1,2,1],[0,0,0],[-1,-2,-1])     
    pixels,minimo,maximo,gx,gy,conv=convolucion(sobelx,sobely,image)
    return pixels,minimo,maximo,gx,gy,conv

def convolucion(sobelx,sobely,image):
    foto = image.load()
    ancho, alto = image.size 
    m = len(sobelx[0])
    conv = np.empty((ancho, alto))
    gx = numpy.empty((ancho, alto))
    gy = numpy.empty((ancho, alto))
    minimo = 255
    maximo = 0
    for x in range(ancho):
        for y in range(alto):
            sumax = 0.0
            sumay = 0.0
            for i in range(m): 
                for j in range(m): 
                    try:
                        sumax +=(foto[x+i,y+j][0]*sobelx[i][j])
                        sumay +=(foto[x+i,y+j][0]*sobely[i][j])

                    except:
                        pass
            gradiente = math.sqrt(pow(sumax,2)+pow(sumay,2))
            conv[x,y]=gradiente
            gx[x,y]=sumax
            gy[x,y]=sumay
            gradiente = int(gradiente)
            foto[x,y] = (gradiente,gradiente,gradiente)
            p = gradiente
            if p <minimo:
                minimo = p
            if  p > maximo:
                maximo = p
    image.save('convolucion.png')
    return image,gx,gy,minimo,maximo,conv

def vecindad(i,j,lista,image):
    foto = image.load()
    promedio = 0
    indice  = 0
    for x in lista:
        for y in lista:
            a = i+x
            b = j+y
            try:
           		if pixels[a,b] and (x!=a and y!=b):
                    promedio += pixels[a,b][0] 
                    indice +=1            
            except IndexError:
                pass
    try:
        promedio = int(promedio/indice)
        return promedio
    except ZeroDivisionError:
        return 0

def escala(pix):
    global ancho,alto
    foto = pix
    analis = numpy.empty((ancho, alto))
    for i in range(ancho):
        for j in range(alto):
            (r,g,b) = foto[i,j]
            escala_gris = (r+g+b)/3
            foto[i,j] = (escala_gris,escala_gris,escala_gris)
            analis[i,j] = int(escala_gris)
    im = Image.fromarray(foto)
    im.save()
    return image 

def main():
	anterior=None
	siguiente=None
	global img
	pygame.init()
	ancho = 500
	alto = 500
	ventana= pygame.display.set_mode((ancho, alto), 0, 32)
	
	b_izq = 1
	b_der = 5
	s_izq = 7
	s_der = 9
	
	mueve_rect = 4
	naranja = (255,69,0)
	verde = (0,128,0)
	amarillo = (255,255,0)
    
	fig = {'rect':pygame.Rect(50, 50,50, 50), 'color':naranja,'dir':s_der}	
	rect = [fig]
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		ventana.fill((255,255,255))

		for fig in rect: 
        
			if fig['dir'] == b_izq:
				fig['rect'].left -= mueve_rect
				fig['rect'].top += mueve_rect
			if fig['dir'] == b_der:
				fig['rect'].left += mueve_rect
				fig['rect'].top += mueve_rect
			if fig['dir'] == s_izq:
				fig['rect'].left -= mueve_rect
				fig['rect'].top -= mueve_rect
			if fig['dir'] == s_der:
				fig['rect'].left += mueve_rect
				fig['rect'].top -= mueve_rect
	
			if fig['rect'].top < 0: 
				if fig['dir'] == s_izq:
					fig['dir'] = b_izq
				if fig['dir'] == s_der:
					fig['dir'] = b_der
			if fig['rect'].bottom > ancho:
				if fig['dir'] == b_izq:
					fig['dir'] = s_izq
				if fig['dir'] == b_der:
					fig['dir'] = s_der
			if fig['rect'].left < 0:
				if fig['dir'] == b_izq:
					fig['dir'] = b_der
				if fig['dir'] == s_der:
					fig['dir'] = s_der
			if fig['rect'].right > alto:
				if fig['dir'] == b_der:
					fig['dir'] = b_izq
				if fig['dir'] == s_der:
					fig['dir'] = s_izq
	
		pygame.draw.rect(ventana, fig['color'], fig['rect'])
		pygame.image.save(ventana,img)
		if anterior==None:
			pix_a = abrir_imagen()
			anterior = pix_a
			print 'anterior',anterior
		else:
			pix_s = abrir_imagen()
			siguiente = pix_s
			print 'siguiente'
			ddetectar_mov(pix_a,pix_s)
			anterior = siguiente            
			print 'detect'
		raw_input()
		pygame.display.update()
		time.sleep(0.02)
main()
