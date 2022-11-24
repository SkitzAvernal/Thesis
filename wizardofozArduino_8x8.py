import time
import random
import pyfirmata
import msvcrt as m
from maxmatrix import LedMatrix
from csv import writer
import keyboard

matcher = 0
def wait():
    m.getch()

ts, t1, t1r, t2, t2r, t3, t3r, tf = "-", "-", "-", "-", "-", "-", "-", "-"
# SET 1 - Simple Shapes
cross = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]

circle =[[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 1, 1, 1, 0, 0],
         [0, 0, 1, 1, 1, 1, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]

triangle =[[0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 1, 0, 0, 0],
           [0, 0, 1, 1, 1, 1, 0, 0],
           [0, 0, 1, 1, 1, 1, 0, 0],
           [0, 1, 1, 1, 1, 1, 1, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0]]

square =[[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 1, 1, 0, 0],
         [0, 0, 1, 1, 1, 1, 0, 0],
         [0, 0, 1, 1, 1, 1, 0, 0],
         [0, 0, 1, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]

# SET 2 = Complex Shapes
# Cross and Square are kept
mail =  [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 1, 1, 1, 0],
         [0, 1, 1, 0, 0, 1, 1, 0],
         [0, 1, 0, 1, 1, 0, 1, 0],
         [0, 1, 0, 1, 1, 0, 1, 0],
         [0, 1, 1, 1, 1, 1, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]
call =  [[0, 0, 1, 1, 1, 1, 0, 0],
         [0, 0, 1, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 1, 1, 0, 0],
         [0, 0, 0, 0, 1, 1, 0, 0],
         [0, 0, 0, 0, 1, 1, 0, 0],
         [0, 0, 0, 0, 1, 1, 0, 0],
         [0, 0, 1, 1, 1, 1, 0, 0],
         [0, 0, 1, 1, 1, 1, 0, 0]]

curr = time.ctime(time.time())
board = pyfirmata.Arduino('COM3')
matrix = LedMatrix(board, 10, 9, 8)
matrix.setup()

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
    tSleep = random.randrange(10, 30) # Program will go to sleep at random time between 10 seconds and 60 seconds (could be too high). For demo, it is 5 and 10 seconds
    time.sleep(tSleep)

def timecount():
    msS = current_milli_time()
    # Each number corresponds to each 
    rand = random.randrange(0,4)
    if (matcher == 1):
        match rand:
            case 0:
                matrix.draw_matrix(cross)
            case 1:
                matrix.draw_matrix(mail)
            case 2:
                matrix.draw_matrix(call)
            case 3:
                matrix.draw_matrix(square)
    else: 
        match rand:
            case 0:
                matrix.draw_matrix(cross)
            case 1:
                matrix.draw_matrix(circle)
            case 2:
                matrix.draw_matrix(triangle)
            case 3:
                matrix.draw_matrix(square)

    """
    while m.kbhit():
        flush = wait() #Flush doesn't actually have an output, rather it's there to catch any stray inputs
    while (matcher==-1):
        key = m.getch()
        print(key)
        match rand:
            case 0: #cross
                if key == b"o":
                    break
            case 1: #ciircle
                if key ==  b"p":
                    break
            case 2: #triangle
                if key == b"l":
                    break
            case 3: #square
                if key == b";":
                    break
    ##key = wait()
    """
    match rand:
        case 0: #cross
            keyboard.wait('o')
                
        case 1: #circle/mail
            keyboard.wait('p')
                    
        case 2: #triangle/call
            keyboard.wait('l')
                    
        case 3: #square
            keyboard.wait(';')
    matrix.clear()
    msE = current_milli_time()
    return msE - msS

#print("Ready. Press Enter on the keyboard to start")
#keyboard.wait('enter)
mode = input("Press Enter to Start")
if (mode == "C"):
    matcher = 1
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
time.sleep(3)
out = input("Testing Complete. Press Enter to continue.") #Enter DNF and press enter if the participant cannot complete the course)
#keyboard.wait('enter')

tf = stopwatch(time.time() - ts)

print("Final Results")
print("Test 1 Time: {0} Reaction Time: {1}ms".format(t1, t1r))
print("Test 2 Time: {0} Reaction Time: {1}ms".format(t2, t2r))
print("Test 3 Time: {0} Reaction Time: {1}ms".format(t3, t3r))
print("Total Test Time: {0}".format(tf))

#curr = time.ctime(time.time())
List = ["8x8", curr, t1, t1r, t2, t2r, t3, t3r, tf]

with open('final_test.csv', 'a') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(List)
    f_object.close