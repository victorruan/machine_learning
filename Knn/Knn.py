# Knn基础
import numpy as np
import matplotlib.pyplot as plt
raw_data_X = [
        [3.4,2.3],
        [3.1,1.8],
        [1.3,3.4],
        [3.6,4.7],
        [2.3,2.9],
        [7.4,4.7],
        [5.7,3.5],
        [9.2,2.5],
        [7.8,3.4],
        [7.9,0.8],
        ]


raw_data_y = [0,0,0,0,0,1,1,1,1,1]

X_train = np.array(raw_data_X)
y_train = np.array(raw_data_y)
x = np.array([8.1,3.4])
#print(X_train)

#print(y_train)
plt.scatter(X_train[y_train==0,0],X_train[y_train==0,1],color="g")
plt.scatter(X_train[y_train==1,0],X_train[y_train==1,1],color="r")
plt.scatter(x[0],x[1],color="b")
plt.show()

# kNN的过程
from math import sqrt
'''
distances = []

for x_train in X_train:
    d = sqrt(np.sum((x_train-x)**2))
    distances.append(d)

print(distances)
'''
distances = [  sqrt(np.sum((x_train-x)**2))    for x_train in X_train]
print(distances)
nearest = np.argsort(distances)
k = 6
topK_y = [  y_train[i]  for i in nearest[:k]]
print(topK_y)

from collections import Counter
votes = Counter(topK_y)
print(votes.most_common(1)[0][0])
