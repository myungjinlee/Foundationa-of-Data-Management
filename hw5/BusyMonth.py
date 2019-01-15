#!/usr/bin/env python2.7

import locale
import findspark
findspark.init()
from pyspark import SparkContext
from sys import argv
from pyspark.sql import SparkSession

sc=SparkContext(appName="inf551")
spark=SparkSession.builder.appName("inf551").getOrCreate()

lines=spark.read.text(argv[1]).rdd.map(lambda r: r[0])

result=lines.map(lambda s:s.split(","))\
            .filter(lambda y:y[2] == "Terminal 1" or y[2] == "Terminal 2" or y[2] == "Terminal 3" or y[2] == "Terminal 4"\
              or y[2] == "Terminal 5" or y[2] == "Terminal 6" or y[2] == "Terminal 7" or y[2] == "Terminal 8" or y[2] == "Tom Bradley International Terminal")\
            .map(lambda p:(str(p[1].split()[0]), int(p[5])))\
            .reduceByKey(lambda x,y:x+y)\
            .filter(lambda x:x[1]>5000000)

output=result.sortByKey().collect()

for i in range(len(output)):
    s=output[i][0].split("/")[0]
    p=output[i][0].split("/")[2]
    month=''.join((s,'/',p))
    print('%s    %s' % (month,"{:,}".format(output[i][1])))


