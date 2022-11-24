import time
import random
import pyfirmata
import msvcrt as m
from maxmatrix import LedMatrix
from csv import writer
import keyboard

matcher = 0
shape =""
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
         [0, 0, 1, 1, 1, 1, 0, 0],
         [0, 0, 1, 0, 1, 1, 0, 0],
         [0, 0, 1, 1, 0, 1, 0, 0],
         [0, 0, 1, 1, 0, 1, 0, 0],
         [0, 0, 1, 0, 1, 1, 0, 0],
         [0, 0, 1, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]
call =  [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 1, 1, 0, 0],
         [0, 1, 1, 1, 1, 1, 1, 0],
         [0, 1, 1, 0, 0, 1, 1, 0],
         [0, 1, 1, 0, 0, 1, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]

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
    tSleep = 1 #random.randrange(5, 15) # Program will go to sleep at random time between 10 seconds and 60 seconds (could be too high). For demo, it is 5 and 10 seconds
    time.sleep(tSleep)

def timecount():
    global shape
    msS = current_milli_time()
    # Each number corresponds to each 
    rand = random.randrange(0,6)
    if (matcher == 1):
        match rand:
            case 0:
                matrix.draw_matrix(cross)
                #print("Cross")
                shape="Cross"
            case 1:
                matrix.draw_matrix(mail)
                #print("Mail")
                shape="Mail"
            case 2:
                matrix.draw_matrix(call)
                #print("Call")
                shape="Call"
            case 3:
                matrix.draw_matrix(square)
                #print("Square")
                shape="Square"
    else: 
        match rand:
            case 0:
                matrix.draw_matrix(cross)
                #print("Cross")
                shape="Cross"
            case 1:
                matrix.draw_matrix(circle)
                #print("Circle")
                shape="Circle"
            case 2:
                matrix.draw_matrix(triangle)
                #print("Triangle")
                shape="Triangle"
            case 3:
                matrix.draw_matrix(square)
                #print("Square")
                shape="Square"
            case 4:
                matrix.draw_matrix(mail)
                shape="Mail"
            case 5:
                matrix.draw_matrix(call)
                shape="Call"

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
    """match rand:
        case 0: #cross
            #keyboard.wait('o')
            wait()
                
        case 1: #circle/mail
            #keyboard.wait('p')
            wait()
                    
        case 2: #triangle/call
            #keyboard.wait('l')
            wait()
                    
        case 3: #square
            wait()
            #keyboard.wait(';')"""
    wait()
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
t1s = shape
go_to_sleep()
t2 = stopwatch(time.time() - ts)
t2r = timecount()
go_to_sleep()
t2s = shape
t3 = stopwatch(time.time() - ts)
t3r = timecount()
t3s = shape
go_to_sleep()
t4 = stopwatch(time.time() - ts)
t4r = timecount()
t4s = shape
go_to_sleep()
t5 = stopwatch(time.time() - ts)
t5r = timecount()
t5s = shape
go_to_sleep()
t6 = stopwatch(time.time() - ts)
t6r = timecount()
t6s = shape
go_to_sleep()
t7 = stopwatch(time.time() - ts)
t7r = timecount()
t7s = shape
go_to_sleep()
t8 = stopwatch(time.time() - ts)
t8r = timecount()
t8s = shape
go_to_sleep()
t9 = stopwatch(time.time() - ts)
t9r = timecount()
t9s = shape
go_to_sleep()
t10 = stopwatch(time.time() - ts)
t10r = timecount()
t10s = shape
go_to_sleep()
t11 = stopwatch(time.time() - ts)
t11r = timecount()
t11s = shape
go_to_sleep()
t12 = stopwatch(time.time() - ts)
t12r = timecount()
t12s = shape
go_to_sleep()
t13 = stopwatch(time.time() - ts)
t13r = timecount()
t13s = shape
go_to_sleep()
t14 = stopwatch(time.time() - ts)
t14r = timecount()
t14s = shape
go_to_sleep()
t15 = stopwatch(time.time() - ts)
t15r = timecount()
t15s = shape
go_to_sleep()
t16 = stopwatch(time.time() - ts)
t16r = timecount()
t16s = shape
go_to_sleep()
t17 = stopwatch(time.time() - ts)
t17r = timecount()
t17s = shape
go_to_sleep()
t18 = stopwatch(time.time() - ts)
t18r = timecount()
t18s = shape
go_to_sleep()
t19 = stopwatch(time.time() - ts)
t19r = timecount()
t19s = shape
go_to_sleep()
t20 = stopwatch(time.time() - ts)
t20r = timecount()
t20s = shape
go_to_sleep()

#out = input("Testing Complete. Press Enter to continue.") #Enter DNF and press enter if the participant cannot complete the course)
#keyboard.wait('enter')

tf = stopwatch(time.time() - ts)
f = open("test.txt", "a")

print("Final Results")
f.write("Final Results")
f.write("\n")

