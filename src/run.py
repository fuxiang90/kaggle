#! /usr/bin/python

import json
import config

import numpy as np
import mlpy
import matplotlib.pyplot as plt # required for plotting


def main():
    
    fin = open(config.train_business )
    for each in fin:
        each_str = str(each)
        j = json.loads(each_str)
#         print type(j)
        print j['business_id']
        

def do1():
    mean1, cov1, n1 = [1, 5], [[1,1],[1,2]], 200 # 200 points, mean=(1,5)
    print mean1   
    x1 = np.random.multivariate_normal(mean1, cov1, n1)
    print x1


# items 里面是个二维 【a ,b】以a 的值进行排序
def get_k_max(items ,k):
    
#     arr = [0 for i in range(0,k)]assert 
    arr = []
    
    issort = 0
    for item in items :
        if len(arr) < k:
            arr.append(item)
        elif len(arr) == k:
            if issort == 0:
                arr = sorted(arr, cmp=lambda x,y : cmp(x[0], y[0]) ,reverse = True )
                issort = 1
            else:
                if item[0] > arr[0][0]:
                for i in range(0,k):
                    
                
                
                
if __name__ == "__main__":
    
#     main()
    do1()

    print "done it"

