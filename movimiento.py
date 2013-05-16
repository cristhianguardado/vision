import pygame, sys
from pygame.locals import *
import time

pygame.init()

ancho_ventana = 500
alto_ventana = 500
ventanaSurface = pygame.display.set_mode((ancho_ventana, alto_ventana), 0, 32)

b_izq = 1
b_der = 5
s_izq = 7
s_der = 9
mueve_rect = 4

blanco = (255,255,255)
naranja = (255,69,0)
verde = (0,128,0)
amarillo = (255,255,0)

fig_1 = {'rect':pygame.Rect(300, 80, 50, 100), 'color':naranja, 'dir':s_der}
fig_2 = {'rect':pygame.Rect(300, 80, 60, 100), 'color':verde, 'dir':s_izq}
fig_3 = {'rect':pygame.Rect(300, 80, 60, 100), 'color':amarillo,'dir':b_izq}
rect = [fig_1, fig_2, fig_3]

while True:
  for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	ventanaSurface.fill(blanco)

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
		if fig['rect'].bottom > ancho_ventana:
			if fig['dir'] == b_izq:
				fig['dir'] = s_izq
			if fig['dir'] == b_der:
				fig['dir'] = s_der
		if fig['rect'].left < 0:
			if fig['dir'] == b_izq:
				fig['dir'] = b_der
			if fig['dir'] == s_der:
				fig['dir'] = s_der
		if fig['rect'].right > alto_ventana:
			if fig['dir'] == b_der:
				fig['dir'] = b_izq
			if fig['dir'] == s_der:
				fig['dir'] = s_izq

		pygame.draw.rect(ventanaSurface, fig['color'], fig['rect'])
	pygame.image.save(ventanaSurface,'movimiento.png')
	pygame.display.update()
	time.sleep(0.02)
