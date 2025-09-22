import matplotlib.pyplot as plt

year = [1950, 1951, 1952, 2100]
pop = [2.538, 2.570, 2.620, 10.850]

# Add more data points
year = [1800, 1850, 1900] + year
pop = [1.0, 1.262, 1.650] + pop

plt.plot(year, pop)

plt.xlabel("Year")
plt.ylabel("Population (millions)")
plt.title("World Population Projections")

plt.yticks([0, 2, 4, 6, 8, 10], ["0", "2B", "4B", "6B", "8B", "10B"])

# plt.grid()
plt.show()
