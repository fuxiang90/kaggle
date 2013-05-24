# coding=utf-8
#! /usr/bin/python

import config
import json


import train_input
import test_input


def main():
    
    train_business_dict = {}
    train_input.get_business(config.train_business, train_business_dict)
    
    
    test_business_dict = {}
    test_input.get_test_business(config.test_business, test_business_dict)
    
    
    test_len = len(test_business_dict.keys())
    test_count = 0
    for each in test_business_dict.keys():
        
        if each in train_business_dict:
            test_count = test_count + 1
    
    
    print test_count 
    print '\n'
    print  test_len
    
    train_review_dict = {}
    train_input.get_review(config.train_review, train_review_dict)
    
    test_user_dict = {}
    test_input.get_test_user(config.test_user, test_user_dict)
    
    
    train_len = len(train_review_dict.keys())
    train_count = 0
    for each in train_review_dict.keys():
        
        user_id = train_review_dict[each].user_id
        
        if user_id in test_user_dict :
            train_count = train_count + 1
    
    print train_count 
    print '\n'
    print  train_len
    

def check_categories():
    
    train_business_dict = {}
    train_input.get_business(config.train_business, train_business_dict)     
    train_input.get_checkin(config.train_checkin, train_business_dict)
    
    test_business_dict = {}
    test_input.get_test_business(config.test_business, test_business_dict)
    test_input.get_test_checkin(config.test_checkin ,test_business_dict)
    
    categories_dict = {}
    for each in train_business_dict.keys():
        
        categories_list =  train_business_dict[each].categories 
        
        for each_categories in categories_list:
            if each_categories not in categories_dict :
                categories_dict[each_categories] = len(categories_dict.keys()) + 1
    
    
    for each in train_business_dict.keys():
        
        categories_list =  train_business_dict[each].categories 
        
        for each_categories in categories_list:
            if each_categories not in categories_dict :
               print "test" + each_categories
    
    
    print len (categories_dict.keys())
    

# 检查 train 中 user 有多少个 在 test 的review 中出现过
def check_review_user():
    
    fin = open(config.test_review)
    user_set = set()
    for each in fin:
        review_dict = json.loads(each)
        user_set.add(review_dict['user_id'])
    len_user_set = len(user_set)
    
    len_count = 0
    train_review_dict = {}
    train_input.get_review(config.train_review, train_review_dict)
    
    for each in train_review_dict.keys():
        userid = train_review_dict[each].user_id
        if userid in user_set:
            len_count = len_count + 1
    
    print len_count 
    print len_user_set
        
        
    
    
# 检查 train 中 business 有多少个 在 test 的review 中出现过
def check_review_business():
    fin = open(config.test_review)
    business_set = set()
    for each in fin:
        review_dict = json.loads(each)
        business_set.add(review_dict['user_id'])
    len_business_set = len(business_set)
    
    len_count = 0
    train_review_dict = {}
    train_input.get_review(config.train_review, train_review_dict)
    
    for each in train_review_dict.keys():
        business_id = train_review_dict[each].business_id
        if business_id in business_set:
            len_count = len_count + 1
    
    print len_count 
    print len_business_set
    pass

if __name__ == '__main__':

#     main()
#     check_categories()
#     check_review_business()
    check_review_user()
    print 'done it'
