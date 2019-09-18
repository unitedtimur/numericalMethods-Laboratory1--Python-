import numpy
import matplotlib.pyplot as plt

def polynomialLagranz(x, y, parameter):
    
    #Initialization
    sum = 0
    
    #Cycle for all numbers 'n'
    for j in range(len(y)):
        p1 = 1 #Top
        p2 = 1 #Bottom
        for i in range(len(x)):
            if i == j:
                p1 = p1 * 1
                p2 = p2 * 1
            else:
                p1 = p1 * (parameter - x[i])
                p2 = p2 * (x[j] - x[i])

        sum = sum + y[j] * p1 / p2

    return sum


x = [0.000, 1.250, 2.350, 3.000, 5.500] 
y = [3.000, -1.513, 2.872, -2.592, -2.813]

origX = numpy.linspace(numpy.min(x), numpy.max(x), 10000)
origY = [polynomialLagranz(x, y, i) 
                    for i in numpy.linspace(numpy.min(x), numpy.max(x), 10000)]

#Print Lagranz
plt.plot(x, y, 'o', origX, origY, color = 'green')

#Original Function 
def originalFunc(x):
    return numpy.sin(x) + 3 * numpy.cos(3 * x)

origY = [originalFunc(x) for x in numpy.linspace(numpy.min(x), numpy.max(x), 10000)]

#Print original function
plt.plot(origX, origY, color = 'red')

#print pointX
pointX = 1.963
plt.scatter(pointX, originalFunc(pointX), marker = 'x', color = 'black')
plt.legend(['Points', 'Lagranz function', 'Original function', 'Point X'])

#Absolute infelicity

def infelicityFunction(x, y, parameter):
    
    sum = 0

    for j in range(len(y)):
        p1 = 1
        p2 = 1
        for i in range(len(x)):
            if i == j:
                p1 = p1 * 1
                p2 = p2 * 1
            else:
                p1 = p1 * (parameter - x[i])
                p2 = p2 * (x[j] - x[i])

        sum = sum + (p1 / p2)

    return sum

infelicity = 0.5e-3

abs_infelicity = infelicity * numpy.abs(infelicityFunction(x, y, pointX))
relative_infelicity = abs_infelicity / polynomialLagranz(x, y, pointX)

print("Absolute infelicity equal ", round(abs_infelicity, 8))
print("Relative infelicity equal ", round(relative_infelicity, 8))

plt.title("My laboratory work")
plt.xlabel("Axis X")
plt.ylabel("Axis Y")

plt.grid(True)
plt.show()