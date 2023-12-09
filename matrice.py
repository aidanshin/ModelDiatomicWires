from __future__ import print_function
from fitting import *
import pylab as pl
import math
import numpy as np
### LENGTH OF WIRE 2.8 +- 0.01 m 
### Mass of wire 1.59 g
### take ratio mass to length then multiply by the length we use to get mass then divide by how many portions it is divided into
### we use 210 m of wire


### -3 the string on the last end is half as long so its twice as stiff so results in a 3.
# Since y(j-1)=0 and the string is half as long so the K will be 2K and it will result in a 3. 


# NEED TO DO ODD MASS ODD MASS LOCATED AT 4/6 
# MASS OF SMALL BALL 1.66
# MASS OF OTHER BALLS 2.4789

# Unceratinity of K 0.5733

# Diameter of wire 0.31 mm
# Explain the having an odd mass will cause deviations in the plot of the eigen vectors


def Monatomic():
    zeros = np.zeros((10,10))

    for i in range(0,10):
        zeros[i][i] = -2
        if (i < 9):
            zeros[i][i+1] = 1
        if (i > 0):
            zeros[i][i-1] = 1
    zeros[0][0] = -3
    zeros[9][9] = -3
 
    
    zeros = zeros * (9.81*4.2257/(0.00248*0.2))

    omega, vector = np.linalg.eig(zeros)

    omega = (np.sqrt(-1 * omega)) / (2 * np.pi)

    print(f"Matrix calculated frequencies: {omega}") 


def Diatomic():
    zeros = np.zeros((10,10))

    for i in range(0,10):
        zeros[i][i] = -2
        if (i < 9):
            zeros[i][i+1] = 1
        if (i > 0):
            zeros[i][i-1] = 1
    zeros[0][0] = -3
    zeros[9][9] = -3
    
    K_Mb = (9.81*4.2257/(0.2*(0.003356)))
    K_Ms = (9.81*4.2257/(0.2*(0.00166)))

    for i in range(0,10):
        for k in range(0,10):
            if (i % 2 == 0):
                zeros[k][i] = zeros[k][i]*K_Ms
            else:
                zeros[k][i] = zeros[k][i]*K_Mb

    omega, vector = np.linalg.eig(zeros)

    omega = (np.sqrt(abs(omega))) / (2 * np.pi)

    print(f"Matrix calculated frequencies: {omega}") 


def StringMass():
    zeros = np.zeros((30,30))

    for i in range(0,30):
        zeros[i][i] = -2
        if (i < 29):
            zeros[i][i+1] = 1
        if (i > 0):
            zeros[i][i-1] = 1
    zeros[0][0] = -3
    zeros[29][29] = -3

    STRING_MASS = (((0.00159)/2.8))*2.0/30
    
    K_Mb = 9.81*4.2257/((0.003356 + STRING_MASS) *(.2/3)) 
    K_Ms = 9.81*4.2257/((0.00166+ STRING_MASS) *(.2/3)) 
    K_m_string = 9.81*4.2257/(STRING_MASS*(.2/3)) 
    

    for i in range(0, 5):
        for k in range(0, 30):
            zeros[k][i*6+0] = zeros[k][i*6+0] * K_m_string
            zeros[k][i*6+1] = zeros[k][i*6+1] * K_Mb
            zeros[k][i*6+2] = zeros[k][i*6+2] * K_m_string
            zeros[k][i*6+3] = zeros[k][i*6+3] * K_m_string
            zeros[k][i*6+4] = zeros[k][i*6+4] * K_Ms
            zeros[k][i*6+5] = zeros[k][i*6+5] * K_m_string

    omega, vector = np.linalg.eig(zeros)

    omega = (np.sqrt(abs(omega))) / (2 * np.pi)

    print(f"Matrix calculated frequencies: {omega}") 

