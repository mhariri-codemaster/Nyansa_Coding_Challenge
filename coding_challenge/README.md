# Table of Contents
1. [Problem Statement](README.md#problem_statement)
2. [Complexity Analysis](README.md#complexity_analysis)
3. [Requirements](README.md#requirements)
4. [Examples](README.md#examples)

# Problem Statement
The problem is to summarize a list of unordered url and timestamp combinations. The full problem description can be found at:  
https://sites.google.com/a/nyansa.com/nyansa-programming-exercise/

# Complexity Analysis
If N is the number of unique urls in the file and assuming that the number of url counts and dates is O(1) compared to N (The problem statement indicates that these values are much smaller than N) then the complexity of the code will be:  

## src/summarize.py
O(NlogN) as follows:  
**Stage 1:**  
The code will build the records line by line form the input file. The number of lines will be O(N) based on the assumptions above  
The input line is split O(1)  
The timestamp is converted to date O(1)  
The new url is added or updated in the record O(1)  
Therefore, reading the file and updating the record will require O(N) time and O(N) memory  
**Stage 2:**  
The dates are sorted. Since we assumed O(1) dates then this will require O(1)  
An O(1) loops are required over the dates  
Sorting the urls for each date is O(NlogN)  
printing the urls is O(N)  
Therefore looping through all the records and sorting will require O(NlogN) time and O(N) memory

## src/summarize2.py
O(N) as follows:  
**Stage 1:**  
The code will build the records line by line form the input file. The number of lines will be O(N) based on the assumptions above  
The input line is split O(1)  
The timestamp is converted to date O(1)  
The new url is added or updated in the record O(1) as follows:  
-- Only hashmaps are used so lookup is O(1)  
-- If the date is not in the records, add the date and the url at count 1 O(1)  
-- Otherwise check if the url is in any of the counts for that date. Since we assumed the number of counts is small, this will be done in O(1) time  
-- The url position is updated accordingly in O(1)
Therefore, reading the file and updating the record will require O(N) time and O(N) memory for the full file  
**Stage 2:**  
The dates are sorted. Since we assumed O(1) dates then this will require O(1)  
An O(1) loops are required over the dates  
The counts are sorted as well. Since we assumed O(1) counts, then this will require O(1) time  
printing the urls is O(N)  
Therefore looping through all the records and sorting will require O(N) time and O(N) memory

# Requirements
Python 2.7

# Examples
To run the example input file given in examples/input.txt:  
$ python src/summarize.py examples/input.txt  
$ python src/summarize2.py examples/input.txt  
or  
$ chmod 755 run.sh  
$ ./run.sh



