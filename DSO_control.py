#############################################
#
# Filename: DSO control.py
#
# Project  : RaspberryPi-PyVisa
# Hardware : Raspberry Pi 
#
# Description:
# A easy to use User Interface to control your DSO.
#
# Date:       Author:           Version
# 03.02.2022  Thomas S. Perri   V1.0
#
##############################################

import os
import time
import pyvisa


def clear():
    clear = os.popen("clear").readline()
    return clear.replace("clear=", "")


rm = pyvisa.ResourceManager()
DSO = rm.open_resource('YOURUSBDEVICE')

print(clear())
time.sleep(0.5)

print("DSO control panel")
print("-------------------------------------------------")
# Setup Digital Signal Oszilloscope
#set: Auto scale the DSO
#DSO.write(':AUToscale')
#READ USER INPUTS
#User input Channel
channel = input("Enter channel(1-4): ")
#User input coupling
coupling = input("Enter coupling(DC, AC, GND): ")
#User input voltage scale [V]
voltageScale = input("Enter voltage scale [V]: ")
#User input voltage offset [V]
voltageOffset = input("Enter voltage offset [V]: ")
#User input time scale
timeScale = input("Enter time scale [s]: ")
#User input trigger level
triggerLevel = input("Enter trigger level [V]: ")

#SET USER INPUTS
#set: Channel 1 coupling
DSO.write(':CHANnel'+channel+':COUPling ' + coupling)
#set voltage scale
DSO.write(':CHANnel'+channel+':SCALe ' + voltageScale)
#set voltage offset
DSO.write(':CHANnel'+channel+':OFFSet ' + voltageOffset)
#set time scale
DSO.write(':TIMebase:MAIN:SCALe ' + timeScale)
#set trigger level
DSO.write(':TRIGger:EDGe:LEVel '+ triggerLevel)
print("-------------------------------------------------")
