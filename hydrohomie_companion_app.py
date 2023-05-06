import serial
from datetime import datetime
import math

#UNIX
btser= serial.Serial("/dev/rfcomm0", baudrate=9600)
#Windows; may need to change comm port
#btser= serial.Serial(port='COM9', baudrate=9600)
time_data = []
volume_data = []
while(1):

    now = datetime.now() #source 1 datetime library
    volume_data_point = int(btser.readline().decode()) #source 2 serial port


    #print to terminal
    print(now.strftime('%Y-%m-%d %H:%M:%S'),":",volume_data_point)

    #save the data
    time_data.append(now)
    volume_data.append(volume_data_point)

