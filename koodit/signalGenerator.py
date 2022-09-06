from tehtava1 import signalAnalyser
import numpy as np
import matplotlib.pyplot as plt

def sigGen():
    time = int(input("Give time 1-10s: "))
    frequency = int(input("Give frequency 0-500Hz: "))
    sRate = int(input("how many samples?: "))
    sCount = sRate * time
    print("Time: ",time,"s")
    print("Frequency: ",frequency,"Hz")
    print("Sample rate in samples per second",sRate)
    print("Sample count",sCount,"Samples")

    obj = signalAnalyser(sRate,time)
    obj.create(frequency)
    obj.plot(0,sCount)

sigGen()