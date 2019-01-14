#!/usr/bin/env python2.7

import sys
import json
import StringIO
import re
from collections import OrderedDict

f_obj=open(sys.argv[1],'r')
f_out_obj=open('1b.json','w')
obj=sys.argv[2]
obj=obj.lower()

s=''
slist=[]
for i in xrange(len(obj.split())):
    slist.append(obj.split()[i])

data=f_obj.read()
dic=json.loads(data)

doc=[]
dict=OrderedDict()
for i in dic["data"]:
    for j in i["paragraphs"]:
        for k in j["qas"]:
            compare=k["question"].lower()
            if all(re.compile(r'\b'+x+r'\b').search(compare.encode('utf-8')) for x in slist):
                tmp=OrderedDict()
                dict["id"]=k["id"]
                tmp.update(dict)
                dict["question"]=k["question"]
                tmp.update(dict)
                dict["answer"]=k["answers"][0]["text"]
                tmp.update(dict)
                doc.append(tmp)

infile=json.dumps(doc, indent=2)
infile=StringIO.StringIO(infile)
json_block=''
for line in infile:
       if line.strip()=='[':
           json_block+=str(line.strip())
       elif line.strip()==']':
           json_block+=str(line.strip())
       elif line.strip()=='{':
           json_block+=str('\n'+'  '+line.strip())
       elif line.strip()=='}':
           json_block+=str(line.strip()+'\n')
       elif line.strip().startswith('"answer"'):
           json_block+=str('   '+line.strip())
       elif line.strip().startswith('"question"'):
           json_block+=str('   '+line.lstrip())
       else:
           json_block+=str(line.lstrip())

for line in json_block:
    f_out_obj.write(line)

