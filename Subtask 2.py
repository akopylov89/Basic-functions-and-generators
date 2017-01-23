#  -*- coding: UTF-8 -*-

from urllib2 import urlopen
from pprint import pprint
import json

url = 'http://www.reddit.com/r/python.json'

def to_reddit(subreddit):
    response = urlopen(url)
    content = response.read()
    data = json.loads(content)
    my_list = []
    for i in data:
        print(type(i))
        for j in i:
            print(type(j))

    # def to_subreddit(data=data):
    #     if isinstance(data, dict):
    #         for key,value in data:
    #             if isinstance(data[key],dict):
    #                 to_subreddit(data[key])
    #             elif isinstance(data[key], list):
    #                 for elem in data:
    #                     to_subreddit(elem)
    #             else:
    #                 print data["title"]
    #                 my_list.append(data['title'])
    #     elif isinstance(data, list):
    #         for elem in data:
    #             to_subreddit(elem)
    #     else:
    #         print data["title"]
    #         my_list.append(data['title'])
    # return my_list


if __name__ == '__main__':
    python = to_reddit('Python')
    print (python)
    # for elem in python:
    #     print(elem)

