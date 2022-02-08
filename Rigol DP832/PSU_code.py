import os
import time
import pyvisa


def clear():
    clear = os.popen("clear").readline()
    return clear.replace("clear=", "")


rm = pyvisa.ResourceManager()
PSU = rm.open_resource('INSERT YOUR RECOURCE HERE')

print(clear())
time.sleep(0.5)

print("PSU control panel")
print("-------------------------------------------------")
# Setup Rigol DC Power Supply
#READ USER INPUTS
#User input Channel parameters
#CHANNEL1 parameters
currentCH1 = input("CH1 Current[0-3A]: ")
if int(float(currentCH1)) > 3 or int(float(currentCH1)) < 0:
    print("Invalid input")
    currentCH1 = input("CH1 Current[0-3A]: ")

voltageCH1 = input("CH1 Voltage[0-30V]: ")
if int(float(voltageCH1)) > 30 or int(float(voltageCH1)) < 0:
    print("Invalid input")
    voltageCH1 = input("CH1 Voltage[0-30V]: ")

#CHANNEL2 parameters
currentCH2 = input("CH2 Current[0-3A]: ")
if int(float(currentCH2)) > 3 or int(float(currentCH2)) < 0:
    print("Invalid input")
    currentCH2 = input("CH2 Current[0-3A]: ")

voltageCH2 = input("CH2 Voltage[0-30V]: ")
if int(float(voltageCH2)) > 30 or int(float(voltageCH2)) < 0:
    print("Invalid input")
    voltageCH2 = input("CH2 Voltage[0-30V]: ")

#CHANNEL3 parameters
currentCH3 = input("CH3 Current[0-3A]: ")
if int(float(currentCH3)) > 3 or int(float(currentCH3)) < 0:
    print("Invalid input")
    currentCH3 = input("CH3 Current[0-3A]: ")

voltageCH3 = input("CH3 Voltage[0-5V]: ")
if int(float(voltageCH3)) > 30 or int(float(voltageCH3)) < 0:
    print("Invalid input")
    voltageCH3 = input("CH3 Voltage[0-5V]: ")

#SET USER INPUTS
#set: Channels

stateCH1 = input("CH1 [ON/OFF]: ")
stateCH2 = input("CH2 [ON/OFF]: ")
stateCH3 = input("CH3 [ON/OFF]: ")

PSU.write(':OUTP CH1,'+stateCH1)
PSU.write(':OUTP CH2,'+stateCH2)
PSU.write(':OUTP CH3,'+stateCH3)

PSU.write(':APPL CH1,'+voltageCH1+','+currentCH1)
PSU.write(':APPL CH2,'+voltageCH2+','+currentCH2)
PSU.write(':APPL CH3,'+voltageCH3+','+currentCH3)

print("-------------------------------------------------")
