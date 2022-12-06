import numpy as np
from matplotlib import colors
from matplotlib import pyplot as plt


############################################################################################################################
##  User Functions
############################################################################################################################
## For finding Hamming distance of given test data with each trained letter.
def Hamming(x, y):
    dis = []
    for xx, yy in zip(x, y):
        dd = 0.
        for xxx, yyy in zip(xx, yy):
            if xxx == 1 and yyy != 1:
                dd += 1.
            elif yyy == 1 and xxx != 1:
                dd += 1.
        dis.append(dd)
    return dis

## For plotting
def plotting(actual, predict, shape):
    cmap = colors.ListedColormap(['white', 'black'])
    bounds = [-1.5, 0, 1.5]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    _ , ax = plt.subplots(nrows=1, ncols=2, sharex=True, sharey=True)
    ax[0].imshow(np.array(predict).reshape(shape), cmap=cmap, norm=norm)
    ax[1].imshow(np.array(actual).reshape(shape), cmap=cmap, norm=norm)

    for i in range(2):
        ax[i].grid(linewidth=0.5)
        ax[i].set_xticks(np.arange(-0.5, 4, 1))
        ax[i].set_yticks(np.arange(-0.5, 4, 1))
        ax[i].set(xlabel='Width', ylabel='Height')
    ax[0].set_title("Corrupted Letter")
    ax[1].set_title("Converged Letter")

    plt.show()

## Activation Function
def activation_function(f, net):
    if net > 0:
        return 1
    elif net == 0:
        return f
    else:
        return -1

inputDimension = 5


## For bipolar Conversion
def bipolarTransformation(vector):
    vector = np.array(vector).reshape(1, inputDimension * inputDimension)
    vector = np.where(vector == 0, -1, vector)
    return vector

## Clearing the diagonal
def clearDiagonal(matrix):  ## returns weight matix with diagnol elements 0
    np.fill_diagonal(matrix, 0)
    return matrix


## For finding individual weight matrix for each letter to be stored
def weightMatix(vector):  ## returns weight matix

    temp = vector.T
    temp = np.dot(temp,vector)
    return temp

## For matrix addition
def add_matrices(matrix1, matrix2):
    return matrix1 + matrix2


############################################################################################################################
##  HopField Class
############################################################################################################################

class Hopfield():
    def __init__(self, nodes):
        self.nodes = nodes
        self.patterns = 0
        self.memoryWeightMatrix = np.zeros((nodes, nodes))

    def netInfo(self, training_set):
        self.patterns = len(training_set)
        print(f"Hopfield Network(Nodes = '{self.nodes}', Patterns = '{self.patterns}')")

    def weightMatrixNetwork(self, training_set):  ## Memory Weight Matrix creation

        for i in range(len(training_set)):
            # print(training_set[i])
            bipolarVector = np.array(training_set[i]).reshape(1,25)
            vectorWeightMatrix = weightMatix(bipolarVector)
            vectorWeightMatrix = clearDiagonal(vectorWeightMatrix)
            self.memoryWeightMatrix = add_matrices(self.memoryWeightMatrix, vectorWeightMatrix)
            self.memoryWeightMatrix = clearDiagonal(self.memoryWeightMatrix)
        self.memoryWeightMatrix =  self.memoryWeightMatrix/ len(training_set)


    def energy(self, vector):  ## Finding the energy of the system
        e = 0
        for i in range(self.nodes):
            for j in range(self.nodes):
                e += self.memoryWeightMatrix[i][j]*vector[i]*vector[j]
        return -1*e/2

    def predict(self, y):  ## Prediction

        energy_pre =-1
        energy_cur = self.energy(y)
        tmp = y.copy()
        converges = 0

        while energy_pre != energy_cur:
            y1 = y
            y1 = y1.reshape(1, 25)
            for i in range(len(y)):
                tmp2 = 0
                for j in range(len(y)):
                    tmp2 += self.memoryWeightMatrix[i][j] * tmp[j]
                tmp[i] = activation_function(tmp[i], tmp2)
            y = tmp.copy()
            energy_pre = energy_cur
            energy_cur = self.energy(y)
            print()
            for i in range(len(training_set)):
                err = Hamming(y1, training_set[i:])
                print(f"TestVector differs by {err} bits from Training Set{[i]}")  ## Previous and updated energy
            print(f"Previous Energy:{energy_pre} and Energy Current:{energy_cur}")
            converges += 1
        print(f"Converged in {converges} iterations")
        return y


