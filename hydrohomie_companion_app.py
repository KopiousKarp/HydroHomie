import serial
from datetime import datetime
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

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

    if (now.second == 0):
       timestamps = [datetime.timestamp(t) for t in time_data]
       #plt.ion()
       graph_vol = volume_data
       #plt.plot([1, 2, 3], [1, 2, 3])
       plt.plot(timestamps,graph_vol)
       plt.show()


