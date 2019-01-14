import redis
from random import *
import time
import json

def make_coordinates():
    MIN_X_VALUE = -121.34249499999999
    MAX_X_VALUE = -117.41711999999995
    MIN_Y_VALUE = 32.806193000000064
    MAX_Y_VALUE = 36.73986200000007
    randomX = uniform(MIN_X_VALUE,MAX_X_VALUE)
    randomY = uniform(MIN_Y_VALUE,MAX_Y_VALUE)
    random_coord = [randomX, randomY]
    return random_coord

def insertion_measurement(key, longi, lati, member):
    r = redis.Redis(host='localhost', port=6379)
    start_time = time.time()
    value = r.geoadd(key, longi, lati, member)
    finish_time = time.time()
    #print("%s seconds" %(finish_time - start_time))
#        print(value)
    return finish_time - start_time

def delete_measurement(key, member):
    r = redis.Redis(host='localhost', port=6379)
    start_time = time.time()
    value = r.zrem(key, member)
    finish_time = time.time()
    #print("%s seconds" %(finish_time - start_time))
#        print(value)
    return finish_time - start_time


def main():
    insert_set = []
    delete_set = []
    random = make_coordinates()
    #print(random)
    for x in xrange(1,102):
        insert_duration = insertion_measurement('synthe10', random[0], random[1], 'h:10000001')
        insert_set.append(insert_duration)
        delete_duration = delete_measurement('synthe10', 'h:10000001')
        delete_set.append(delete_duration)
    insert_set = insert_set[1:]
    delete_set = delete_set[1:]
    insert_avg = sum(insert_set) / len(insert_set)
    delete_avg = sum(delete_set) / len(delete_set)
    print("insert ")
    print(insert_avg)
    print("delete ")
    print(delete_avg)

if __name__ == '__main__':
        main(