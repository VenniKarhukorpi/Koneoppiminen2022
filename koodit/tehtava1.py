import numpy as np
import matplotlib.pyplot as plt

class signalAnalyser:
    def __init__(self,Fs,t):
        print('Constructor of signalAnalyser')
        self.Fs = Fs
        self.Ts = 1/Fs
        self.t = t
        self.xakseli = np.arange(0,t,self.Ts)       # x akselin luonti
        self.pituus = int(self.xakseli.size)        # x akselin pituus
        self.yakseli = np.zeros((1,self.pituus))    # y akselin pituus
        

    def create(self,f):
        pii = np.pi
        t = self.xakseli

        self.yakseli = np.cos( 2 * pii * f * t)     # akselin määritys
        self.sinakseli = np.sin( 2 * pii * f * t)

    def plot(self,start,stop):
        fig, ax = plt.subplots(2)
        ax[0].plot(self.xakseli[start:stop],self.sinakseli[start:stop],'-*')
        ax[0].set_title("Sin")
        ax[1].plot(self.xakseli[start:stop],self.yakseli[start:stop],'-*')
        ax[1].set_title("Cos")
        plt.figure(1)
        plt.show()   

if __name__ == '__main__':
    obj = signalAnalyser(100,2)  # luodaan objekti, jonka konstruktorille Fs = 100 Hz ja t = 2s
    obj.create(2)                # käytetään objektin create funktiota, missä f = 2 Hz
    obj.plot(0,50)               # käytetään objektin plot funktiota, plotataan väli 0 - 50 näytettä.

