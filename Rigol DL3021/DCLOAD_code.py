import os
import time
import pyvisa


def clear():
    clear = os.popen("clear").readline()
    return clear.replace("clear=", "")

def constantCurrent(A):
    DCL.write(':SOUR:FUNC CURR')
    DCL.write(':SOUR:CURR:LEV:IMM '+A)
    function = DCL.query(':SOUR:FUNC?')
    return function

def constantVoltage(V):
    DCL.write(':SOUR:FUNC VOLT')
    DCL.write(':SOUR:VOLT:LEV:IMM '+V)
    function = DCL.query(':SOUR:FUNC?')
    return function

def constantResistance(R):
    DCL.write(':SOUR:FUNC RES')
    DCL.write(':SOUR:RES:LEV:IMM '+R)
    function = DCL.query(':SOUR:FUNC?')
    return function

def constantPower(P):
    DCL.write(':SOUR:FUNC POW')
    DCL.write(':SOUR:POW:LEV:IMM '+P)
    function = DCL.query(':SOUR:FUNC?')
    return function

rm = pyvisa.ResourceManager()
DCL = rm.open_resource('USB0::6833::3601::DL3A232800682::0::INSTR')

print(clear())
time.sleep(0.5)
DCL.write(':SOUR:INP:STAT 0')

print("DC Load control panel")
print("-------------------------------------------------")
# Setup Rigol DC Load
mode = input("Set load mode CC/CV/CR/CP: ")

if mode == "CC":
    A = input("Enter CC value (A): ")
    constantCurrent(A)
if mode == "CV":
    V = input("Enter CV value (V): ")
    constantVoltage(V)
if mode == "CR":
    R = input("Enter CR value (R): ")
    constantResistance(R)
if mode == "CP":
    P = input("Enter CP value (P): ")
    constantPower(P)

loadState = input("Turn Load ON/OFF: ")
DCL.write(':SOUR:INP:STAT '+loadState)

print("-------------------------------------------------")
