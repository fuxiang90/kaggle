# coding=utf-8
#! /usr/bin/python

# 简单的通过物品的分来来预测
import config
import json


import train_input
import test_input

def compute_test_business_stars(train_business_dict,test_business_dict ):
    categories_stars_dict = {} 
    
    for each in train_business_dict.keys():
        
        categories_list =  train_business_dict[each].categories 
        stars = train_business_dict[each].stars
        for each_categories in categories_list:
            if each_categories not in categories_stars_dict :
                categories_stars_dict [each_categories] = []
            categories_stars_dict[each_categories].append(stars)
    
    ## 计算test_business_dict 里面的平均值
    for each in test_business_dict.keys():
        
        categories_list =  test_business_dict[each].categories 
        sum_stars = 0
        count = 0
        for each_categories in categories_stars_dict:
            sum_stars = sum_stars + sum( categories_stars_dict[each_categories] )
            count = count + len(categories_stars_dict[each_categories] )
        test_business_dict[each].stars = sum_stars*1.0 / count

    compute_test_review(config.test_review ,train_business_dict,test_business_dict)

def compute_test_review(filename,train_business_dict,test_business_dict):
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
    
    
  
            
       
    

def main():
    train_business_dict = {}
    train_input.get_business(config.train_business, train_business_dict)
    
    
    test_business_dict = {}
    test_input.get_test_business(config.test_business, test_business_dict)
    
    
    compute_test_business_stars(train_business_dict ,test_business_dict)


if __name__ == "__main__":
    
    main() 

    print  "done it"