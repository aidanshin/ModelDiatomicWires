import math
import numpy as np
odd_frequency = np.array([14.579, 28.5774, 41.5977, 55.1375, 65.835, 74.3318, 85.4571, 89.7666, 91.9978, 97.9136])
U_odd_frequency = np.array([0.261, 0.316, 0.247, 0.203, 1.726, 3.341, 1.075, 1.389, 0.293, 0.482])

matrix = [  14.44176377,  28.45252787,  41.00015505,   54.62627211,   65.17584058, 73.64356812, 83.23025961, 87.678738, 90.36233541,  96.36444193]
expected_y = [14.78098759, 29.0897629, 41.81979329, 55.66727829, 66.26284008, 74.67952066, 84.25874434,88.62179335, 91.23018417, 97.61329212]
    
test = [14.39546059 ,28.43645716 ,41.77725378, 54.08935576 ,65.06959829 ,74.44761136,
 81.99247716, 92.02230841 ,90.88936109, 87.51841605]
test = sorted(test)

def chisq(calculated, expected, uncertainty, dof):
    return np.sqrt(np.sum(((calculated-expected)/uncertainty)**2)) / dof

Oddtenbyten = chisq(odd_frequency, expected_y, U_odd_frequency, 9)
Oddmassofwire = chisq(odd_frequency,matrix,U_odd_frequency, 9)
print(chisq(odd_frequency,test,U_odd_frequency, 9))
print(f"Odd mass 10 by 10 matrix {Oddtenbyten}")
print(f"Odd mass 30 by 30 matrix {Oddmassofwire}\n")


freq = np.array([14.4624, 27.9244, 41.0114, 51.74355,61.5171, 82.10615, 87.6077, 92.3173, 96.4018, 103.15])
U_freq = np.array([0.284, 0.2021, 0.1971, 0.315, 0.1941, 0.354, 0.402, 2.378, 0.288, 0.504])


test = [14.293931936198534, 28.091136199282527, 40.7734279077054, 51.175883703784294, 55.93620393247486, 82.67684337112355, 88.27207417599126, 93.08769827270363, 96.17751822790956, 97.23390099485134]

Dia_MatrixF = [14.29393194, 28.0911362,   40.77342791, 51.1758837,  61.80881467, 82.67684337, 88.27207418, 93.08769827, 96.17751823, 101.79055793]
    
    #Matrix of Diatomic Wire Including String Mass
# MatrixF = [14.08850581,   27.72023173,   40.31521287,   50.74407543,   61.39447402,
#     81.81669042,   87.60676509,   92.57750052,   95.76991689,  101.31576096]
MatrixF = [13.98690246 ,  27.52371798  , 40.04080423  , 50.42981635  , 61.00862108,
   80.97678573  , 86.76080336  , 91.70939593   ,94.88339337  ,100.27102218]

Dia_tenbyten = chisq(freq, Dia_MatrixF, U_freq, 9)
Dia_massWire = chisq(freq,MatrixF,U_freq, 9)
print(chisq(freq, test, U_freq, 9))
print(f"Dia mass 10 by 10 matrix {Dia_tenbyten}")
print(f"Dia mass 30 by 30 matrix {Dia_massWire}")
# def perDif(a, b):
#     pd = []
#     for i in range(len(a)):
#         pd.append(  abs((a[i] - b[i])/((a[i] + b[i])/2)) )
#     return pd

# perdif_FvMatrix = np.average(perDif(freq, Dia_MatrixF)) * 100
# perdif_FvMs = np.average(perDif(freq, MatrixF)) * 100
# print(perDif(freq, Dia_MatrixF))
# print(perdif_FvMatrix)
# print(perdif_FvMs)