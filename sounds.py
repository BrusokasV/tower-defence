from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame, sys, time

pygame.mixer.init()
#pygame.mixer.music.load('sounds/Insidious Theme [ ezmp3.cc ].mp3')

#pygame.mixer.music.play()       #(loops = 0, start = 10, fade_ms = 2000)

#input('Enter to exit')

def sound(user_input):
    match user_input:
        case '1' :
            soundeffect = pygame.mixer.Sound("sounds/ghost_out.mp3")
            soundeffect.play()
            soundeffect.set_volume(0.7)
        case '2' :
            soundeffect = pygame.mixer.Sound("sounds/boing_sound.mp3")
            soundeffect.play()
    

def play(user_input): 
    match user_input:
        case '1' :
            pygame.mixer.music.load('sounds/Dead Silence Soundtrack [ ezmp3.cc ].mp3')
            pygame.mixer.music.play(loops=-1)
            pygame.mixer.music.set_volume(0.4)
        case '2' :
            pygame.mixer.music.load('sounds/Insidious Theme [ ezmp3.cc ].mp3') 
            pygame.mixer.music.play()
        case '3' :
            pygame.mixer.music.load('sounds/John Carpenter - HALLOWEEN Theme [ ezmp3.cc ].mp3') 
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.6)
        case 'x':
            pygame.mixer.music.stop()


    









#pygame.mixer.music.rewind()
#pygame.mixer.music.stop()
#pygame.mixer.music.get_volume()
#pygame.mixer.music.set_volume(0.5)
###pygame.mixer.music.fadeout(1000)
#pygame.mixer.music.get_pos()

#pygame.mixer.music.queue('Insidious Theme [ ezmp3.cc ].mp3')

