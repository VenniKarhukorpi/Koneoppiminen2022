import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

""" 
Tehtävä 1: 
- lataa Latest https://covidtracking.com/data/download/national-history.csv
  tiedosto pandas kirjaston avulla Pandas dataframeksi. 
- "Irroita" siitä ladattaessa'date','deaths','hospitalInc','hospitalNow' sarakkeet
- Piirrä matplotlib.pyplot kirjaston ja plt.subplot, plt.plot, plt.title, plt.show 
  komentojen avulla kuva, josta nähdään kuolleiden lukumäärät, sairaalapotilaiden
  inkrementaalinen kasvu ja kuinka paljon sairaalassa on potilaita eri päivinä.
- Selvitä minä päivänä potilaiden kasvu on ollut suurinta ja mikä on tuon päivän potilasmäärä

Tehtävä 2:
- Muuta kaikki dataFramen sarakkeet numpy arrayksi to_numpy() funktion avulla
- Tulosta kuolleiden määrä ja sairaalassa olleiden lukumäärät oikeassa järjestyksessä
  (huom päivämäärät ovat tiedostossa viimeisin päivämäärä ensin. Eli käännä tulostusjärjestys
   siten, että kuvaan tulostetaan deaths sarakkeen viimeisin alkio ensin jne.)
"""

def tehtava1():
      df = pd.read_csv('national-history.csv')
      data = df[['date','death','hospitalizedIncrease','hospitalizedCurrently']]
      dateformat = mdates.DateFormatter('%d-%m-%y')

      fig, ax = plt.subplots(3)
      fig.set_size_inches(10,5)

      ax[0].set_title('Dead')
      ax[0].plot((data['date']),data['death'])
      ax[0].xaxis.set_major_formatter(dateformat)

      ax[1].set_title('Hospitalized Increase')
      ax[1].plot((data['date']),data['hospitalizedIncrease'])

      ax[2].set_title('Hospitalized Currently')
      ax[2].plot((data['date']), data['hospitalizedCurrently'])


def tehtava2():
      df = pd.read_csv('national-history.csv')
      data_array = df.to_numpy()
      axisLenght = 420
      dateformat = mdates.DateFormatter('%d-%m-%y')
    
      fig, ax = plt.subplots(3)
      fig.set_size_inches(10,5)
    
      ax[0].set_title('Dead',color='red')
      ax[0].plot(mdates.num2date(mdates.datestr2num(data_array[0:axisLenght,0])), data_array[0:axisLenght,1],color='red')
      ax[0].xaxis.set_major_formatter(dateformat)

      ax[1].set_title('Hospitalized Increase')
      ax[1].plot(mdates.num2date(mdates.datestr2num(data_array[0:axisLenght,0])), data_array[0:axisLenght,5])
      ax[1].xaxis.set_major_formatter(dateformat)

      ax[2].set_title('Hospitalized Currently')
      ax[2].plot(mdates.num2date(mdates.datestr2num(data_array[0:axisLenght,0])), data_array[0:axisLenght,6])
      ax[2].xaxis.set_major_formatter(dateformat)

      
      

tehtava1()
tehtava2()

plt.show()