def OddBall():
    zeros = np.zeros((10,10))

    for i in range(0,10):
        zeros[i][i] = -2
        if (i < 9):
            zeros[i][i+1] = 1
        if (i > 0):
            zeros[i][i-1] = 1
    zeros[0][0] = -3
    zeros[9][9] = -3
 
    
    zeros = zeros * (9.81*4.2257/((0.0024789 )*0.2))

    #Add the mass of the odd ball into matrix
    zeros[2][3] = 1 * (9.81*4.2257/((0.00166 )*0.2))
    zeros[3][3] = -2 * (9.81*4.2257/((0.00166)*0.2))
    zeros[4][3] = 1 * (9.81*4.2257/((0.00166 )*0.2))

    omega, vector = np.linalg.eig(zeros)

    omega = (np.sqrt(-1 * omega)) / (2 * np.pi)

    print(f"Matrix calculated frequencies: {omega}")

    # vector = np.array(vector)
    # x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # for vectors in vector:
    #     print(vectors)
    #     pl.figure(figsize = (8, 5),facecolor='white')
    #     # pl.scatter(vectors,amplitude,s=15,label='Resonant Frequencies')
    #     pl.plot(x,vectors,"r-")
    #     # pl.title(f"Amplitude of the {name} Wire\'s Motion vs Driving Frequency")
    #     # pl.xlabel('Driving Frequency (Hz)')
    #     # pl.ylabel('Amplitude of the Monatomic with one Odd Mass Wire\'s Motions (mV)')
    #     # pl.legend(loc='upper left')
    


def OddStringMass():
    zeros = np.zeros((30,30))
    expected = np.zeros((30,30))
    for i in range(0,30):
        zeros[i][i] = -2
        if (i < 29):
            zeros[i][i+1] = 1
        if (i > 0):
            zeros[i][i-1] = 1
    zeros[0][0] = -3
    zeros[29][29] = -3

    for i in range(0,30):
        expected[i][i] = -2
        if (i < 29):
            expected[i][i+1] = 1
        if (i > 0):
            expected[i][i-1] = 1
    expected[0][0] = -3
    expected[29][29] = -3

    STRING_MASS = (((0.00159)/2.8))*2.0/30

    K_Mb = 9.81*4.2257/((0.0024789 + STRING_MASS)*(.20/3))
    K_Ms = 9.81*4.2257/((0.00166+ STRING_MASS)*(.20/3))
    K_m_string = 9.81*4.2257/(STRING_MASS*(.20/3))

    for i in range(0, 5):
        if i == 1:
            for k in range(0, 30):
                zeros[i*6+0][k] = zeros[i*6+0][k] * K_m_string
                zeros[i*6+1][k] = zeros[i*6+1][k] * K_Mb
                zeros[i*6+2][k] = zeros[i*6+2][k] * K_m_string
                zeros[i*6+3][k] = zeros[i*6+3][k] * K_m_string
                zeros[i*6+4][k] = zeros[i*6+4][k] * K_Ms
                zeros[i*6+5][k] = zeros[i*6+5][k] * K_m_string
        else :
            for k in range(0, 30):
                zeros[i*6+0][k] = zeros[i*6+0][k] * K_m_string
                zeros[i*6+1][k] = zeros[i*6+1][k] * K_Mb
                zeros[i*6+2][k] = zeros[i*6+2][k] * K_m_string
                zeros[i*6+3][k] = zeros[i*6+3][k] * K_m_string
                zeros[i*6+4][k] = zeros[i*6+4][k] * K_Mb
                zeros[i*6+5][k] = zeros[i*6+5][k] * K_m_string

    for i in range(0, 5):
        if i == 1:
            for k in range(0, 30):
                expected[i*6+0][k] = expected[i*6+0][k] * K_m_string
                expected[i*6+1][k] = expected[i*6+1][k] * K_Mb
                expected[i*6+2][k] = expected[i*6+2][k] * K_m_string
                expected[i*6+3][k] = expected[i*6+3][k] * K_m_string
                expected[i*6+4][k] = expected[i*6+4][k] * K_Mb
                expected[i*6+5][k] = expected[i*6+5][k] * K_m_string
        else :
            for k in range(0, 30):
                expected[i*6+0][k] = expected[i*6+0][k] * K_m_string
                expected[i*6+1][k] = expected[i*6+1][k] * K_Mb
                expected[i*6+2][k] = expected[i*6+2][k] * K_m_string
                expected[i*6+3][k] = expected[i*6+3][k] * K_m_string
                expected[i*6+4][k] = expected[i*6+4][k] * K_Mb
                expected[i*6+5][k] = expected[i*6+5][k] * K_m_string


    omega, vector = np.linalg.eig(zeros)
    expected_omega, expected_vector = np.linalg.eig(expected)

    omega = (np.sqrt(abs(omega))) / (2 * np.pi)
    expected_omega = (np.sqrt(abs(expected_omega))) / (2 * np.pi)

    print(omega) 
    print(expected_omega)
    for i in range(0, 10):
        if i == 3 or i == 6 or i ==8:
            None
        else:
            expected_vector[:,i] = expected_vector[:,i] * -1 
    
    for i in range(0, 10):
        figure(figsize=(8,5), facecolor='white')
        if i == 6:
            plot(arange(0,len(vector[:,0])),vector[:,i],"r-", label="Odd Mass")
            plot(arange(0,len(expected_vector[:,0])),expected_vector[:,i+1], "b-", label="Expected")
            legend(loc='upper left')
            title(f"Resonant Frequency {round(omega[i], 2)} Expected {round(expected_omega[i+1], 2)}")
            ylabel('Vertical Displacement')
        elif i == 7:
            plot(arange(0,len(vector[:,0])),vector[:,i],"r-", label="Odd Mass")
            plot(arange(0,len(expected_vector[:,0])),expected_vector[:,i-1], "b-", label="Expected")
            legend(loc='upper left')
            title(f"Resonant Frequency {round(omega[i], 2)} Expected {round(expected_omega[i-1], 2)}")
            ylabel('Vertical Displacement')
        else: 
            plot(arange(0,len(vector[:,0])),vector[:,i],"r-", label="Odd Mass")
            plot(arange(0,len(expected_vector[:,0])),expected_vector[:,i], "b-", label="Expected")
            legend(loc='upper left')
            title(f"Resonant Frequency {round(omega[i], 2)} Expected {round(expected_omega[i], 2)}")
            ylabel('Vertical Displacement')

