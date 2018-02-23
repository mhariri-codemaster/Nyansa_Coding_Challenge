import sys
import datetime

def updateRecord(Record,date,url):
    if date in Record:
        check = True
        for count in Record[date]:
            if url in Record[date][count]:
                check = False
                Record[date][count].remove(url)
                if not Record[date][count]:
                    del Record[date][count]
                if count + 1 in Record[date]:
                    Record[date][count + 1].add(url)
                else:
                    Record[date][count + 1] = set([url])
                break
        if check:
            if 1 in Record[date]:
                Record[date][1].add(url)
            else:
                Record[date][1] = set([url])
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
