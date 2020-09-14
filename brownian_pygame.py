# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 21:12:56 2020

@author: deepa
"""
import pygame
import numpy as np

# Initialize the game
pygame.init()

#Set display
pygame.display.set_caption("Brownian Motion")
screen = pygame.display.set_mode((600,600))

#help(particle)

#type(screen)
start_x=280
start_y=280
particle_x=start_x
particle_y=start_y
particle2_x=start_x
particle2_y=start_y
vel2_x=1
vel2_y=1
running=True

while running:
    #pygame.time.delay(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            #pygame.quit()
    screen.fill((0,0,0))
    
    if particle_x>600:
        particle_x=1200-particle_x
    if particle_x<0:
        particle_x=-particle_x
    if particle_y>600:
        particle_y=1200-particle_y
    if particle_y<0:
        particle_y=-particle_y
        
    if particle2_x>600:
        particle2_x=1200-particle2_x
        vel2_x=-vel2_x
    if particle2_x<0:
        particle2_x=-particle2_x
        vel2_x=-vel2_x
    if particle2_y>600:
        particle2_y=1200-particle2_y
        vel2_y=-vel2_y
    if particle2_y<0:
        particle2_y=-particle2_y
        vel2_y=-vel2_y
        
    start_point=pygame.draw.circle(screen,(0,250,0),(int(start_x),int(start_y)),4)
    particle=pygame.draw.circle(screen,(250,0,0),(int(particle_x),int(particle_y)),4)
    particle2=pygame.draw.circle(screen,(0,0,250),(int(particle2_x),int(particle2_y)),4)
    particle_x=particle_x+np.random.normal(0,1)
    particle_y=particle_y+np.random.normal(0,1)
    particle2_y=particle2_y+np.random.normal(0,1)
    particle2_x=particle2_x+np.random.normal(0,1)
    pygame.display.update()
pygame.quit()
