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
        self.stars = float (business_dict['stars'])
        self.latitude = business_dict['latitude']
        self.type = business_dict['type']
        self.review_count = business_dict['review_count']
        
        self.checkin_vec = [ [ 0 for j in range(24) ] for i in range(7) ]    
    
    def get_checkin_data(self,checkin_info_dict): 
        
        for each in checkin_info_dict.keys():
            len_each = len(each)
            if len_each == 3 :
                hour = int(each[:1])
            elif len_each == 4:
                hour = int(each[:2])
            
            weekday = int(each[len_each-1:])
            
            count = checkin_info_dict[each]
            
            
            self.checkin_vec[weekday][hour] = count
                
                

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

    for each in fin:

        business_dict = json.loads(each)
        data = BusinessData(business_dict)

        
        g_business_dict[  business_dict['business_id'] ] = data

        
    return g_business_dict


def get_checkin(filename ,g_business_dict):
    fin = open(filename)
    
    for each in fin:

        checkin_dict = json.loads(each)

        g_business_dict[ checkin_dict['business_id'] ].get_checkin_data(checkin_dict['checkin_info'])
        
    return checkin_dict
    

def get_review(filename ,g_review_dict):
    fin = open(filename)
    
    
    for each in fin:        

        review_dict = json.loads(each)
        data = ReviewData(review_dict)
        

        g_review_dict[  review_dict['business_id'] ] = data


    return g_review_dict
        
def main():
    g_business_dict = {}
    get_business(config.train_business,g_business_dict)
     
        
    g_checkin_dict = {}
     
    get_checkin(config.train_checkin, g_business_dict)
    
#     g_review_dict = {}
#     
#     get_review(config.train_review, g_review_dict)
    
    
    
    

if __name__ == '__main__':
    main()
    
    content = raw_input("input a num to exit")
    print "done it"