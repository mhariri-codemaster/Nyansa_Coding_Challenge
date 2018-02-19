import sys
import contextlib
from pyspark import SparkConf, SparkContext

SPARK_EXECUTOR_MEMORY = '2g'
SPARK_APP_NAME = 'Highest Poor Ratio Device'
SPARK_MASTER = 'local'

@contextlib.contextmanager
def spark_manager():
    conf = SparkConf().setMaster(SPARK_MASTER) \
                      .setAppName(SPARK_APP_NAME) \
                      .set("spark.executor.memory", SPARK_EXECUTOR_MEMORY)
    spark_context = SparkContext(conf=conf)
    try:
        yield spark_context
    finally:
	    spark_context.stop()

def tupleAdd(T1,T2):
    return (T1[0] + T2[0], T1[1] + T2[1])

def getHPRdevice(filepath):
    with spark_manager() as sc:
        ratings = sc.textFile(filepath) \
                    .map(lambda line: line.split("\"")) \
                    .map(lambda x: ((x[1], x[3]), (int(x[-1][2:-1]),1))) \
                    .reduceByKey(tupleAdd) \
                    .mapValues(lambda x: 1 if float(x[0])/float(x[1]) < 50.0 else 0) \
                    .map(lambda x: (x[0][1], (x[1], 1))) \
                    .reduceByKey(tupleAdd) \
                    .mapValues(lambda x: float(x[0])/float(x[1])) \
                    .max()
        print("\n\n"+ratings[0])
        return

def main(filepath):
    """
    :param string filepath:  path of file to summarize
    """
    try:
        getHPRdevice(filepath)
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
