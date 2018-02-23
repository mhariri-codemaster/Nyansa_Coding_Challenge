import sys
import datetime

def updateRecord(Record,date,url):
    if date in Record:
        check = True
        for j in Record[date]:
            if url in Record[date][j]:
                check = False
                Record[date][j].remove(url)
                if j + 1 in Record[date]:
                    Record[date][j + 1].add(url)
                else:
                    Record[date][j + 1] = set([url])
                break
        if check:
            Record[date][1].add(url)
    else:
        Record[date] = {1: set([url])}

def summarizeFile(filepath):
    with open(filepath, 'r') as lines:
        Record = {}
        for line in lines:
            if line.split():
                timestamp, url = line.split('|')
                date = datetime.datetime.utcfromtimestamp(int(timestamp)).date()
                updateRecord(Record,date,url)
    dates = sorted(Record.keys())
    for date in dates:
        print(date.strftime("%m/%d/%Y")+" GMT")
        counts = sorted(Record[date].keys(),reverse=True)
        for count in counts:
            for url in Record[date][count]:
                print(url[:-1] + " " +str(count))

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
