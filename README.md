# py4k-means

K-Means Python Library

## Getting Started

This project is simply implementation of K-Means clustering algorithm in python programming language.

### Prerequisites

Numpy & Pandas


### Installing

The easiest way to install py4k-means is using pip

```
pip install py4k-means
```

### Usage
There is only 1 public method of k_means class. It is cluster. cluster method takes 3 argument namely x, k, and max_iter. x is the data its self, k is the number of cluster we are aiming to, while max_iter is maximum iteration. By default max_iter is 10. The return of this method is pandas DataFrame with 1 column addition, it is the label column obtained by K-Means algorithm
```
from py4k_means.cluster import k_means
import numpy as np
import matplotlib.pyplot as plt
x = [np.random.uniform(-5,5 ,2) for i in range(500)]
km = k_means()
y = km.cluster(x,4,20)
plt.scatter(y['x0'],y['x1'],c=y['label'],cmap='rainbow')
plt.show()
```
<img src="https://ibb.co/N61nXYN">
