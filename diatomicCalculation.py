import math
Ms = 0.00166
Mb = 0.003356

K = 9.81*4.2257/0.2

a = (1/(2*math.pi))*(math.sqrt(K*(Ms+Mb)/(Ms*Mb)))
b = 4*(Ms*Mb)/((Ms+Mb)**2)

def Calc():
    omega_square_pos = []
    omega_square_neg = []
    for i in range(6,11):
        x = K*(((Mb+Ms)/(Mb*Ms)) + math.sqrt(((Ms+Mb)/(Ms*Mb))**2 - (4 / (Ms*Mb)) * math.sin(i*math.pi/10)**2))
        omega_square_pos.append(x)

    for i in range(1,6):
        x = K*(((Mb+Ms)/(Mb*Ms)) - math.sqrt(((Ms+Mb)/(Ms*Mb))**2 - (4 / (Ms*Mb)) * math.sin(i*math.pi/10)**2))
        omega_square_neg.append(x)

    frequency_pos = []
    frequency_neg = []
    for omega in omega_square_pos:
        frequency_pos.append(1/(2*math.pi)*math.sqrt(omega))

    for omega in omega_square_neg:
        frequency_neg.append(1/(2*math.pi)*math.sqrt(omega))

    print(frequency_pos)
    print(frequency_neg)
    

def New():
    omega_square_pos = []
    omega_square_neg = []
    for i in range(6,11):
        x = a*math.sqrt(1 + math.sqrt(1-b * (math.sin(i*math.pi/10))**2))
        omega_square_pos.append(x)

    for i in range(1,6):
        x = a*math.sqrt(1 - math.sqrt(1-b * (math.sin(i*math.pi/10))**2))
        omega_square_neg.append(x)

    # frequency_pos = []
    # frequency_neg = []
    # for omega in omega_square_pos:
    #     frequency_pos.append(1/(2*math.pi)*math.sqrt(omega))

    # for omega in omega_square_neg:
    #     frequency_neg.append(1/(2*math.pi)*math.sqrt(omega))

    print(omega_square_pos)
    print(omega_square_neg)
Calc()
#New()