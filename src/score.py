# coding=utf-8
#! /usr/bin/python

"""

评分 
将train review 分割成测试集和训练集 ，这样就可以自己测试 
"""

import config
import time
import json

def split_train_review():
    fout1 = open(config.my_train_review,"w")
    fout2 = open(config.my_test_review,"w")
    
    fin = open(config.train_review)
    
    pos = 0 
    for each in fin:
        if pos % 8 == 0:
            fout2.write(each)
        else :
            fout1.write(each)
        pos += 1

def rmse(predict_csv_file  , test_filename):
    import csv
    
    actual_review_dict = {}
    fin = open(test_filename)
    for each in fin:
        each_dict = json.loads(each)
         
        user_id = each_dict['user_id']
        business_id = each_dict['business_id']
        stars = float(each_dict['stars'])
         
        if user_id not in actual_review_dict:
            actual_review_dict[user_id] = {}
        actual_review_dict[user_id][business_id] = stars
    fin.close()
    
    predict_review_dict = {}
    reader = csv.reader(open(predict_csv_file ,"rb" ))
    
    pos = 0
    for row in reader:
        pos += 1
        if pos == 1 :
            continue
        
        print row
        user_id = row[0]
        business_id = row[1]
        stars = float(row[2])
        if user_id not in predict_review_dict:
            predict_review_dict[user_id] = {}
        predict_review_dict[user_id][business_id] = stars
        
    
    
    score = 0.0
    
    n = 0
    for each in predict_review_dict:
        for each_bu in predict_review_dict[each]:
            
            predict_stars = predict_review_dict[each][each_bu]
            actual_stars = actual_review_dict[each][each_bu]
            
            n += 1
            
            score += (predict_stars - actual_stars)**2
    score /= n
    
    score = score**(0.5)
    
    print score 
    return score
if __name__ == '__main__':
#     split_train_review()
    
    rmse("../submit/June-17-07-41-submit.csv",config.my_test_review)
    print "done it"

