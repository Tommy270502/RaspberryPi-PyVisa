import os
import time
import pyvisa

#IMPORTANT NOTE
#--------------
#Values returned from the functions are strings!
#if you prefer to have floats to perform further calculations instead just comment out the line:
# ohm = str(ohm) + "Ω"
#

def clear():
    clear = os.popen("clear").readline()
    return clear.replace("clear=", "")

def measureOhm():
    DMM.write(':FUNCtion:RESistance')
    for try_x in range(100):
        try:
            ohm = float(DMM.query(':MEASure:RESistance?'))
            ohm = str(ohm) + "Ω"
            return ohm
        except:
            print("Retrying", try_x)
            time.sleep(0.2)
    print("failed")
    return False

def measureVoltsDC():
    DMM.write(':FUNCtion:VOLTage:DC')
    voltsDC = float(DMM.query(':MEASure:VOLTage:DC?'))
    voltsDC = str(voltsDC)+"V"
    return voltsDC

def measureVoltAC():
    DMM.write(':FUNCtion:VOLTage:AC')
    voltsAC = float(DMM.query(':MEASure:VOLTage:AC?'))
    voltsAC = str(voltsAC)+"V"
    return voltsAC

def measureAmpDC():
    DMM.write(':FUNCtion:CURRent:DC')
    ampsDC = float(DMM.query(':MEASure:CURRent:DC?'))
    ampsDC = str(ampsDC)+"A"
    return ampsDC

def measureAmpAC():
    DMM.write(':FUNCtion:CURRent:AC')
    ampsAC = float(DMM.query(':MEASure:CURRent:AC?'))
    ampsAC = str(ampsAC)+"A"
    return ampsAC

def measureDiode():
    DMM.write(':FUNCtion:DIODe')
    diode = float(DMM.query(':MEASure:DIODe?'))
    diode = str(diode)+"V"
    return diode

def measureCap():
    DMM.write(':FUNCtion:CAPacitance')
    cap = float(DMM.query(':MEASure:CAPacitance?'))
    cap = str(cap)+"F"
    return cap

rm = pyvisa.ResourceManager()
DMM = rm.open_resource('INSERT YOUR RESOURCE HERE')

print(clear())
time.sleep(0.5)

# Setup Digital MultiMeter in DC Voltage mode
leadsCorrect = input("Are the leads connected correctly?[y/n]: ")

while leadsCorrect == "y":
    # Setup Rigol Digital Multi Meter

    print("DMM panel")
    print("-----------")
    print("insert <measureMEASUREMENT()> function here")
    print("-----------")
    time.sleep(1)
    print(clear())
    time.sleep(0.1)

print("Please check your leads before proceeding.")
