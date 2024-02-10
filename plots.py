import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set_style('darkgrid')

# for scatter plot
X = np.random.normal(size=100)
y = np.random.normal(size=100)
plt.scatter(X, y)
plt.show()

# for bar plot
X = ['A', 'B', 'C', 'D', 'E']
y = [10, 20, 30, 40, 50]
plt.bar(X, y)
plt.show()

# for pie chart
X = [150, 200, 350, 400, 550]
plt.pie(X, labels=['A', 'B', 'C', 'D', 'E'])
plt.show()

#for subplots
X = np.random.normal(size=100)
y = np.random.normal(size=100)
plt.subplot(1, 1, 1)
plt.scatter(X, y, ax=[0,0])
plt.hist(X, bins=20)
plt.show()