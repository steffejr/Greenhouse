import u12
import time
import numpy as np
import pandas as pd

d = u12.U12()

d.eAnalogOut(analogOut0=5)
d.rawAISample()

# Turn on power
def TurnOnPower(U12Pointer,Channel0Volt,Channel1Volt):
    U12Pointer.eAnalogOut(analogOut0=Channel0Volt,analogOut1=Channel1Volt)
    
def TakeSample(U12Pointer,Channel):
    Data = []
    ChannelName = 'Channel%d'%(Channel)
    #print "Using channel %s"%ChannelName
    for i in range(0,10,1):
        datapoint = U12Pointer.rawAISample()
        datapoint = datapoint[ChannelName]
        Data.append(datapoint)
    return np.mean(Data)

def TakeReading(U12Pointer,Calibration=[0,5,5]):
    # Turn on power
    TurnOnPower(d,5,0)
    # take reading
    Data = TakeSample(d,0)
    # Turn off power
    TurnOnPower(d,0,0)
    
    # Calculate calibrated value
    PercentData = 100*(Data - Calibration[0])/Calibration[2]    
    return Data,PercentData

def Calibrate(U12Pointer): 
    # Run calibration routine
    print "Take probe out and make sure it is dry. Then press enter."
    dummy = raw_input("Good.")
    MinData = TakeReading(U12Pointer)
    print "Put probe in water and press enter"
    
    dummy = raw_input("Good.")
    MaxData = TakeReading(U12Pointer)
    
    Range = MaxData - MinData
    return MinData, MaxData, Range
    