############################################################################################################################
##  Training (Weight Matrix Creation)
############################################################################################################################

C = [1, 1, 1, 1, 1,
     1, 0, 0, 0, 0,
     1, 0, 0, 0, 0,
     1, 0, 0, 0, 0,
     1, 1, 1, 1, 1]  ## C

T = [1, 1, 1, 1, 1,
     0, 0, 1, 0, 0,
     0, 0, 1, 0, 0,
     0, 0, 1, 0, 0,
     0, 0, 1, 0, 0] ## T

N = [1, 0, 0, 0, 1,
     1, 1, 0, 0, 1,
     1, 0, 1, 0, 1,
     1, 0, 0, 1, 1,
     1, 0, 0, 0, 1] ## N

Z = [1, 1, 1, 1, 1,
     0, 0, 0, 1, 0,
     0, 0, 1, 0, 0,
     0, 1, 0, 0, 0,
     1, 1, 1, 1, 1] ## Z


C = bipolarTransformation(C)
T = bipolarTransformation(T)
N = bipolarTransformation(N)
Z = bipolarTransformation(Z)

training_set = np.vstack([C,T,N,Z])

network = Hopfield(25)
network.netInfo(training_set)

network.weightMatrixNetwork(training_set)
energy_c = network.energy(training_set[0])
print(f"C energy = {energy_c}")
energy_t = network.energy(training_set[1])
print(f"T energy = {energy_t}")
energy_n = network.energy(training_set[2])
print(f"N energy = {energy_n}")
energy_z = network.energy(training_set[3])
print(f"Z energy = {energy_z}")


############################################################################################################################
##  For testing C
############################################################################################################################


y = [1, 0, 1, 1, 0,
     1, 0, 0, 0, 0,
     0, 0, 0, 0, 1,
     1, 0, 0, 0, 0,
     1, 1, 0, 1, 0]

print()
print(f"Testing for C")
y = bipolarTransformation(y)
y1 = y
y1 = np.array(y1).reshape(25)
y1 = y1.reshape(1,25)
y = np.array(y).reshape(25)
eng = network.energy(y)

output = network.predict(y)
plotting(output, y, (5, 5))
print("Converged Letter:\n", output.reshape(5, 5))

############################################################################################################################
##  For testing T
############################################################################################################################

y = [1, 1, 1, 1, 0,
     0, 0, 1, 0, 0,
     1, 0, 1, 0, 0,
     0, 0, 1, 0, 0,
     0, 0, 0, 0, 0]
print()
print(f"Testing for T")
y = bipolarTransformation(y)
y = np.array(y).reshape(25)
eng = network.energy(y)
output = network.predict(y)
plotting(output, y, (5, 5))
print("Converged Letter:\n", output.reshape(5, 5))
#
############################################################################################################################
##  For testing N
############################################################################################################################

y = [1, 0, 0, 0, 1,
     1, 1, 0, 0, 0,
     1, 0, 1, 0, 1,
     0, 0, 0, 0, 1,
     1, 0, 0, 0, 1]
print()
print(f"Testing for N")
y = bipolarTransformation(y)
y = np.array(y).reshape(25)
eng = network.energy(y)

output = network.predict(y)
plotting(output, y, (5, 5))
print("Converged Letter:\n", output.reshape(5, 5))