print(f"Montatomic Frequency: ")
Monatomic()
print(f"Diatomic Frequency: ")
Diatomic()
print(f"Diatomic with Mass of String Frequency: ")
StringMass()
print("Odd Mass Wire Frequency: ")
OddBall()
print("Odd ball string with mass of wire: ")
OddStringMass()
pl.show()



# def ZOddStringMass():
#     zeros = np.zeros((30,30))

#     for i in range(0,30):
#         zeros[i][i] = -2
#         if (i < 29):
#             zeros[i][i+1] = 1
#         if (i > 0):
#             zeros[i][i-1] = 1
#     zeros[0][0] = -3
#     zeros[29][29] = -3

#     STRING_MASS = (((0.00159)/2.8))*2.0/30

#     K_Mb = 9.81*4.2257/((0.0024789 + STRING_MASS)*(.20/3))
#     K_Ms = 9.81*4.2257/((0.00166+ STRING_MASS)*(.20/3))
#     K_m_string = 9.81*4.2257/(STRING_MASS*(.20/3))

#     for i in range(0, 5):
#         if i == 1:
#             for k in range(0, 30):
#                 zeros[k][i*6+0] = zeros[k][i*6+0] * K_m_string
#                 zeros[k][i*6+1] = zeros[k][i*6+1] * K_Mb
#                 zeros[k][i*6+2] = zeros[k][i*6+2] * K_m_string
#                 zeros[k][i*6+3] = zeros[k][i*6+3] * K_m_string
#                 zeros[k][i*6+4] = zeros[k][i*6+4] * K_Ms
#                 zeros[k][i*6+5] = zeros[k][i*6+5] * K_m_string
#         else :
#             for k in range(0, 30):
#                 zeros[k][i*6+0] = zeros[k][i*6+0] * K_m_string
#                 zeros[k][i*6+1] = zeros[k][i*6+1] * K_Mb
#                 zeros[k][i*6+2] = zeros[k][i*6+2] * K_m_string
#                 zeros[k][i*6+3] = zeros[k][i*6+3] * K_m_string
#                 zeros[k][i*6+4] = zeros[k][i*6+4] * K_Mb
#                 zeros[k][i*6+5] = zeros[k][i*6+5] * K_m_string


