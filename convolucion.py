import pygame, sys, os
from pygame.locals import*
import Image
from time import *
import math



def bordes():
    t = time()
    image = Image.open("borrosa.jpg")
    foto = image.load()
    alto, ancho = image.size
    
    sobelx = ([-1,0,1],[-2,0,2],[-1,0,1])
    sobely = ([1,2,1],[0,0,0],[-1,-2,-1]) 
    
    for i in range(alto):
        for j in range(ancho):
            #a = foto1[i,j]
            gradiantx, gradianty = 0,0
            for a in range(len(sobelx)):
                for b in range(len(sobely)):
                    try:
                        gradiantx += sobelx[a][b] * foto[i+a, j+b][0]
                        gradianty += sobely[a][b] * foto[i+a, j+b][0]
                    except:
                        gradiantx += 0
                        gradianty += 0
            gradiant = int(math.sqrt(pow(gradiantx,2)+pow(gradianty,2)))
            if gradiant <= 0:
                gradiant = 0
            
      elif gradiant >= 255:
                gradiant = 255
            
	    foto[i,j] = (gradiant, gradiant, gradiant)
    
    new = 'bordes.jpg'
    d=image.save(new)
    ti = time()
    tf = ti - t
    print "Tiempo"+str(tf)+" segundos"
    return new

def main():

    pygame.init()
    screen = pygame.display.set_mode((300,300))
    foto = bordes()
    imagen = pygame.image.load(foto)

    while True:
  	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()



        screen.blit(imagen,(0,0))
        pygame.display.update()

main()
