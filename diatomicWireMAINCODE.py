from __future__ import print_function
from fitting import *
import pylab as pl
import math

x, y = np.loadtxt('lab5.txt', unpack=True)
oddx, oddy = np.loadtxt('oddmass.txt', unpack=True)
y = y * 1000
oddy = oddy * 1000
def maxValues():
    maxvalue = []
    freq = []
    def findMax(frequency, amplitude, a , b):
        for i in range(len(frequency)):
            if (frequency[i] > a and frequency[i] < b):
                maxvalue.append(amplitude[i])
                freq.append(frequency[i])
        maximum = max(maxvalue)
        maxFreq = 0
        for i in range(len(maxvalue)):
            if(maximum == maxvalue[i]):
                maxFreq = freq[i]

        return maxFreq, maximum

    #80 64
    a = [13, 26, 38, 49, 52, 58,80, 82, 86, 92, 96, 102]
    b = [15.5, 29.5, 43, 51, 54, 64, 82, 84, 90, 95, 98, 104]
    frequency = []
    amplitude = []
    for i in range(0,12):
        F, A = findMax(x, y, a[i], b[i])
        frequency.append(F)
        amplitude.append(A)
        maxvalue = []
        freq = []
    
    return frequency, amplitude

def OddmaxValues():
    maxvalue = []
    freq = []
    def findMax(frequency, amplitude, a , b):
        for i in range(len(frequency)):
            if (frequency[i] > a and frequency[i] < b):
                maxvalue.append(amplitude[i])
                freq.append(frequency[i])
        maximum = max(maxvalue)
        maxFreq = 0
        for i in range(len(maxvalue)):
            if(maximum == maxvalue[i]):
                maxFreq = freq[i]

        return maxFreq, maximum

    #80 64
    a = [14,27, 41, 53, 65, 72,83.5, 85,  88, 91, 97]
    b = [15,30, 43, 58, 67, 77, 85, 88, 90, 94, 99]
    frequency = []
    amplitude = []
    for i in range(0,11):
        F, A = findMax(oddx, oddy, a[i], b[i])
        frequency.append(F)
        amplitude.append(A)
        maxvalue = []
        freq = []
    
    return frequency, amplitude
frequency, amplitude = maxValues()
oddfreq, oddamp = OddmaxValues()

U_frequency = [0.284, 0.2021, 0.1971, 0.253, 0.188, 0.1941, 0.171, 0.31, 0.402, 2.378, 0.288, 0.504]
odd_U_freq = [0.261, 0.316, 0.247, 0.203, 1.726, 3.341, 1.075, 0.414, 1.326, 0.293, 0.482]

def AmpFreq(x,y, frequency, amplitude, name):

    pl.figure(figsize = (8, 5),facecolor='white')
    pl.scatter(frequency,amplitude,s=15,label='Resonant Frequencies')
    pl.plot(x,y,"r-",label='Best-Fit Curve')
    pl.title(f"Amplitude of the {name} Wire\'s Motion vs Driving Frequency")
    pl.xlabel('Driving Frequency (Hz)')
    pl.ylabel('Amplitude of the Monatomic with one Odd Mass Wire\'s Motions (mV)')
    pl.legend(loc='upper left')

