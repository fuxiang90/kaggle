# coding=utf-8
#! /usr/bin/python

import config
import json


class BusinessData(object):
    
    def __init__(self,business_dict):
        self.business_id = business_dict['business_id']
        self.full_address = business_dict['full_address']
        self.categories = business_dict['categories']
        self.city = business_dict['city']
        self.name = business_dict['name']
        self.neighborhoods = business_dict['neighborhoods']
        self.longitude = business_dict['longitude']
        self.stars = business_dict['stars']
        self.latitude = business_dict['latitude']
        self.type = business_dict['type']
        self.review_count = business_dict['review_count']

class CheckinData(object):
    def __init__(self,check_dict):
        
        self.info = check_dict['checkin_info']
        self.business_id = check_dict['business_id']

class ReviewData(object):
    
    def __init__(self,review_dict):
        self.votes = review_dict['votes']
        self.user_id = review_dict['user_id']
        self.review_id = review_dict['review_id']
        self.stars = review_dict['stars']
        self.date = review_dict['date']
        self.text = review_dict['text']
        self.business_id = review_dict['business_id']
 
 #得到business 的输入       
def get_business(filename ,g_business_dict):
    
    fin = open(filename)
    
    
    debug_i =  1
    for each in fin:
#         each_str = str(each)
        business_dict = json.loads(each)
        data = BusinessData(business_dict)
        
#         if business_dict['business_id'] not in g_business_dict :
#             g_business_dict[]
        
        g_business_dict[  business_dict['business_id'] ] = data
#         print type(j)
#         if debug_i > 10 : 
#             break
#     
# 
#         debug_i= debug_i + 1
    
#     for each_business in g_business_dict.keys():
#         
#         print each_business ,  g_business_dict[each_business].business_id
        
    return g_business_dict


def get_checkin(filename ,g_checkin_dict):
    fin = open(filename)
    
    
    debug_i =  1
    for each in fin:

        checkin_dict = json.loads(each)
#         print che
        data = CheckinData(checkin_dict)
        

        g_checkin_dict[  checkin_dict['business_id'] ] = data

#         if debug_i > 10 : 
#             break
#         debug_i= debug_i + 1
    
#     for each_checkin in g_checkin_dict.keys():
#         
#         print each_checkin ,  g_checkin_dict[each_checkin].business_id
        
    return checkin_dict
    

def get_review(filename ,g_review_dict):
    fin = open(filename)
    
    
    for each in fin:
        
#         print each
        review_dict = json.loads(each)
#         print che
        data = ReviewData(review_dict)
        

        g_review_dict[  review_dict['business_id'] ] = data

#         if debug_i > 10 : 
#             break
#         debug_i= debug_i + 1
    
#     for each_review in g_review_dict.keys():
#         
#         print each_review ,  g_review_dict[each_review].text
        
    return g_review_dict
        
def main():
    g_business_dict = {}
    get_business(config.train_business,g_business_dict)
     
        
    g_checkin_dict = {}
     
    get_checkin(config.train_checkin, g_checkin_dict)
    
    g_review_dict = {}
    
    get_review(config.train_review, g_review_dict)
    
    
    
    

if __name__ == '__main__':
    main()
    
    content = raw_input("input a num to exit")
    print "done it"