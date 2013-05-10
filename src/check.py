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

if __name__ == '__main__':

    main()
    print 'done it'