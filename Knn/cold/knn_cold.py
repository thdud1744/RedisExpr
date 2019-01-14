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

def knn_measurement(longi, lati, radius, numCount):
    r = redis.Redis(host='localhost', port=6379)
    start_time = time.time()
    # change key here!
    value = r.georadius('tweets', longi, lati, radius, 'km', count = numCount, sort = 'ASC')
    finish_time = time.time()
    num_result=len(value)
    return finish_time - start_time

def main():
    random = make_coordinates()
    duration = knn_measurement(random[0], random[1], 500, 1000)
    print(duration)

if __name__ == '__main__':
        main()