#!/usr/bin/env python2.7

import locale
import findspark
findspark.init()
from pyspark import SparkContext
from sys import argv
from pyspark.sql import SparkSession

sc=SparkContext(appName="inf551")
spark=SparkSession.builder.appName("inf551").getOrCreate()

flights=spark.read.text(argv[1]).rdd.map(lambda r: r[0])
passeng=spark.read.text(argv[2]).rdd.map(lambda r: r[0])

def myfunc(data):
    for i in range(len(data)):
        new="".join(data)
        new_data=new.split(" ")
        key=", ".join(new_data[0:3])
        value=int(new_data[3])
        return key, value

result1=flights.map(lambda s:s.split(","))\
               .map(lambda p:(str(p[1].split()[0]), str(p[3]), str(p[4]), str(p[5])))\
               .map(lambda x:(" ".join(x)))\
               .map(lambda x:(x.split("/")))\
               .map(lambda z:(str(z[0]+'/'), str(z[2])))\
               .map(myfunc)\
               .reduceByKey(lambda a,b:a+b)\
               .sortByKey()

result2=passeng.map(lambda s:s.split(","))\
               .map(lambda p:(str(p[1].split()[0]), str(p[3]), str(p[4]),str(p[5])))\
               .map(lambda x:(" ".join(x)))\
               .map(lambda x:(x.split("/")))\
               .map(lambda z:(str(z[0]+'/'), str(z[2])))\
               .map(myfunc)\
               .reduceByKey(lambda a,b:a+b)\
               .sortByKey()



output=result1.join(result2).sortByKey().collect()

for i in range(len(output)):
    print(str(output[i][0])+','+' '+str(output[i][1][0])+','+' '+str(output[i][1][1]))



