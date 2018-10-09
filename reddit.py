#!/usr/bin/python3 
import sys
import pprint
from helper import crawler

pp = pprint.PrettyPrinter(indent=2)

def main(arg,main=True):
    result=[]
    url = 'https://www.reddit.com/r/worldnews/top/?sort=top&t=day'
    cur_result = crawler.get_data(url)
    if(cur_result!=None):
        result.extend(cur_result)   
    if(main):
        for item in result:
            pp.pprint(item)
    return result

if __name__ == "__main__":
    main(sys.argv)