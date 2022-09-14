from tehtava1 import signalAnalyser
import numpy as np
import matplotlib.pyplot as plt

def sigGen():
    time = int(input("Give time 1-10s: "))
    print("Time: ",time,"s")
    frequency = int(input("Give frequency 0-500Hz: "))
    print("Frequency: ",frequency,"Hz")
    sRate = int(input("how many samples? (at least twice the frequency): "))
    sCount = sRate * time

    print("Sample rate in samples per second",sRate)
    print("Sample count",sCount,"Samples")

    obj = signalAnalyser(sRate,time)
    obj.create(frequency)
    obj.plot(0,sCount)

sigGen()