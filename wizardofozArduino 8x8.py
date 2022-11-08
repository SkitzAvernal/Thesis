import time
import random
import pyfirmata
from pyfirmata import util
import msvcrt as m

def wait():
    m.getch()

# TODO: Timeout system?

ts, t1, t1r, t2, t2r, t3, t3r, tf = "-", "-", "-", "-", "-", "-", "-", "-"
testString =  "■■■■■■■■■■■■"
emptyString = "            "

board = pyfirmata.Arduino('COM3')

def stopwatch(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    return "{0}:{1}:{2}".format(int(hours),int(mins),int(sec))
    

def current_milli_time():
    return round(time.time() * 1000)

def alt_current_milli_time():
    return time.time_ns()

def go_to_sleep():
    tSleep = random.randrange(5, 10) # Program will go to sleep at random time between 10 seconds and 150 seconds (could be too high). For demo, it is 5 and 10 seconds
    time.sleep(tSleep)

def timecount():
    msS = current_milli_time()
    # TODO: Change code to use screen. Right now we're just using an LED, screen code is more complicated and requries some more parts
    board.send_sysex( pyfirmata.STRING_DATA, util.str_to_two_byte_iter(testString))
    while m.kbhit():
        flush = wait() #Flush doesn't actually have an output, rather it's there to catch any stray inputs
    wait()
    board.send_sysex( pyfirmata.STRING_DATA, util.str_to_two_byte_iter(emptyString))
    msE = current_milli_time()
    return msE - msS

input("Press Enter to Start")
ts = time.time()
go_to_sleep()
t1 = stopwatch(time.time() - ts)
t1r = timecount()
go_to_sleep()
t2 = stopwatch(time.time() - ts)
t2r = timecount()
go_to_sleep()
t3 = stopwatch(time.time() - ts)
t3r = timecount()
time.sleep(3) #TODO: Have a way to count when car finishes/tester presses a button
tf = stopwatch(time.time() - ts)

print("Final Results")
print("Test 1 Time: {0} Reaction Time: {1}ms".format(t1, t1r))
print("Test 2 Time: {0} Reaction Time: {1}ms".format(t2, t2r))
print("Test 3 Time: {0} Reaction Time: {1}ms".format(t3, t3r))
print("Total Test Time: {0}".format(tf))

