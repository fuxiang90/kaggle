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
    
    

if __name__ == '__main__':

#     main()
    check_categories()
    print 'done it'