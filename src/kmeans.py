# coding=utf-8
#! /usr/bin/python

import json
import config
import train_input
import test_input

import numpy as np
import mlpy
import matplotlib.pyplot as plt # required for plotting


def test1():
    np.random.seed(0)
    mean1, cov1, n1 = [1, 5], [[1,1],[1,2]], 200 # 200 points, mean=(1,5)
    x1 = np.random.multivariate_normal(mean1, cov1, n1)
    mean2, cov2, n2 = [2.5, 2.5], [[1,0],[0,1]], 300 # 300 points, mean=(2.5,2.5)
    x2 = np.random.multivariate_normal(mean2, cov2, n2)
    mean3, cov3, n3 = [5, 8], [[0.5,0],[0,0.5]], 200 # 200 points, mean=(5,8)
    x3 = np.random.multivariate_normal(mean3, cov3, n3)
    x = np.concatenate((x1, x2, x3), axis=0) # concatenate the samples
    cls, means, steps = mlpy.kmeans(x, k=3, plus=True)
    print means


##计算两个向量的距离
def distance(a ,b):
    a = np.array(a)
    b = np.array(b)
    
    return np.linalg.norm(a-b)
def set__business_cluster(means ,train_business_dict ):
    
    pass

### 
def kmeans_compute_test_review(filename,train_business_dict,test_business_dict):
    fin = open(filename,'r')
    
    import csv
 
    writer=csv.writer(open('sumbut.csv', 'wb'))
    writer.writerow(['user_id', 'businsess_id', 'stars'])
    for each in fin:
        review_dict = json.loads(each)
        business_id = review_dict['business_id']
        item = [review_dict['user_id'] ,review_dict['business_id'] ]
        if business_id in train_business_dict :
#             print "in train"
            item.append(train_business_dict[business_id].stars)
        if business_id in test_business_dict :
#             print "in test"
            item.append(test_business_dict[business_id].stars)
#         item = [review_dict['user_id'] ,review_dict['business_id'] ,test_business_dict[business_id].stars ]
        writer.writerow(item)
    
    fin.close()

# 得到最相似k 个business ，得到他们的平均得分
def get_near_k_means(train_business_dict ,test_business_dict, business_id ,k):
    
    items = []
    for each in train_business_dict :
        item = []
        item.append(  distance(train_business_dict[each].checkin_vec , test_business_dict[business_id].checkin_vec) )
        
        item.append(train_business_dict[each].stars  )
        
        items.append(item)
    sorted(items, cmp=lambda x,y : cmp(x[0], y[0]) ,reverse=True)
    
    result = 0.0
    for i in range(0,k):
        result = result + items[i][1]
    
    result = result / k
    return result

# 如果使用checkin 作为评判标准
#
#
def k_compute_test_review(filename,train_business_dict,test_business_dict,means,means_star):
#     fin = open(filename,'r')
#     
#     import csv
#  
#     writer=csv.writer(open('sumbut.csv', 'wb'))
#     writer.writerow(['user_id', 'businsess_id', 'stars'])
#     for each in fin:
#         review_dict = json.loads(each)
#         business_id = review_dict['business_id']
#         item = [review_dict['user_id'] ,review_dict['business_id'] ]
#         if business_id in train_business_dict :
# #             print "in train"
#             item.append(train_business_dict[business_id].stars)
#         if business_id in test_business_dict :
#             item.append( get_near_k_means(train_business_dict, test_business_dict, business_id, 6 ) )
#         
#         writer.writerow(item)
#     
#     fin.close()
    fin = open(filename,'r')
    
    import csv
 
    writer=csv.writer(open('sumbut.csv', 'wb'))
    writer.writerow(['user_id', 'businsess_id', 'stars'])
    for each in fin:
        review_dict = json.loads(each)
        business_id = review_dict['business_id']
        item = [review_dict['user_id'] ,review_dict['business_id'] ]
        if business_id in train_business_dict :
#             print "in train"
            item.append(train_business_dict[business_id].stars)
        if business_id in test_business_dict :
            near_cluster = 0
            min_dist = 100000000
            for each_mean in  range(0,100):
            
                dist = distance(test_business_dict[business_id].checkin_vec, means[each_mean])
            
                if dist < min_dist:
                    near_cluster = each_mean
                    min_dist = dist
            item.append(1.0 * means_star[near_cluster][0] / means_star[near_cluster][1])
        writer.writerow(item)
    
    fin.close()

def get_cluster():
    pass
def main():
    train_business_dict = {}
    train_input.get_business(config.train_business, train_business_dict)
    
    train_input.get_checkin(config.train_checkin, train_business_dict)
    
    test_business_dict = {}
    test_input.get_test_business(config.test_business, test_business_dict)
    
    test_input.get_test_checkin(config.test_checkin,test_business_dict)
    
    
    
    kmeas_input = []
    for each in train_business_dict:
        
        l = train_business_dict[each].get_chink_info_vec()
        kmeas_input.append(l)
    
    ### 用mlpy 对checkin 的数据进行聚类   
    x = np.concatenate((kmeas_input), axis=0)
    cls, means, steps = mlpy.kmeans(x, k=100, plus=True)
    
    means_star = [ [0,0] for i in range(0,100)]
    
    ##计算每个train_business 属于哪个类
    for each in train_business_dict:
        
        check_vec = train_business_dict[each].checkin_vec
        
        near_cluster = -1
        min_dist = 100000000
        for each_mean in  range(0,100):
            
            dist = distance(check_vec, means[each_mean])
            
            if dist < min_dist:
                near_cluster = each_mean
                min_dist = dist
        print near_cluster
        means_star[near_cluster][0] = means_star[near_cluster][0] + train_business_dict[each].stars
        means_star[near_cluster][1] = means_star[near_cluster][1] + 1
        
    #然后计算每个business
    
    k_compute_test_review( config.test_review,train_business_dict,test_business_dict,means,means_star)
    
    
if __name__ == '__main__':
    
    main()