print("Test 1 Time: {0} Reaction Time: {1}ms Shape: {2}".format(t1, t1r, t1s))
f.write("Test 1 Time: {0} Reaction Time: {1}ms Shape: {2}\n".format(t1, t1r, t1s))
print("Test 2 Time: {0} Reaction Time: {1}ms Shape: {2}".format(t2, t2r, t2s))
print("Test 3 Time: {0} Reaction Time: {1}ms Shape: {2}".format(t3, t3r, t3s))
print("Test 4 Time: {0} Reaction Time: {1}ms Shape: {2}".format(t4, t4r, t4s))
print("Test 5 Time: {0} Reaction Time: {1}ms Shape: {2}".format(t5, t5r, t5s))
print("Test 6 Time: {0} Reaction Time: {1}ms Shape: {2}".format(t6, t6r, t6s))
print("Test 7 Time: {0} Reaction Time: {1}ms Shape: {2}".format(t7, t7r, t7s))
print("Test 8 Time: {0} Reaction Time: {1}ms Shape: {2}".format(t8, t8r, t8s))
print("Test 9 Time: {0} Reaction Time: {1}ms Shape: {2}".format(t9, t9r, t9s))
print("Test 10 Time: {0} Reaction Time: {1}ms Shape: {2}".format(t10, t10r, t10s))
print("Test 11 Time: {0} Reaction Time: {1}ms Shape: {2}".format(t11, t11r, t11s))
print("Test 12 Time: {0} Reaction Time: {1}ms Shape: {2}".format(t12, t12r, t12s))
print("Test 13 Time: {0} Reaction Time: {1}ms Shape: {2}".format(t13, t13r, t13s))
print("Test 14 Time: {0} Reaction Time: {1}ms Shape: {2}".format(t14, t14r, t14s))
print("Test 15 Time: {0} Reaction Time: {1}ms Shape: {2}".format(t15, t15r, t15s))
print("Test 16 Time: {0} Reaction Time: {1}ms Shape: {2}".format(t16, t16r, t16s))
print("Test 17 Time: {0} Reaction Time: {1}ms Shape: {2}".format(t17, t17r, t17s))
print("Test 18 Time: {0} Reaction Time: {1}ms Shape: {2}".format(t18, t18r, t18s))
print("Test 19 Time: {0} Reaction Time: {1}ms Shape: {2}".format(t19, t19r, t19s))
print("Test 20 Time: {0} Reaction Time: {1}ms Shape: {2}".format(t20, t20r, t20s))

f.write("Test 2 Time: {0} Reaction Time: {1}ms Shape: {2}\n".format(t2, t2r, t2s))
f.write("Test 3 Time: {0} Reaction Time: {1}ms Shape: {2}\n".format(t3, t3r, t3s))
f.write("Test 4 Time: {0} Reaction Time: {1}ms Shape: {2}\n".format(t4, t4r, t4s))
f.write("Test 5 Time: {0} Reaction Time: {1}ms Shape: {2}\n".format(t5, t5r, t5s))
f.write("Test 6 Time: {0} Reaction Time: {1}ms Shape: {2}\n".format(t6, t6r, t6s))
f.write("Test 7 Time: {0} Reaction Time: {1}ms Shape: {2}\n".format(t7, t7r, t7s))
f.write("Test 8 Time: {0} Reaction Time: {1}ms Shape: {2}\n".format(t8, t8r, t8s))
f.write("Test 9 Time: {0} Reaction Time: {1}ms Shape: {2}\n".format(t9, t9r, t9s))
f.write("Test 10 Time: {0} Reaction Time: {1}ms Shape: {2}\n".format(t10, t10r, t10s))
f.write("Test 11 Time: {0} Reaction Time: {1}ms Shape: {2}\n".format(t11, t11r, t11s))
f.write("Test 12 Time: {0} Reaction Time: {1}ms Shape: {2}\n".format(t12, t12r, t12s))
f.write("Test 13 Time: {0} Reaction Time: {1}ms Shape: {2}\n".format(t13, t13r, t13s))
f.write("Test 14 Time: {0} Reaction Time: {1}ms Shape: {2}\n".format(t14, t14r, t14s))
f.write("Test 15 Time: {0} Reaction Time: {1}ms Shape: {2}\n".format(t15, t15r, t15s))
f.write("Test 16 Time: {0} Reaction Time: {1}ms Shape: {2}\n".format(t16, t16r, t16s))
f.write("Test 17 Time: {0} Reaction Time: {1}ms Shape: {2}\n".format(t17, t17r, t17s))
f.write("Test 18 Time: {0} Reaction Time: {1}ms Shape: {2}\n".format(t18, t18r, t18s))
f.write("Test 19 Time: {0} Reaction Time: {1}ms Shape: {2}\n".format(t19, t19r, t19s))
f.write("Test 20 Time: {0} Reaction Time: {1}ms Shape: {2}\n\n".format(t20, t20r, t20s))

print("Total Test Time: {0}".format(tf))
f.write("Total Test Time: {0}\n".format(tf))
f.write("\n")

f.close()


'''
#curr = time.ctime(time.time())
List = ["8x8", curr, t1, t1r, t2, t2r, t3, t3r, tf]

with open('final_test.csv', 'a') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(List)
    f_object.close

'''