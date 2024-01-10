import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("data1-1.csv", names=['sal'])

# Histogram: bin counts and edges
counts, edges = np.histogram(data['sal'], bins=32, range=[0, 161262])

# Bin centers and widths for plotting
centers = 0.5 * (edges[1:] + edges[:-1])
widths = edges[1:] - edges[:-1]

# Probability density (assuming 'y' contains density values)
pdf = counts / sum(counts)

# Plot PDF
plt.figure(figsize=(8, 6))
plt.bar(centers, pdf, width=0.9 * widths)

# Mean salary
mean_sal = np.sum(centers * pdf)
# Plot mean line
plt.plot([mean_sal, mean_sal], [0, max(pdf)], c='red')
plt.text(25000, max(pdf), f'Mean value: {int(mean_sal)}', fontsize=12, c='red')

# Find index closest to target cumulative prob
target_cp = 0.67
cdf = np.cumsum(pdf)
closest_idx = np.argmin(np.abs(cdf - target_cp))
sal_cp = edges[closest_idx]

# Histogram beyond target cumulative prob in green
plt.bar(centers[closest_idx:], pdf[closest_idx:], width=0.9 * widths[closest_idx:], color='green')

# Vertical line at target cumulative prob
plt.plot([sal_cp, sal_cp], [0, max(pdf)], c='black')
text = '''X value above 33%'''
plt.text(x=60000, y=max(ydst) - 0.01, s=text, fontsize=12, c='black')

# Labeling the axes

plt.xlabel("Annual Salary (Euros)")
plt.ylabel("Probability Density")
plt.title("Salary Distribution")
plt.show()
