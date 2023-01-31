#Programa que abra e reproduza o áudio um arquivo mp3

import pygame  #Módulo de criar jogos, contém método para musicas
pygame.init() #Iniciando pygame
pygame.mixer.music.load('exercicio19.mp3') #Seleciona a música
pygame.mixer.music.play() #Toca a música
pygame.event.wait() #Espera a música acabar e fecha o programa, wait = esperar
#Não funciona por falta de coisas no sistema
#Outro método

