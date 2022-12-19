# ___________________________________________________________________________________________________________________
# |                                   IMPORTANT                                                                     |
# |                                                                                                                 |
# | YOU NEED THE TERMCOLOR MODULE AND YOU NEED TO RUN THIS ON A TERMINAL (TERMINAL APPLICATION OR VS CODE TERMINAL) |
# | RUN IN TERMINAL:   pip install termcolor                                                                        |
# -------------------------------------------------------------------------------------------------------------------

# Import time, os, from termcolor, colored.
import time, os, platform
try:
    from termcolor import colored
    
# Print without color if not able to find the correct modules.
except ModuleNotFoundError:
    if platform.system() == "Windows":
        clear = 'cls'
    else:
        clear = 'clear'
    def clear():
        os.system(clear)
    # Define the print bar module.
    def printBar(dlc, seconds, length, showTimeDifference):
        
        # Print the message saying that the 'download' has started.
        print("Beginning download of %s." % dlc)
        
        # Define important variables.
        timeS = int(seconds)
        chrLen = int(length)
        lenSoFar = 0
        bar = " " * chrLen
        # Start the timer to time the 'download'.
        startTime = time.time()
        
        # Start the loop for the bar to fill.
        for _ in range(chrLen+1):
            
            # Assign the bar a value.
            bar = "-" * lenSoFar + ">" + "-" * (chrLen - lenSoFar-1)
            
            # Check if bar is full.
            if lenSoFar == chrLen:
                bar = "-" * chrLen
                endTime = time.time()
                
            # Increase the current length value.
            lenSoFar += 1
            # Delay the bars updates.
            time.sleep(timeS/chrLen)
            # Clear screen.
            clear()
            
            # Print the message saying that the 'download' has started.
            print("Beginning download of %s." % dlc)
            
            # Print the bar.
            print("<" + bar + ">")
        
        # Set the variable for how long it took for the 'download' to finish.
        elapsedTime = endTime - startTime
        
        # Check if the user wants to show the difference in elapsed time from the specified time, since it is run by a computer, therefore the calculations take time and the difference may be larger or smaller based on the power of the computer running the program.
        if showTimeDifference == "on":
            # Check if the elapsed time is larger than the specified time.
            if elapsedTime > seconds:
                setTimeDifference = str(elapsedTime - seconds)[:(str(elapsedTime).index(".")+3)]
            # Check if the elapsed time is smaller than the specified time.
            elif elapsedTime < seconds:
                setTimeDifference = str(seconds - elapsedTime)[:(elapsedTime.index(".")+3)]
            else:
                # Set the time difference to zero if they are equal (somehow)
                setTimeDifference = 0
        # Print the message for when the 'download' finishes.
        print("Finished downloading %s in %s seconds."  % (dlc, str(elapsedTime)[:(str(elapsedTime).index(".")+3)]))
        # Check if the user wants to show the difference in elapsed time from the specified time.
        if showTimeDifference == "on":
            print("There was a difference of %s seconds from the set amount of time, which was %s." % (setTimeDifference, timeS))
        quit()
        
        
# Run the exact same thing as above but with color, if supported. (therefore it will not be commented.)
else:
    if platform.system() == "Windows":
        clear = 'cls'
    else:
        clear = 'clear'
    def clear():
        os.system(clear)
       
    def printBar(dlc, seconds, length, showTimeDifference):
        print(colored("Beginning download of ", 'blue') + colored(dlc, 'green') + colored(".", 'blue'))
        timeS = int(seconds)
        chrLen = int(length)
        lenSoFar = 0
        bar = " " * chrLen
        startTime = time.time()
        for _ in range(chrLen+1):
            bar = colored("-", 'blue') * lenSoFar + colored(">", 'blue') + "-" * (chrLen - lenSoFar-1)
            # Check if bar is full.
            if lenSoFar == chrLen:
                bar = colored("-", 'blue') * chrLen
                endTime = time.time()
            lenSoFar += 1
            # Delay the bars updates.
            time.sleep(timeS/chrLen)
            # Clear screen.
            clear()
            print(colored("Beginning download of ", 'blue') + colored(dlc, 'green') + colored(".", 'blue'))
            # Print the bar.
            print("<" + bar + ">")
        elapsedTime = endTime - startTime
        if showTimeDifference == "on":
            if elapsedTime > timeS:
                setTimeDifference = str(float(elapsedTime) - timeS)[:str(elapsedTime).index(".")+3]
            elif elapsedTime < timeS:
                setTimeDifference = str(timeS - float(elapsedTime))[:str(elapsedTime).index(".")+3]
            else:
                setTimeDifference = 0
        print(colored("Finished downloading ", 'red') + colored(dlc, 'green') + colored(", in ", 'red') + colored(str(elapsedTime)[:(str(elapsedTime).index(".")+3)], 'red') + colored(" seconds.", 'red'))
        if showTimeDifference == "on":
            print("There was a difference of " + colored(setTimeDifference, 'red') + " seconds from the set amount of time, which was " + colored(timeS, 'red') + " seconds.")
        quit()

on = "on"
off = "off"

# Sample run for the printBar() function.
printBar("Minecraft", 5, 50, on)
