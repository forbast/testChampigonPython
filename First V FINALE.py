# -*- coding: cp1252 -*-
import pygame
from pygame.locals import *
from random import randint
import time
import function
     
pygame.init()
#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))
#Chargement et collage du fond
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))
    
# bouleV3
boule = pygame.image.load("bouleV3.jpg").convert_alpha()

     #perdu
perdu = pygame.image.load("perdu.png").convert_alpha()
a = 120
b = 50


#gagne
gagne = pygame.image.load("gagne.png").convert_alpha()
ag = 120
bg = 50

     #bombe
bombe = pygame.image.load("bombe.png").convert()
     
bombe.set_colorkey((255,255,255))
     
     #bombeE
bombeIE = pygame.image.load("bombeE.jpg").convert()
     
     
     
     #Chargement et collage du personnage
perso = pygame.image.load("perso.png").convert_alpha()
     
     #Rafraîchissement de l'écran
pygame.display.flip()
pygame.key.set_repeat(40, 10)
     
pygame.time.Clock().tick(30)
test = 1
while test:
     debut = 0
     val = 0
     compt = 0
     comptB = 0
     bombeEP = 0
     bombeE = 0
     mort = 0
     absBombe = 200
     ordBombe = 200
     abscisse = 240
     ordonne = 320
     absBombe = -2200
     ordBombe = 2200
     absBoule = -5000
     ordBoule = 5000
     #BOUCLE INFINIE
     
     continuer = 1
     while continuer:
         if debut == 1:
             comptB += 1
         for event in pygame.event.get():
             if event.type == QUIT:     
                 continuer = 0
                 test = 0
                 pygame.quit()
             if event.type == KEYDOWN:
                 if event.key == K_DOWN:
                    ordonne += function.reculer(ordonne)
                 if event.key == K_RIGHT:
                         abscisse += function.droite(abscisse)
                 if event.key == K_UP:
                         ordonne += function.avancer(ordonne)
                 if event.key == K_LEFT:
                         abscisse += function.gauche(abscisse)
                 if event.key == K_SPACE:
                     print(abscisse,'  ',ordonne)
                     
                 if event.key == K_RETURN:
                     ordBoule = (ordonne+200)%380
                     absBoule = (abscisse)%550
                     tempD = time.time()
                     compt = 0
                     debut = 1
                     
         #apparition Bombe
     
         
                     
         # colision avec le perso
         if int(ordBoule) < int(ordonne)+30 and int(ordBoule) > int(ordonne)-30 and int(absBoule) < int(abscisse)+30 and int(absBoule) > int(abscisse)-30:
             val = randint(0,3)            
             ordBoule = (ordonne+40)%380
             absBoule = (abscisse+40)%550
             compt +=1
             print(compt)
             if compt == 10:
                 continuer = 0
                 tempF = time.time()  
     
         # rebond sur mur
         if val == 0 and int(ordBoule) == 390:
             val = 1
         if val == 1 and int(absBoule) == 550:
             val = 3
         if val == 3 and int(ordBoule) == 0:
             val = 2
         if val == 2 and int(absBoule) == -5:
             val = 0      
         if val == 1 and int(ordBoule) == 0:
             val = 0
         if val == 0 and int(absBoule) == 550:
             val = 2
         if val == 2 and int(ordBoule) == 390:
             val = 3
         if val == 3 and int(absBoule)  ==  -5:
             val = 1 
         
            
          
         # direction boule 
         if val == 0:
                 absBoule += 0.1
                 ordBoule += 0.1
     
         if val == 1:
                 absBoule += 0.1
                 ordBoule -= 0.1
        
         if val == 2:
                 absBoule -= 0.1
                 ordBoule += 0.1
                 
         if val == 3:
                 absBoule -= 0.1
                 ordBoule -= 0.1     
     #BOMBE
         if bombeE == 0 and comptB == 2000 and debut == 1:
             bombeE = 1
         if bombeE == 1 and comptB == 2200 and debut == 1:    
            absBombe = randint(0,550)
            ordBombe = randint(0,380)
            comptB = 0
            bombeE = 0
         if function.isDead(ordBombe,absBombe,ordonne,abscisse,bombeE,debut):
                 continuer = 0
                 mort = 1    
         
         fenetre.blit(fond, (0,0))
         fenetre.blit(boule,(absBoule,ordBoule))
         fenetre.blit(perso,(abscisse,ordonne))  
         #apparition bombe
         if bombeE == 1 and debut == 1:
             fenetre.blit(bombeIE,(absBombe,ordBombe))
         if bombeE == 0 and debut == 1:
             fenetre.blit(bombe,(absBombe,ordBombe)) 
         pygame.display.flip()
     
     if mort == 0:
         tempT = tempF - tempD
         print('Vous avez gagner en ', tempT,'seconde')
         for i in range(15000):
             fenetre.blit(gagne,(b,a))
             pygame.display.flip()
     if mort == 1:
         for i in range(15000):
             fenetre.blit(perdu,(b,a))
             pygame.display.flip()
         print("MORT")
pygame.quit()
     
     
