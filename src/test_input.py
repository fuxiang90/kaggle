# coding=utf-8
#! /usr/bin/python

import config
import json

class TestBusinessData(object):
    
    def __init__(self,business_dict):
        self.business_id = business_dict['business_id']
        self.full_address = business_dict['full_address']
        self.categories = business_dict['categories']
        self.city = business_dict['city']
        self.name = business_dict['name']
        self.neighborhoods = business_dict['neighborhoods']
        self.longitude = business_dict['longitude']
#         self.stars = business_dict['stars']
        self.latitude = business_dict['latitude']
        self.type = business_dict['type']
        self.review_count = business_dict['review_count']
        

class TestUserData(object):
    
    def __init__(self,user_dict):
        {"user_id": "LVc6c7dS2EtO7PY4MfKcEg", "review_count": 1, "name": "A", "type": "user"}
        
        self.user_id = user_dict['user_id']
        self.name = user_dict['name']


def get_test_business(filename ,test_business_dict):
    
    fin = open(filename)   
    for each in fin:
        business_dict = json.loads(each)
        data = TestBusinessData(business_dict)
        test_business_dict[  business_dict['business_id'] ] = data

        
    return test_business_dict

def get_test_user(filename ,test_user_dict):
    
    fin = open(filename)   
    for each in fin:
        business_dict = json.loads(each)
        data = TestUserData(business_dict)
        test_user_dict[  business_dict['user_id'] ] = data

        
    return test_user_dict
    
def main():
    
    test_business_dict = {}
    get_test_business(config.test_business, test_business_dict)
    
    test_user_dict = {}
    get_test_user(config.test_user, test_user_dict)
    
    
if __name__ == '__main__':
    
    main()
    print "done it"
        