from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame, sys, time

pygame.mixer.init()
#pygame.mixer.music.load('sounds/Insidious Theme [ ezmp3.cc ].mp3')

#pygame.mixer.music.play()       #(loops = 0, start = 10, fade_ms = 2000)

#input('Enter to exit')

print('1 = sounds/Dead Silence Soundtrack [ ezmp3.cc ].mp3')
print('2 = sounds/Insidious Theme [ ezmp3.cc ].mp3')
print('3 = sounds/John Carpenter - HALLOWEEN Theme [ ezmp3.cc ].mp3')
print('x = exit')


while True : 
    user_input = input('Command : ')
    if user_input == '1' :
        pygame.mixer.music.load('sounds/Dead Silence Soundtrack [ ezmp3.cc ].mp3') 
        pygame.mixer.music.play()
    if user_input == '2' :
        pygame.mixer.music.load('sounds/Insidious Theme [ ezmp3.cc ].mp3') 
        pygame.mixer.music.play()
    if user_input == '3' :
        pygame.mixer.music.load('sounds/John Carpenter - HALLOWEEN Theme [ ezmp3.cc ].mp3') 
        pygame.mixer.music.play()

    if user_input ==  'x':
        sys.exit()


    









#pygame.mixer.music.rewind()
#pygame.mixer.music.stop()
#pygame.mixer.music.get_volume()
#pygame.mixer.music.set_volume(0.5)
###pygame.mixer.music.fadeout(1000)
#pygame.mixer.music.get_pos()

#pygame.mixer.music.queue('Insidious Theme [ ezmp3.cc ].mp3')

