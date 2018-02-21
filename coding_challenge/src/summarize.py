import sys
import datetime

def updateRecord(Record,date,url):
    if date in Record:
        if url in Record[date]:
            Record[date][url] += 1
        else:
            Record[date][url] = 1
    else:
        Record[date] = {url: 1}

def summarizeFile(filepath):
    with open(filepath, 'r') as lines:
        Record = {}
        for line in lines:
            if line.split():
                timestamp, url = line.split('|')
                try:
                    date = datetime.datetime.utcfromtimestamp(int(timestamp)).date()
                    updateRecord(Record,date,url)
                except ValueError:
                    print("Invalid timestamp "+timestamp+" encountered. Skipping ...")
                    continue
    dates = sorted(Record.keys())
    for date in dates:
        print(date.strftime("%m/%d/%Y")+" GMT")
        rec = Record[date]
        urls = sorted(rec,key=rec.__getitem__,reverse=True)
        for url in urls:
            print(url[:-1] + " " +str(rec[url]))

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
