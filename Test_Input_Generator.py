from fxpmath import Fxp  ## For Decimal to binary manupulation
import numpy as np

############################################################################################################################
##  Bipolar Conversion                                                                                                    ##
############################################################################################################################
def bipolarTransformation(vector):
    vector = np.array(vector).reshape(1, 5 * 5)
    vector = np.where(vector == 0, -1, vector)
    return vector


############################################################################################################################
##  Binary Conversion                                                                                                     ##
############################################################################################################################
# x = Fxp(-1, True, 16, 8)   # (val, signed, n_word, n_frac)
p = Fxp(-0.5, True, 16, 8)   # (Converting signed decimal into 16 bit binary with 8 fractional parts)
q = Fxp(1, True, 16, 8)
r = Fxp(0.5, True, 16, 8)
s = Fxp(0, True, 16, 8)

## -1   = 1111111100000000
## -0.5 = 1111111110000000
## 1    = 0000000100000000
## 0.5  = 0000000010000000
## 0    = 0000000000000000

############################################################################################################################
##  Test Data Generation for testing (Distorted inputs can be given to below list 'c'-                                     ##
##  -for any letter and a text file named testData.txt will be generated. This file needs to be included in verilog file   ##
############################################################################################################################

## Distorted N
# test = [1, 0, 0, 0, 0,
#         1, 1, 0, 0, 1,
#         1, 0, 1, 0, 1,
#         1, 0, 0, 1, 0,
#         1, 0, 0, 0, 1]

## Distorted Z
test = [0, 0, 1, 1, 1,
        0, 0, 0, 1, 0,
        0, 0, 1, 0, 0,
        0, 1, 0, 0, 0,
        1, 1, 0, 1, 0]

## Distorted C
# test = [1, 0, 1, 1, 0,
#         1, 0, 0, 0, 0,
#         0, 0, 0, 0, 1,
#         1, 0, 0, 0, 0,
#         1, 1, 0, 1, 0]

## Distorted T
# test = [1, 1, 1, 1, 0,
#         0, 0, 1, 0, 0,
#         1, 0, 1, 0, 0,
#         0, 0, 1, 0, 0,
#         0, 0, 0, 0, 0]

y = bipolarTransformation(test)
y = np.array(y).reshape(25)
y = list(y)

yyy = []
for i in range(25):
    if y[i] == 1:
        temp = Fxp(1, True, 16, 8)
        yyy.append(temp)

    if y[i] == -1:
        temp = Fxp(-1, True, 16, 8)
        yyy.append(temp)

rr = len(yyy)
file = open('testData.mif','w')
for i in range(25):
    # file.write("testdata[" + str(i) + "] = 16"+ "'" + "b" + yyy[rr-1].bin() + ";")
    file.write(yyy[i].bin())
    # rr = rr -1
    file.write('\n')
file.close()
############################################################################################################################

import matplotlib.pyplot as plt
import numpy as np

nb_patterns = 4  # Number of patterns to learn
pattern_width = 5
pattern_height = 5
max_iterations = 20

# Define Patterns
patterns = np.array([
    [-1, -1, -1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, -1, -1, -1, -1.],  # Letter C
    [-1, -1, -1, -1, -1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1.],  # Letter T
    [-1, 1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, 1, -1.],  # Letter N
    [-1, -1, -1, -1, -1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, -1, -1, -1, -1, -1.], ],  # Letter Z
    dtype=np.float64)

# Show the patterns
# fig, ax = plt.subplots(1, nb_patterns)

# for i in range(nb_patterns):
#     ax[i].matshow(patterns[i].reshape((pattern_height, pattern_width)), cmap='gray')
#     ax[i].set_xticks([])
#     ax[i].set_yticks([])

plt.show()

# Initialize Weight matrix
W = np.zeros((pattern_width * pattern_height, pattern_width * pattern_height))
WT = np.zeros((pattern_width * pattern_height, pattern_width * pattern_height))

# Train Network
for i in range(nb_patterns):
    for j in range(pattern_width * pattern_height):
        for k in range(pattern_width * pattern_height):
            WT[j][k] = patterns[i][j] * patterns[i][k]

    for l in range(pattern_width * pattern_height):
        WT[l][l] = 0
    W += WT
W = W / nb_patterns
# print(W)

# Create a corrupted pattern S
S = np.array([-1, -1, -1, -1, -1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1.],
             dtype=np.float64)

# Show the corrupted pattern
# fig, ax = plt.subplots()
# ax.matshow(S.reshape((pattern_height, pattern_width)), cmap='gray')
# plt.show()

# Test Network

R = np.matmul(S, W)
# print(R)
for n in range(pattern_height * pattern_width):
    if R[n] >= 0:
        R[n] = 1
    else:
        R[n] = -1

# fig, ax = plt.subplots()
# ax.matshow(R.reshape((pattern_height, pattern_width)), cmap='gray')
# plt.show()

print(W)
W = list(W)
W = np.array(W)

weightMatrix = W
weightMatrix = np.where(weightMatrix == 0.5, '0000000010000000', weightMatrix)
weightMatrix = np.where(weightMatrix == '-0.5', '1111111110000000', weightMatrix)
weightMatrix = np.where(weightMatrix == '1.0', '0000000100000000', weightMatrix)
weightMatrix = np.where(weightMatrix == '-1.0', '1111111100000000', weightMatrix)
weightMatrix = np.where(weightMatrix == '0.0', '0000000000000000', weightMatrix)

print(weightMatrix)



