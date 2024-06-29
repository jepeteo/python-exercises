import sched
import time
import pygame

# init pygame | didn't use playsound due to errors in installation
pygame.init()
pygame.mixer.init()

# int scheduler
scheduler = sched.scheduler(time.time, time.sleep)

def schedule_func(event_time, func, *args):
    delay = event_time - time.time()
    # check time
    if delay < 0:
        print("Time is in the past. Time travel is not yet possible. Please provide a future time!")
        return
    scheduler.enter(delay, 1, func, argument=args)
    print(f'The alarm is scheduled to run in {delay} seconds.')
    scheduler.run
    
def play_alarm_sound(fname):
    pygame.mixer.music.load(fname)
    pygame.mixer.music.play()
    
event_time = time.time() + 10
schedule_func(event_time, play_alarm_sound, 'beep.mp3')

while scheduler.queue:
    scheduler.run(blocking=False)  
    time.sleep(1)

# Wait until the music finishes playing
while pygame.mixer.music.get_busy():
    time.sleep(1)

pygame.mixer.music.stop()
pygame.quit()
