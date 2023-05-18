from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

def plotFilter(H, w_start,w_stop,step):
    N = int ((w_stop-w_start )/step) + 1
    w = np.linspace (w_start , w_stop , N)

    w, mag, phase = signal.bode(H,w)
    maxI = np.array(mag).argmax()
    maxV = round(np.array(mag).max(),2)
    maxF = round(w[maxI],2)




    difference_array = np.absolute(mag-(maxV-3))
    n3dB_index = difference_array[0:maxI].argmin()

    p3dB_index = difference_array[maxI:].argmin() + maxI



    n3dBV = round(mag[n3dB_index],2)
    n3dBF = round(w[n3dB_index],2)
    n3dB_label = '-3dB Frequency = {F}rad/s\nGain = {G}dB'.format(F=n3dBF, G=n3dBV)

    p3dBV = round(mag[p3dB_index],2)
    p3dBF = round(w[p3dB_index],2)
    p3dB_label = '+3dB Frequency = {F}rad/s\nGain = {G}dB'.format(F=p3dBF, G=p3dBV)

    BW = round(p3dBF - n3dBF,2)
    Q = round(maxF/BW,2)

    QBW_label = '\nBW = {bw}rad/s\nQ = {q}'.format(bw=BW,q=Q)

    
    f = plt.figure()
    plt.title("Bode Plot")

    plt.subplot (3, 1, 1)
    markers_on = [maxI]
    rlabel = 'Resonant Frequency = {F}rad/s\nGain = {G}dB'.format(F=maxF,G=maxV)
    plt.semilogx(w, mag, '-gD', markevery=markers_on, label=rlabel) # Magnitude Plot plt.grid()

    plt.axvline(x = p3dBF, color = 'b',linestyle='dashed', label = p3dB_label)
    plt.axvline(x = n3dBF, color = 'r',linestyle='dashed', label = n3dB_label+QBW_label)

    plt.ylabel("Magnitude (dB)")
    plt.legend(loc="lower left")

    plt.subplot (3, 1, 2)
    plt.semilogx(w, phase) # Phase plot plt.grid()
    plt.xlabel("Frequency (rad/s)")

    t,v = signal.step(H, N=1000)
    plt.subplot(3,1,3)
    plt.plot(t, v)
    plt.xlabel("t")
    plt.ylabel("v")


    f.set_figwidth(14)
    f.set_figheight(8)
    plt.show()



def pTankCircuit():
    r0 = 50.0
    rs = 3270.0
    ri = .17
    l = 7.3*10**(-6)
    c = 1100*10**(-12)



    # Define Transfer Function
    num = np.array([1,ri/l])
    den = np.array([c,c*ri/l,1/l])
    Zp = signal.TransferFunction(num , den)

    A = c*(r0+rs)
    B = (ri*c/l)*(r0+rs)+1.0
    C = (1/l)*(r0+rs+ri)

    num = np.array([1,ri/l])
    den = np.array([A,B,C])
    Hp = signal.TransferFunction(num,den)


    w_start = 0.01
    w_stop = 10**11
    step = 10000

    plotFilter(Hp,w_start,w_stop,step)




def s1TankCircuit():
    r0 = 50.0
    ri = .17
    l = 6.77*10**(-6)
    c = 150.67*10**(-12)


    a = l
    b = ri

    A = l
    B = ri+r0
    C = 1/c

    num = np.array([a,b,0])
    den = np.array([A,B,C])
    Hp = signal.TransferFunction(num,den)


    w_start = 0.01
    w_stop = 10**10
    step = 10000

    plotFilter(Hp,w_start,w_stop,step)


def s2TankCircuit():
    r0 = 50.0
    ri = .17
    l = 6.77*10**(-6)
    c = 150.67*10**(-12)


    a = 0
    b = 0
    c = 1/c

    A = l
    B = ri+r0
    C = 1/c

    num = np.array([a,b,c])
    den = np.array([A,B,C])
    Hp = signal.TransferFunction(num,den)


    w_start = 0.01
    w_stop = 10**10
    step = 10000

    plotFilter(Hp,w_start,w_stop,step)


pTankCircuit()
