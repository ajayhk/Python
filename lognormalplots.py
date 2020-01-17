import matplotlib.pyplot as plt
import numpy as np
mu = -4.6
sigma = 1.35
for i in range(10):
  a = np.random.lognormal(mu, sigma, 1000)
  count, bins, ignored = plt.hist(a, 100, normed=True, align='mid')
  x = np.linspace(min(bins), max(bins), 10000)
  pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2)) / (x * sigma * np.sqrt(2 * np.pi)))
  plt.plot(x, pdf, linewidth=2, color='r')
  plt.axis('tight')
  plt.show()
  plt.plot(a)
  plt.show()
