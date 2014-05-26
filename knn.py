'''
Created on May 25, 2014

@author: Sean
'''

import sys
from sys import argv
import numpy as np
from collections import Counter

sys.stdout = open("HW3-4-output2.txt", 'w')

def add_vectors(a, b):
    '''Add vectors a and b '''
    assert len(a) == len(b)
    return [a[i]+b[i] for i in range(len(a))]

def multiply_scalar_vector(alpha, vec):
    '''Multiply vector vec with scalar alpha '''
    return [alpha*f for f in vec]

def Euclid(x, y):
    sumSq=0.0
    list = []
    '''x is input, y is the neighbours vectors'''
    for i in range(len(x)):
        sumSq+=(x[i]-y[i])**2
    result = sumSq**0.5
    list.append(result)
    list.append(int(y[-1]))
    return list

def train_classifier(filename):
    train_file = open(filename)
    row, col = map(int, train_file.readline().split())
    neighbours = []
    for line in train_file:
        x = list(map(float, line.split()))
        neighbours.append(x)
    train_file.close()
    return neighbours
        
def test_classifier(filename, k, n):
    test_file = open(filename)
    row, col = map(int, test_file.readline().split())
    count = 1
    for line in test_file:
        Euclid_dist = []
        x = list(map(float, line.split()))
        for i in range(len(n)):
            Euclid_dist.append(Euclid(x, n[i]))
        Euclid_dist.sort()
        index = []
        for i in range(int(k)):
            index.append(str(Euclid_dist[i][-1]))
        data = Counter(index)
        if (len(data) > 1):
            result = int(Euclid_dist[0][-1])
        else:
            result = data.most_common(1)
            result = int(result[0][0])
        print(count, end='')
        print('.',end=' ')
        print(x,end=' ')
        print('--',end=' ')
        print(result)
        count = count + 1
    test_file.close()

if __name__ == '__main__':
    if len(argv) == 4:
        temp = train_classifier(argv[2])
        temp2 = test_classifier(argv[3], argv[1], temp)
    else: 
        print('Please input the training file and the test file')