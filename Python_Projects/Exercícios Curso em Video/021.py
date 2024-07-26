#Write a program that can plays a song in mp3 located in the same folder that this code
import pygame, time
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('usefulCeV/Song_EX021.wav')
pygame.mixer.music.play()
#pygame.event.wait()          just played with time.sleep bellow

time.sleep(15)

input() #wait
