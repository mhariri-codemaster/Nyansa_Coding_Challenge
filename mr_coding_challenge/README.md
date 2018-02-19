# Table of Contents
1. [Problem Statement](README.md#problem_statement)
2. [Requirements](README.md#requirements)
3. [Examples](README.md#examples)

# Problem Statement
The problem is to find the device type, from a list of devices, that has the highest poor-ratio (the ratio of poor instances of the device to the total given devices of that type). A device is poor if its average rating is less than 50 on a scale of 100. The full problem description can be found at:  
https://sites.google.com/a/nyansa.com/nyansa-programming-exercise-map-reduce/

# Requirements
Python 2.7.12
spark 2.2.1
pyspark

# Examples
To run the example input file given in examples/input.txt:  
$ python src/HPRdevice.py examples/input.txt  
or  
$ chmod 755 run.sh  
$ ./run.sh



