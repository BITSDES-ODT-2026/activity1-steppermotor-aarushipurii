from machine import Pin
import time

pb= Pin(18,Pin.IN,Pin.PULL_UP)
pb1= Pin(33,Pin.IN,Pin.PULL_UP)
list1 = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

in1 = Pin(14, Pin.OUT)
in2 = Pin(25, Pin.OUT)
in3 = Pin(32, Pin.OUT)
in4 = Pin(27, Pin.OUT)

sleep = 0.003

while True:
    pb_val=pb.value()
    pb1_val=pb1.value()
    
    for i in range(0,500):
        if pb_val==0:
            for i in list1:
                in1.value(i[0])
                in2.value(i[1])
                in3.value(i[2])
                in4.value(i[3])
                
                time.sleep(sleep)
        

    for i in range(0,500):
        if pb1_val==0:
            for i in reversed(list1):
                  in1.value(i[0])
                  in2.value(i[1])
                  in3.value(i[2])
                  in4.value(i[3])
                  
                  time.sleep(sleep)


