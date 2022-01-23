import time

# Countdown timer

def countdown(t):
    while t: # while t > 0
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r") # overwrite previous line
        time.sleep(1)
        t-= 1
    print("kai zen!",'\a')
t = input("Enter time in seconds: ")

countdown(int(t))


# Pomodoro timer
def pomodoro():
    print("Start a task, focus!")
    for i in range(4):
        t = 25*60
        while t:
            mins = t // 60
            secs = t % 60
            timer = '{:02d}:{:02d}'.format(mins, secs) 
            print(timer, end="\r") # overwrite previous
            time.sleep(1)
            t -= 1
        print("Take a Break",'\a')
        
        t = 5*60
        while t:
            mins = t // 60
            secs = t % 60
            timer = '{:02d} : {:02d}'.format(mins, secs)
            print(timer, end='\r')
            time.sleep(1)
            t -= 1
        print("Return to task, focus.",'\a')
        
pomodoro()
            