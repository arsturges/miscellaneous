import matplotlib.pyplot as plt

def ones(n):
  length = len(str(n))
  number_of_ones = 0
  for digit in range(0,length):
    if int(str(n)[digit]) == 1:
      number_of_ones += 1
  return number_of_ones

import numpy as np
npx = np.arange(0,int(1e6))
vectorized_ones = np.vectorize(ones)
npy = vectorized_ones(npx)
npy = np.cumsum(npy)

plt.plot(npx, npy, label="f(n)")
plt.title("Number Line Puzzle")
plt.ylabel("Cumulative number of ones between 0 and n")
plt.xlabel("n")
plt.plot(npx,npx, label="x = y")
plt.legend()
plt.show()
