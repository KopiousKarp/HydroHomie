#!/bin/bash
#listen for a BT connection and then pipe it to a serial port
#Every 3 seconds, get a list of paired devices and their UUIDs
#Isolate the UUIDs and then check if one is connected
#if a device is connected, mount it to a serial port with rfcomm
while true
do
   sleep 3s
   bluetoothctl paired-devices | cut -f2 -d' '|
   while read -r uuid
   do
      info=`bluetoothctl info $uuid`
      if echo "$info" | grep -q "Connected: yes"; then
            sudo rfcomm connect /dev/rfcomm0 40:22:D8:EA:35:2A 1 &
            echo "$info"

      fi
   done
done
echo found a device

python3 hydrohomie_companion_app.py