# AmpFreq(x, y, frequency, amplitude, "Diatomic")
# AmpFreq(oddx, oddy, oddfreq,oddamp, "Odd Ball")
def ModeFreq(freq, U_freq):
    def fitfunc(x, A, B):
        fit = []
        for i in range(len(x)):
            if(x[i] <= 5):
                fit.append(A*pl.sqrt(1 - pl.sqrt(1-B * (pl.sin(x[i]*math.pi/10))**2)))
                #return A*pl.sqrt(1 - pl.sqrt(1-(4*(m*M)/((m+M)**2) * (pl.sin(x))**2)))
            elif(x[i]>5 and x[i]<=11):
                fit.append(A*pl.sqrt(1 + pl.sqrt(1-B * (pl.sin(x[i]*math.pi/10))**2)))
                #return A*pl.sqrt(1 + pl.sqrt(1-(4*(m*M)/((m+M)**2) * (pl.sin(x))**2)))
        return(fit)

    
    modes = pl.array([1,2,3,4,5,6,7,8,9,10])
    frequency = pl.array(freq)
    frequency_U = pl.array(U_freq)

    accurate_modes = pl.array([1,2,3,4,6,7,8,9])
    accurate_freq = np.array([14.4624, 27.9244, 41.0114, 51.74355, 82.10615, 87.6077, 92.3173, 96.4018])
    accurate_U_freq = np.array([0.284, 0.2021, 0.1971, 0.315, 0.354, 0.402, 2.378, 0.288])    

    #Calculation Using Equation
    expectedF=[14.293931936198508, 28.091136199282527, 40.77342790770538, 51.17588370378429, 55.93620393247486, 82.67684337112355, 88.27207417599125, 93.08769827270363, 96.17751822790956, 97.23390099485134]
    
    #Matrix of Diatomic Wire
    Dia_MatrixF = [14.29393194, 28.0911362,   40.77342791, 51.1758837,  61.80881467, 82.67684337, 88.27207418, 93.08769827, 96.17751823, 101.79055793]
    
    #Matrix of Diatomic Wire Including String Mass
    MatrixF = [13.98690246 ,  27.52371798  , 40.04080423  , 50.42981635  , 61.00862108,
   80.97678573  , 86.76080336  , 91.70939593   ,94.88339337  ,100.27102218]
    
    m = 0.00166
    M = 0.003356
    K = 9.81*4.2257/0.2

    x = modes 
    y = frequency 
    a = (1/(2*math.pi))*(math.sqrt(K*(m+M)/(m*M)))
    b = 4*(m*M)/((m+M)**2)
    print(f"Expect Value of fitting parameter: \nA = {a}\nB = {b}")

    p0 = pl.array([a, b])
    popt, punc, rchi2, dof = general_fit(fitfunc, x, y, p0, frequency_U)
    print('optimal parameters: ', popt)
    print('uncertainties of parameters: ', punc)

    acc_p0 = pl.array([a, b])
    acc_popt, acc_punc, acc_rchi2, acc_dof = general_fit(fitfunc, accurate_modes, accurate_freq, acc_p0, accurate_U_freq)
    print('Accurate optimal parameters: ', acc_popt)
    print('Accurate uncertainties of parameters: ', acc_punc)

    xf = pl.linspace(min(x),max(x),100)
    accurate_x = pl.linspace(min(accurate_modes), max(accurate_modes), 100)
    
    yf = fitfunc(xf,*popt)
    ye = fitfunc(xf, *p0)
    accurate_y = fitfunc(accurate_x, *acc_popt)

    pl.figure(figsize = (8, 5),facecolor='white')

    pl.scatter(x,y,s=15,label='Data')
    #pl.scatter(x, expectedF, s=15, label='Expected')
    pl.scatter(x, MatrixF, color='grey',s=15,label='Matrix')
    pl.scatter(x, Dia_MatrixF, color = 'black', s=15,label='Matrix w/ String Mass')

    pl.errorbar(x, y,frequency_U, ls='None', capsize=2)

    pl.plot(xf,yf,"r-",label='Fitting Curve')
    pl.plot(xf,ye,"b-",label='Expected Curve')
    pl.plot(accurate_x, accurate_y, 'g-', label='Accurate Fit')

    pl.title("Resonant Frequency vs Modes")
    pl.xlabel('Modes')
    pl.ylabel('Resonant Frequency (Hz)')
    pl.legend(loc='upper left')

def OddModeFreq(freq, U_freq):
    
    modes = pl.array([1,2,3,4,5,6,7,8,9,10])
    frequency = pl.array([1.45E+01,2.86E+01,4.08E+01,5.40E+01,6.63E+01,7.53E+01,8.27E+01,8.92E+01,9.26E+01,9.42E+01])
    expected_monatomic = pl.array([14.39546059, 28.43645716, 41.77725378, 54.08935576, 65.06959829, 74.44761136, 81.99247716, 87.51841605, 90.88936109, 92.02230841])
    x = modes 
    y = freq
    yerr = U_freq
    #matrix of the monatomic wire
    matrix = [  14.44176377,  28.45252787,  41.00015505,   54.62627211,   65.17584058, 73.64356812, 83.23025961, 87.678738, 90.36233541,  96.36444193]
    expected_y = [14.78098759, 29.0897629, 41.81979329, 55.66727829, 66.26284008, 74.67952066, 84.25874434,88.62179335, 91.23018417, 97.61329212]
    # test = [14.08411157,   27.84662298  , 40.96878029  , 53.13832812   ,64.05468084, 73.436105    , 81.02901437  , 86.61890807  , 90.04181388 , 91.19453527]
    pl.figure(figsize = (8, 5),facecolor='white')
    pl.scatter(x,y,s=15,label='Data')
    # pl.scatter(x,expected_y, s=15, label='Matrix')
    # pl.scatter(x,matrix, s=15,label='Matrix w/ String Mass')
    pl.scatter(x,frequency, s=15, label='Monatomic Data')
    # pl.scatter(x,expected_monatomic, s=15, label='Expected Monatomic', color='purple')
    pl.errorbar(x, y,yerr, ls='None', capsize=2)
    pl.title(" Resonant Frequency vs Modes")
    pl.xlabel('Modes')
    pl.ylabel('Resonant Frequency (Hz)')
    pl.legend(loc='upper left')

#81.6477, 82.5646
#50.8058, 52.6813
freq = np.array([14.4624, 27.9244, 41.0114, 51.74355,61.5171, 82.10615, 87.6077, 92.3173, 96.4018, 103.15])
U_freq = np.array([0.284, 0.2021, 0.1971, 0.315, 0.1941, 0.354, 0.402, 2.378, 0.288, 0.504])

odd_frequency = np.array([14.579, 28.5774, 41.5977, 55.1375, 65.835, 74.3318, 85.4571, 89.7666, 91.9978, 97.9136])
U_odd_frequency = np.array([0.261, 0.316, 0.247, 0.203, 1.726, 3.341, 1.075, 1.389, 0.293, 0.482])
ModeFreq(freq, U_freq)
OddModeFreq(odd_frequency, U_odd_frequency)


pl.show()