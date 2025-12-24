# Random walk
import numpy as np

np.random.seed(123)
tails = [0]
for x in range(10):
    coin = np.random.randint(0, 2)
    tails.append(tails[x] + coin)

# Distribution
import numpy as np

np.random.seed(123)
final_tails = []
for x in range(100):
    tails = [0]
    for x in range(10):
        coin = np.random.randint(0, 2)
        tails.append(tails[x] + coin)
    final_tails.append(tails[-1])

# print(final_tails)

# Visualizing the distrubtion
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
final_tails = []
for y in range(100):
    tails = [0]
    for x in range(10):
        coin = np.random.randint(0, 2)
        tails.append(tails[x] + coin)
    final_tails.append(tails[-1])
plt.hist(final_tails, bins=11)
plt.show()

# Better graphics
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)

# 1. More efficient way: Generate a 100x10 array of random 0s and 1s
# Each row is one trial of 10 flips
simulations = np.random.randint(0, 2, size=(100, 10))

# 2. Sum each row to get the total number of tails per trial
final_tails = np.sum(simulations, axis=1)

# 3. Plotting with better bin alignment
# We set bins to align with the integers 0 through 10
plt.hist(final_tails, bins=np.arange(12) - 0.5, edgecolor="black", alpha=0.7)
plt.xticks(range(11))
plt.xlabel("Number of Tails")
plt.ylabel("Frequency")
plt.title("Binomial Distribution (100 trials of 10 flips)")
plt.show()

# A Quick Tip on Efficiency
# If you just want the final counts and don't need to simulate the "walk"
#  step-by-step, you can skip the loops entirely using
np.random.binomial(n=10, p=0.5, size=100)

# 1000 times
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
final_tails = []
for y in range(100):
    tails = [0]
    for x in range(10):
        coin = np.random.randint(0, 2)
        tails.append(tails[x] + coin)
    final_tails.append(tails[-1])
plt.hist(final_tails, bins=10)
plt.show()

# 10,000 times
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
final_tails = []
for y in range(100):
    tails = [0]
    for x in range(10):
        coin = np.random.randint(0, 2)
        tails.append(tails[x] + coin)
    final_tails.append(tails[-1])
plt.hist(final_tails, bins=100)
plt.show()