#     omega, vector = np.linalg.eig(zeros)

#     omega = (np.sqrt(abs(omega))) / (2 * np.pi)

# print(omega) 
# print(vector)
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# y = [-0.00036083888760339263, -0.0007751455536805676, 0.0009881875824253987, 0.001262194475987451, -0.0020060417998076486, 0.0015443523838125528, -0.0009404189669524344, 0.001619715566186751, -0.0007735048639810649, 0.0034854789258269544]
# # pl.figure(figsize=(8,5), facecolor='white')
# pl.scatter(x,y,s=15)
# for i in range(0, 10):
#     figure()
#     plot(arange(0,len(vector[:,0])),vector[:,i])
# for vectors in vector:
#     pl.figure(figsize = (8, 5),facecolor='white')
#     # pl.scatter(vectors,amplitude,s=15,label='Resonant Frequencies')
#     pl.plot(x,vectors,"r-")
# for i in range(0, 10):
#     y = []
#     for k in range(0, 10):
#        y.append(vector[i][k])
        
#     pl.figure(figsize = (8, 5),facecolor='white')
#     print(y) 
#     # pl.scatter(vectors,amplitude,s=15,label='Resonant Frequencies')
#     pl.plot(x,y,"r-")



# def NewOddStringMass():
#     zeros = np.zeros((50,50))

#     for i in range(0,50):
#         zeros[i][i] = -2
#         if (i < 49):
#             zeros[i][i+1] = 1
#         if (i > 0):
#             zeros[i][i-1] = 1
#     zeros[0][0] = -3
#     zeros[49][49] = -3

#     STRING_MASS = (((0.00159)/2.8))*2.0/50
#     print(STRING_MASS)
#     K_Mb = 9.81*4.2257/((0.0024789 + 0) *(.20/5))
#     K_Ms = 9.81*4.2257/((0.00166+ 0) *(.20/5))
#     K_m_string = 9.81*4.2257/(STRING_MASS*(.20/5))

#     for i in range(0, 5):
#         if i == 1: 
#             for k in range(0, 50):
#                 zeros[k][i*10+0] = zeros[k][i*10+0] * K_m_string
#                 zeros[k][i*10+1] = zeros[k][i*10+1] * K_m_string
#                 zeros[k][i*10+2] = zeros[k][i*10+2] * K_Mb
#                 zeros[k][i*10+3] = zeros[k][i*10+3] * K_m_string
#                 zeros[k][i*10+4] = zeros[k][i*10+4] * K_m_string
#                 zeros[k][i*10+5] = zeros[k][i*10+5] * K_m_string
#                 zeros[k][i*10+6] = zeros[k][i*10+6] * K_m_string
#                 zeros[k][i*10+7] = zeros[k][i*10+7] * K_Ms
#                 zeros[k][i*10+8] = zeros[k][i*10+8] * K_m_string
#                 zeros[k][i*10+9] = zeros[k][i*10+9] * K_m_string
#         else:
#             for k in range(0, 50):
#                 zeros[k][i*10+0] = zeros[k][i*10+0] * K_m_string
#                 zeros[k][i*10+1] = zeros[k][i*10+1] * K_m_string
#                 zeros[k][i*10+2] = zeros[k][i*10+2] * K_Mb
#                 zeros[k][i*10+3] = zeros[k][i*10+3] * K_m_string
#                 zeros[k][i*10+4] = zeros[k][i*10+4] * K_m_string
#                 zeros[k][i*10+5] = zeros[k][i*10+5] * K_m_string
#                 zeros[k][i*10+6] = zeros[k][i*10+6] * K_m_string
#                 zeros[k][i*10+7] = zeros[k][i*10+7] * K_Mb
#                 zeros[k][i*10+8] = zeros[k][i*10+8] * K_m_string
#                 zeros[k][i*10+9] = zeros[k][i*10+9] * K_m_string

#     omega, vector = np.linalg.eig(zeros)

