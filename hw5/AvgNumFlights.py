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

def myfunc(data):
    for i in range(len(data)):
        new="".join(data)
        new_data=new.split(" ")
        key=", ".join(new_data[0:2])
        value=int(new_data[2])
        return key, value

result=lines.map(lambda s:s.split(","))\
               .map(lambda p:(str(p[1].split()[0]), str(p[3]), str(p[5])))\
               .map(lambda x:(" ".join(x)))\
               .map(lambda x:(x.split("/")))\
               .map(lambda z:str(z[2]))\
               .map(myfunc)\
               .aggregateByKey((0,0), lambda U,v: (U[0]+v, U[1]+1), lambda U1,U2:(U1[0]+U2[0], U2[1]+U2[1]))\
               .map(lambda (x,(y,z)):(x,(float(y)/z)))

output=result.sortByKey().collect()

for i in range(len(output)):
    print(str(output[i][0])+','+' '+str(int(output[i][1])))
 


