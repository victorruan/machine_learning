# Knn基础
import numpy as np
from math import sqrt
from collections import Counter

# k是Knn的k,X_train是点集合，y_train是分类结果，x是待预测点
def kNN_classify(k,X_train,y_train,x):
    distances = [sqrt(np.sum((point-x)**2))  for point in X_train]
    nearest = np.argsort(distances)
    topK_y =      [ y_train[i]   for i in nearest[:k]]
    votes = Counter(topK_y)
    return votes.most_common(1)[0][0]

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

predict_y = kNN_classify(6,X_train,y_train,x)

print(predict_y)
