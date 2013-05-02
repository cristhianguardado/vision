import Image,ImageTk
import ImageDraw
from math import floor
import math
import random
from sys import argv

def convolucion(x,y,foto):
    t = time()
    image = Image.open("a.png")
    foto = image.load()
    alto, ancho = image.size
    
    sobelx = ([-1,0,1],[-2,0,2],[-1,0,1])
    sobely = ([1,2,1],[0,0,0],[-1,-2,-1]) 
    
    for i in range(alto):
        for j in range(ancho):
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

def bfs(imaage, relleno,i,j):
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
	
	image2.save("formas.png")
ima1 = argv[1]

    
def get_pendientes(self,image):
        Gx=self.gx
        Gy=self.gy
        foto=imagen.load()
        x,y=imagen.size
        pend=numpy.empty((x,y))
        
        for i in range(x):
            for j in range(y):
                
                if Gx[i,j]!=0 and Gy[i,j]!=0:
                    m=0
                elif Gx[i,j]==0 and Gy[i,j]==0:
                    m=1
                elif Gy[i,j]<=0 and Gx[i,j]==0:
                    m=2
                elif Gy[i,j]>=0 and Gx[i,j]==0:
                    m=3
                elif Gx[i,j]<=0 and Gy[i,j]==0:
                    m=4
                elif Gx[i,j]>=0 and Gy[i,j]==0:
                    m=5
                pend[i,j]=m
        return pend

def get_rectas(self,pend,image):
        seg=list()
        foto=img.load()
        x,y =img.size
        for i in range(x):
            for j in range(y):
                if foto[i,j]!=(0,0,0):
                           
                    pend_n=pend[i,j]

                    if pend[i,j]==0:
                        foto[i,j]=(0,0,255)
                    if pend[i,j]==1:
                        foto[i,j]=(55,0,0)
                    if pend[i,j]==2:
                        foto[i,j]=(255,67,34)
                    if pend[i,j]==3:
                        foto[i,j]=(2,45,0)
                    if pend[i,j]==4:
                        foto[i,j]=(9,67,23)
                    if pend[i,j]==5:
                        foto[i,j]=(34,6,67)
 
       
        img.save('prueba.png')

def main():
	image = Image.open(ima1)
	ancho,alto=foto.size
    foto,gradiantx,gradianty = convolucion(x,y,foto)
    pend(foto,x,y,Gx,Gy)
main()
