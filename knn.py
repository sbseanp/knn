'''
Created on May 25, 2014

@author: Sean
'''
import sys
from sys import argv
from collections import Counter

'''find Euclidean distance and return list'''
def Euclid(x, y):
    sumSq=0.0
    L = []
    '''x is input, y is the neighbours vectors'''
    for i in range(len(x)):
        sumSq+=(x[i]-y[i])**2
    result = sumSq**0.5
    L.append(result)
    L.append(int(y[-1]))
    return L

'''returns list of all training data points'''
def train_classifier(filename):
    train_file = open(filename)
    '''get MxN'''
    row, col = map(int, train_file.readline().split())
    '''put all training data in list'''
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
    '''apply label line by line'''
    for line in test_file:       
        x = list(map(float, line.split()))
        '''find Euclidean distance for every point in training set and put into list'''
        Euclid_dist = []
        for i in range(len(n)):
            Euclid_dist.append(Euclid(x, n[i]))
        '''sort the distances'''
        Euclid_dist.sort()
        '''only keep the labels'''
        index = []
        for i in range(int(k)):
            index.append(str(Euclid_dist[i][-1]))
        '''find what occurs most often amongst all the labels'''
        mode = Counter(index)
        data = mode.most_common()
        '''remove anything that isn't tied for mode'''
        most = data[0][1]
        for i in range(len(data)):
            if most > data[i][1]:
                data[i] = 0
        mode = []
        for item in data:
            if item != 0:
                mode.append(item)
        '''if there is more than one label that applies, use nearest neighbour instead'''
        if (len(mode) > 1):
            reduced = []
            for i in range(len(mode)):
                key = int(mode[i][0])
                for j in range(len(Euclid_dist)):
                    if ((Euclid_dist[j][-1]) == key):
                        reduced.append(Euclid_dist[j])
            reduced.sort()
            result = reduced[0][-1]
            #result = int(Euclid_dist[0][-1])
        else:#otherwise, use the most common occurrence
            result = int(mode[0][0])
        '''print everything with sample formatting'''
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
        test_classifier(argv[3], argv[1], temp)
    else: 
        print('Please input k, the training file, and the test file')