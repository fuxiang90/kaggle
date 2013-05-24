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
        self.stars = 0.0
        self.latitude = business_dict['latitude']
        self.type = business_dict['type']
        self.review_count = business_dict['review_count']
        
        self.checkin_vec = [ [ 0 for j in range(24) ] for i in range(7) ]
        
        self.cluster = 0
        
    def set_checkin_data(self,checkin_info_dict): 
        
        for each in checkin_info_dict.keys():
            len_each = len(each)
            if len_each == 3 :
                hour = int(each[:1])
            elif len_each == 4:
                hour = int(each[:2])
            
            weekday = int(each[len_each-1:])            
            count = checkin_info_dict[each]          
            
            self.checkin_vec[weekday][hour] = count
                
        
    def get_chink_info_vec(self):
        return self.checkin_vec
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

def get_test_checkin(filename, g_business_dict):  
    fin = open(filename)
    
    for each in fin:

        checkin_dict = json.loads(each)

        g_business_dict[ checkin_dict['business_id'] ].set_checkin_data(checkin_dict['checkin_info'])
        
    return checkin_dict  
def main():
    
    test_business_dict = {}
    get_test_business(config.test_business, test_business_dict)
    
    test_user_dict = {}
    get_test_user(config.test_user, test_user_dict)
    
    
if __name__ == '__main__':
    
    main()
    print "done it"
        
