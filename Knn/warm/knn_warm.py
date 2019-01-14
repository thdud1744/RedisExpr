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
    value = r.georadius('streets', longi, lati, radius, 'km', count = numCount, sort = 'ASC')
    finish_time = time.time()
    #print("%s seconds" %(finish_time - start_time))
    #print(value)
    return finish_time - start_time

def main():
    timeSet = []
    for x in xrange(1,102):
        random = make_coordinates()
        #print(random)
        #print(x)
        duration = knn_measurement(random[0], random[1], 1000, 10)
        timeSet.append(duration)
    timeSet = timeSet[1:]
    average = (sum(timeSet) / len(timeSet))
    print(average)

if __name__ == '__main__':
        main()