#
# ############################################################################################################################
# ##  For testing Z
# ############################################################################################################################

y = [0, 0, 1, 1, 1,
     0, 0, 0, 1, 0,
     0, 0, 1, 0, 0,
     0, 1, 0, 0, 0,
     1, 1, 0, 1, 0]
print()
print(f"Testing for Z")
y = bipolarTransformation(y)
y = np.array(y).reshape(25)

eng = network.energy(y)

output = network.predict(y)
plotting(output, y, (5, 5))
print("Converged Letter:\n", output.reshape(5, 5))

# ############################################################################################################################
# ##  Memory weight Matrix and weights files (.mif) for individual neuron Creation
# ############################################################################################################################

## (Converting signed decimal into 16 bit binary with 8 fractional parts)
## -1   = 1111111100000000
## -0.5 = 1111111110000000
## 1    = 0000000100000000
## 0.5  = 0000000010000000
## 0    = 0000000000000000

weightMatrix = network.memoryWeightMatrix
weightMatrix = np.where(weightMatrix == 0.5, '0000000010000000', weightMatrix)
weightMatrix = np.where(weightMatrix == '-0.5', '1111111110000000', weightMatrix)
weightMatrix = np.where(weightMatrix == '1.0', '0000000100000000', weightMatrix)
weightMatrix = np.where(weightMatrix == '-1.0', '1111111100000000', weightMatrix)
weightMatrix = np.where(weightMatrix == '0.0', '0000000000000000', weightMatrix)


## Trained Weight Matrix stored in a text file.
file = open("MemoryWeightMatrix.txt", "w")
for i in range(network.nodes):
    for j in range(network.nodes):
        file.write(weightMatrix[i][j])
        file.write('\n')
    # file.write('\n')
file.close()
# file1 = open("MemoryWeightMatrix.txt", "r")


## Individual weight file creation for neurons
file1 = open("MemoryWeightMatrix.txt", "r")
for i in range(25):
    file = open('n'+str(i+1)+'weights'+'.mif', "w")
    for j in range(25):
        e = file1.readline()
        file.write(e)
    file.close()

####################################################################################################################################
# from fxpmath import Fxp
# neuron1 = network.memoryWeightMatrix[24]
# print(neuron1)
# xxx = []
# for i in range(25):
#     if neuron1[i] == 1:
#         temp = Fxp(1, True, 16, 8)
#         xxx.append(temp)
#     if neuron1[i] == 0:
#         temp = Fxp(0, True, 16, 8)
#         xxx.append(temp)
#     if neuron1[i] == 0.5:
#         temp = Fxp(0.5, True, 16, 8)
#         xxx.append(temp)
#     if neuron1[i] == -0.5:
#         temp = Fxp(-0.5, True, 16, 8)
#         xxx.append(temp)
#     if neuron1[i] == -1:
#         temp = Fxp(-1, True, 16, 8)
#         xxx.append(temp)
# print(xxx)
#
# # for i in range(25):
# #     print(xxx[i].bin())
# y = [0, 0, 1, 1, 1,
#      0, 0, 0, 1, 0,
#      0, 0, 1, 0, 0,
#      0, 1, 0, 0, 0,
#      1, 1, 0, 1, 0]
# y = bipolarTransformation(y)
# y = np.array(y).reshape(25)
# # print(y.shape())
# y = list(y)
# print(y)
# yyy = []
# for i in range(25):
#     if y[i] == 1:
#         temp = Fxp(1, True, 16, 8)
#         yyy.append(temp)
#
#     if y[i] == -1:
#         temp = Fxp(-1, True, 16, 8)
#         yyy.append(temp)
#
# print(yyy)
#
# print()
# sum = 0
# for i in range(25):
#     sum += xxx[i] * yyy[i]
#
#
# print(sum)
# print(sum.bin())
# sum = Fxp(sum, True, 32, 16)
# print(sum.bin())
#
# # file =open()





####################################################################################################################################