#     omega = (np.sqrt(abs(omega))) / (2 * np.pi)

#     print(omega) 

# NewOddStringMass()



# def TestNewOddStringMass():
#     zeros = np.zeros((110,110))

#     for i in range(0,110):
#         zeros[i][i] = -2
#         if (i < 109):
#             zeros[i][i+1] = 1
#         if (i > 0):
#             zeros[i][i-1] = 1
#     zeros[0][0] = -3
#     zeros[109][109] = -3

#     STRING_MASS = (((0.00159)/2.8))*2.0/110
#     # print(STRING_MASS)
#     # K_Mb = 9.81*4.2257/((0.0024789 + STRING_MASS) *(.20/11))
#     # K_Ms = 9.81*4.2257/((0.00166+ STRING_MASS) *(.20/11))
#     # K_m_string = 9.81*4.2257/(STRING_MASS*(.20/11))
#     # K0 = (2.025e+11) * math.pi * (0.00031/2)**2
#     # print(K0)
#     K0 = 4/3
#     K_Mb = ((9.81*4.2257+ K0)/(.2/11)) * 1/ (0.0024789 + STRING_MASS)
#     K_Ms = ((9.81*4.2257+ K0)/(.2/11)) * 1 / (0.00166+ STRING_MASS)
#     K_m_string = ((9.81*4.2257+ K0)/(.2/11)) * 1 / STRING_MASS
#     for i in range(0, 10):
#         if i == 1: 
#             for k in range(0, 110):
#                 zeros[i*11+0][k]= zeros[i*11+0][k] * K_m_string
#                 zeros[i*11+1][k]= zeros[i*11+1][k] * K_m_string
#                 zeros[i*11+2][k]= zeros[i*11+2][k] * K_m_string
#                 zeros[i*11+3][k]= zeros[i*11+3][k] * K_m_string
#                 zeros[i*11+4][k]= zeros[i*11+4][k] * K_m_string
#                 zeros[i*11+5][k]= zeros[i*11+5][k] * K_Ms
#                 zeros[i*11+6][k]= zeros[i*11+6][k] * K_m_string
#                 zeros[i*11+7][k]= zeros[i*11+7][k] * K_m_string
#                 zeros[i*11+8][k]= zeros[i*11+8][k] * K_m_string
#                 zeros[i*11+9][k]= zeros[i*11+9][k] * K_m_string
#                 zeros[i*11+10][k] = zeros[i*11+10][k] * K_m_string
#         else:
#             for k in range(0, 110):
#                 zeros[i*11+0][k]= zeros[i*11+0][k] * K_m_string
#                 zeros[i*11+1][k]= zeros[i*11+1][k] * K_m_string
#                 zeros[i*11+2][k]= zeros[i*11+2][k] * K_m_string
#                 zeros[i*11+3][k]= zeros[i*11+3][k] * K_m_string
#                 zeros[i*11+4][k]= zeros[i*11+4][k] * K_m_string
#                 zeros[i*11+5][k]= zeros[i*11+5][k] * K_Mb
#                 zeros[i*11+6][k]= zeros[i*11+6][k] * K_m_string
#                 zeros[i*11+7][k]= zeros[i*11+7][k] * K_m_string
#                 zeros[i*11+8][k]= zeros[i*11+8][k] * K_m_string
#                 zeros[i*11+9][k]= zeros[i*11+9][k] * K_m_string
#                 zeros[i*11+10][k] = zeros[i*11+10][k] * K_m_string


#     omega, vector = np.linalg.eig(zeros)

#     omega = (np.sqrt(abs(omega))) / (2 * np.pi)

#     print(omega)

#     for i in range(0, 10):
#         figure()
#         plot(arange(0,len(vector[:,0])),vector[:,i])

# TestNewOddStringMass()
# show()

# def Mona():
#     zeros = np.zeros((30,30))

#     for i in range(0,30):
#         zeros[i][i] = -2
#         if (i < 29):
#             zeros[i][i+1] = 1
#         if (i > 0):
#             zeros[i][i-1] = 1
#     zeros[0][0] = -3
#     zeros[29][29] = -3

