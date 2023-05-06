import serial
import time
import math

#UNIX
btser= serial.Serial("/dev/rfcomm0", baudrate=9600)
#Windows; may need to change comm port
#btser= serial.Serial(port='COM9', baudrate=9600)
while(1):
    print(time.time()," : ", btser.readline().decode())
