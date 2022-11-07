import time
import random
import msvcrt as m
from csv import writer

def wait():
    m.getch()

# TODO: Timeout system?

def on_press(key):
    return False

def on_release(key):
    return False


ts, t1, t1r, t2, t2r, t3, t3r, tf = "-", "-", "-", "-", "-", "-", "-", "-"

#board = pyfirmata.Arduino('')

#wb = load_workbook('Testing.xlsx')

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
    # TODO: Change the code here to output from the Ardunio instead of the terminal
    # TODO: Change code to use screen. Right now we're just using an LED, screen code is more complicated and requries some more parts
    #board.digital[13].write(1)
    print("Press a key")
    while m.kbhit():
        flush = wait() #Flush doesn't actually have an output, rather it's there to catch any stray inputs
        #TODO: Possible way to catch any spammed inputs to not be taken in?
    wait()
    print("listener closed")
    #board.digital[13].write(0)
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

curr = time.ctime(time.time())
List = [curr, t1, t1r, t2, t2r, t3, t3r, tf]

with open('test.csv', 'a') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(List)
    f_object.close