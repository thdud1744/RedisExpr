start_time=$(date +%T)
python redis_insertion.py
cat synthe10.txt | redis-cli --pipe
finish_time=$(date +%T)
echo ".....DONE....."
echo ${finish_time} - ${start_time} | bc