#     STRING_MASS = (((0.00159)/2.8))*2.0/30
#     print(STRING_MASS)
#     K_Mb = 9.81*4.2257/((0.0024789 + STRING_MASS) *(.20/3))
#     K_Ms = 9.81*4.2257/((0.00166+ STRING_MASS) *(.20/3))
#     K_m_string = 9.81*4.2257/(STRING_MASS*(.20/3))

#     for i in range(0, 5):
#         for k in range(0, 30):
#             zeros[k][i*6+0] = zeros[k][i*6+0] * K_m_string
#             zeros[k][i*6+1] = zeros[k][i*6+1] * K_Mb
#             zeros[k][i*6+2] = zeros[k][i*6+2] * K_m_string
#             zeros[k][i*6+3] = zeros[k][i*6+3] * K_m_string
#             zeros[k][i*6+4] = zeros[k][i*6+4] * K_Mb
#             zeros[k][i*6+5] = zeros[k][i*6+5] * K_m_string

#     omega, vector = np.linalg.eig(zeros)

#     omega = (np.sqrt(abs(omega))) / (2 * np.pi)

#     print(omega) 
# Mona()

# NewOddStringMass()



# def DiaTenTen():
#     zeros = np.zeros((110,110))

#     for i in range(0,110):
#         zeros[i][i] = -2
#         if (i < 109):
#             zeros[i][i+1] = 1
#         if (i > 0):
#             zeros[i][i-1] = 1
#     zeros[0][0] = -3
#     zeros[109][109] = -3

#     STRING_MASS = (((0.00159)/2.8))*2.0/110
#     print(STRING_MASS)
#     K_Mb = 9.81*4.2257/((0.003356 + STRING_MASS) *(.20/11))
#     K_Ms = 9.81*4.2257/((0.00166+ STRING_MASS) *(.20/11))
#     K_m_string = 9.81*4.2257/(STRING_MASS*(.20/11))

#     for i in range(0, 10):
#         if i % 2 == 0: 
#             for k in range(0, 110):
#                 zeros[k][i*11+0] = zeros[k][i*11+0] * K_m_string
#                 zeros[k][i*11+1] = zeros[k][i*11+1] * K_m_string
#                 zeros[k][i*11+2] = zeros[k][i*11+2] * K_m_string
#                 zeros[k][i*11+3] = zeros[k][i*11+3] * K_m_string
#                 zeros[k][i*11+4] = zeros[k][i*11+4] * K_m_string
#                 zeros[k][i*11+5] = zeros[k][i*11+5] * K_Ms
#                 zeros[k][i*11+6] = zeros[k][i*11+6] * K_m_string
#                 zeros[k][i*11+7] = zeros[k][i*11+7] * K_m_string
#                 zeros[k][i*11+8] = zeros[k][i*11+8] * K_m_string
#                 zeros[k][i*11+9] = zeros[k][i*11+9] * K_m_string
#                 zeros[k][i*11+10] = zeros[k][i*11+10] * K_m_string
#         else:
#             for k in range(0, 110):
#                 zeros[k][i*11+0] = zeros[k][i*11+0] * K_m_string
#                 zeros[k][i*11+1] = zeros[k][i*11+1] * K_m_string
#                 zeros[k][i*11+2] = zeros[k][i*11+2] * K_m_string
#                 zeros[k][i*11+3] = zeros[k][i*11+3] * K_m_string
#                 zeros[k][i*11+4] = zeros[k][i*11+4] * K_m_string
#                 zeros[k][i*11+5] = zeros[k][i*11+5] * K_Mb
#                 zeros[k][i*11+6] = zeros[k][i*11+6] * K_m_string
#                 zeros[k][i*11+7] = zeros[k][i*11+7] * K_m_string
#                 zeros[k][i*11+8] = zeros[k][i*11+8] * K_m_string
#                 zeros[k][i*11+9] = zeros[k][i*11+9] * K_m_string
#                 zeros[k][i*11+10] = zeros[k][i*11+10] * K_m_string


#     omega, vector = np.linalg.eig(zeros)

#     omega = (np.sqrt(abs(omega))) / (2 * np.pi)

#     print(omega) 

# DiaTenTen()