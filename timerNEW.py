## Timer
## Written in Python3 by Benjamin Massey
## Protected under the MIT License, see the License file for more info.

## Going to be using the time module in order to keep track of time.
import time

## Going to be using one main function to track the time
## Everything is set up with parameters that will be defined based on user input.
def timeKeep(startS, startM, startH, direction, stopS, stopM, stopH, end, oppEnd):
    ## s, m, and h will be our current number of seconds, minutes and hours.
	s = startS
    m = startM
    h = startH
	
	## Want to start the program running.
    run = True
    
    while run:
		## Direction is going to be defined by whether we are counting up or down,
		## so it will be adding or subtracting 1 to the current seconds after
		## pausing the program for 1 second with time.sleep(1)
        time.sleep(1)
        s = s + direction
        
		## The following ifs are just to change the structure of displaying the
		## time based on where 0s should be placed. This is also where the current
		## time is being printed. It is even where we check whether or not the
		## specified stop time has been reached.
        if m < 10 and s < 10:
            print(str(h) + ":0" + str(m) + ":0" + str(s))
            if s == stopS and m == stopM and h == stopH:
                run = False
                print("Your time is up!")

        if m >= 10 and s < 10:
            print(str(h) + ":" + str(m) + ":0" + str(s))
            if s == stopS and m == stopM and h == stopH:
                run = False
                print("Your time is up!")

        if m < 10 and s >= 10:
            print(str(h) + ":0" + str(m) + ":" + str(s))
            if s == stopS and m == stopM and h == stopH:
                run = False
                print("Your time is up!")

        if m >= 10 and s >= 10:
            print(str(h) + ":" + str(m) + ":" + str(s))
            if s == stopS and m == stopM and h == stopH:
                run = False
                print("Your time is up!")
        
		## Keep seconds under 60.
        if s == end:
            m = m + direction
            s == oppEnd

## Find out what direction the user wants the timer to count.
print("Would you like to count up or down?")

directInp = input("Up or Down?:" )

## Figure out whether or not we are going to be counting up or down.
if directInp == "Up":
	## Find stopping point.
    print("When would you like to stop?")
    inpH = int(input("Hours: "))
    inpM = int(input("Minutes: "))
    inpS = int(input("Seconds: "))
	## Perform the main function.
    timeKeep(0, 0, 0, 1, inpS, inpM, inpH, 59, 0)

if directInp == "Down":
	## Find starting point.
    print("When would you like to start?")
    inpH = int(input("Hours: "))
    inpM = int(input("Minutes: "))
    inpS = int(input("Seconds: "))
	## Perform the main function.
    timeKeep(inpS, inpM, inpH, -1, 0, 0, 0, 0, 59)

