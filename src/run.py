#! /usr/bin/python

import json
import config




def main():
    
    fin = open(config.train_business )
    for each in fin:
        each_str = str(each)
        j = json.loads(each_str)
#         print type(j)
        print j['business_id']
        
    

if __name__ == "__main__":
    
    main()
    print "done it"

