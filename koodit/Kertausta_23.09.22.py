'''
1. Kerrataan mitä opittiin keskiviikkona
2. Simuliidaan yhdessä vielä se yksinkertainen f(x) = y = x^2 keissi, missä
   derivaatan f'(x) = 2x avulla siirrytään pisteestä x = 2 funnktion minimiin,
   mikä löytyy kohdasta x = 0
3. Toteutetaan kotitehtavan6.py tiedoston virhefunktio laskenta ja tulostus
4. Ja viimeiseksi vielä voidaan harjoitella lisää tekemällä
   data, joka on kolmannen asteen yhtälön mukaan. Eli muotoa
   f(x) = a*x^3 + b*x^2 + c*x + d ja toteutetaan algoritmi, joka hakee kertoimet
   a,b,c,d oikein
'''

'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,5,100)
y = np.power(x,2)

xa = 2
for i in range(10):
    learningRate = 1
    derivaatta = 2*xa
    xa = xa - derivaatta*learningRate
    ya = np.power(xa,2)

    plt.figure(1)
    plt.subplot(5,2,i+1),plt.plot(x,y),plt.plot(xa,ya,'r*')
plt.show()

'''

import matplotlib.pyplot as plt
import numpy as np

M = 100
x = 5*np.random.randn(M)
y = 3*x**3+5*x**2+7*x+12

a = np.random.randn(1)
b = np.random.randn(1)
c = np.random.randn(1)
d = np.random.randn(1)


a_adjusted_values = np.arange(100)
b_adjusted_values = np.arange(100)
c_adjusted_values = np.arange(100)
d_adjusted_values = np.arange(100)

rate = 0.00003   # this is learning rate parameter

plt.figure(1)
for rounds in range(100):
    grad_a = 0
    grad_b = 0
    grad_c = 0
    grad_d = 0
    # lets calculate new gradient values for t0 and t1 based on
    # M known values

    for i in range(M):
        # our cost function c = (1/2M)*(h(x)-y)^2
        # where M = number of known values
        # partial derivatives for t1 and t0 are
        # t0 =>(1/M)*(h(x)-y)*1 => (1/M)*((t1*x(i) + t0) - y(i)) * 1
        # t1 =>(1/M)*(h(x)-y)*x => (1/M)*((t1*x(i) + t0) - y(i)) * x(i)
        # where i goes from 1 => M
        grad_a = grad_a + ((a*x[i]**3+b*x[i]**2+c*x+d) - y[i])*x[i]**3
        grad_b = grad_b + ((a*x[i]**3+b*x[i]**2+c*x+d) - y[i])*x[i]**2
        grad_c = grad_c + ((a*x[i]**3+b*x[i]**2+c*x+d) - y[i])*x[i]
        grad_d = grad_c + ((a*x[i]**3+b*x[i]**2+c*x+d) - y[i])*1


    # and now we can update parameters t0 and t1 with new gradient step
    a = a - (rate/(M*1.0))*grad_a
    b = b - (rate/(M*1.0))*grad_b
    c = c - (rate/(M*1.0))*grad_c
    d = d - (rate/(M*1.0))*grad_d
    np.append(a_adjusted_values, a)
    np.append(b_adjusted_values, b)
    np.append(c_adjusted_values, c)
    np.append(d_adjusted_values, d)
    

    # and finally lets visualize results
    xmin = np.min(x)
    xmax = np.max(x)
    x1 = np.linspace(xmin,xmax,100)
    h = a*x1**3+b*x1**2+c*x1+d

    plt.subplot(3,2,1)
    plt.plot(a_adjusted_values,'-*r')
    plt.title('Adjusted A values')

    plt.subplot(3,2,2)
    plt.plot(b_adjusted_values,'-*g')
    plt.title('Adjusted B values ')

    plt.subplot(3,2,3)
    plt.plot(c_adjusted_values,'-*b')
    plt.title('Adjusted C values ')

    plt.subplot(3,2,4)
    plt.plot(d_adjusted_values,'-*y')
    plt.title('Adjusted d values ')

    plt.subplot(3,2,5)
    #plt.clf()
    plt.plot(x,y,'.r')
    plt.plot(x1, h, '-b')
    plt.title('Known datapoints and fitting straight line')
    plt.pause(0.05)

plt.show()
