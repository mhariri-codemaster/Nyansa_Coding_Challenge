import sys
import datetime

def updateRecord(Record,count,date,url):
    if date in Record:
        check = True
        for j in range(1, count[date] + 1):
            if url in Record[date][j]:
                check = False
                Record[date][j].remove(url)
                if j + 1 in Record[date]:
                    Record[date][j + 1].add(url)
                else:
                    count[date] += 1
                    Record[date][j + 1] = set([url])
                break
        if check:
            Record[date][1].add(url)
    else:
        Record[date] = {1: set([url])}
        count[date] = 1

def summarizeFile(filepath):
    with open(filepath, 'r') as lines:
        Record = {}
        count = {} # max count for each date
        for line in lines:
            if line.split():
                timestamp, url = line.split('|')
                date = datetime.datetime.utcfromtimestamp(int(timestamp)).date()
                updateRecord(Record,count,date,url)
    dates = sorted(Record.keys())
    for date in dates:
        print(date.strftime("%m/%d/%Y")+" GMT")
        rec = Record[date]
        for j in range(count[date],0,-1):
            for url in rec[j]:
                print(url[:-1] + " " +str(j))

def main(filepath):
    """
    :param string filepath:  path of file to summarize
    """
    try:
        summarizeFile(filepath)
    except IOError:
        print("File not found. Remember to include the full file path")
        return

if __name__ == "__main__":
    try:
        if len(sys.argv)>1:
            main(sys.argv[1])
        else:
            print("Missing input file path")
    except KeyboardInterrupt:
        pass
