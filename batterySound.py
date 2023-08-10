import psutil
import time
import pygame


#Function that searches for the file with the sound and plays it
def play_sound(sound_file):
    pygame.init()
    sound = pygame.mixer.Sound(sound_file)
    sound.play()
    pygame.time.wait(3000)  # Play the sound for 3 seconds
    sound.stop()
    pygame.quit()

#Pathname to sound file
#In sound_file you can add your own path to the sound that you want
#Im still learning :)

#SoundFile will be in rep

sound_file = 'new-notification-138807.mp3'
percent = 10
lBatteryCheck = int (0)
while True:
    #For every loop, checks the battery bercentage and stores it...
    battery = psutil.sensors_battery() 
    percent_left = int(battery.percent) # <---- Here
    #If baterry perfecntage is at a number divisible by 10, it plays the sound to notify the user that 
    #battery has decreased a 10 percent

    if (percent_left % 10 == 0 and lBatteryCheck != percent_left): 
        
        play_sound(sound_file)
        lBatteryCheck = percent_left
        
    else:
        time.sleep(300)
