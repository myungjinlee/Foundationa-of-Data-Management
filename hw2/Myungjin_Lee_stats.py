#!/usr/bin/env python2.7

import sys
import numpy
import json

f_obj=open(sys.argv[1],'r')
f_out_obj=open('1a.json','w')

data=f_obj.read()
dic=json.loads(data)

how=0
how_many=0
how_much=0
what=0
when=0
where=0
which=0
who=0
whom=0

for i in dic["data"]:
    for j in i["paragraphs"]:
        for k in j["qas"]:
            k["question"]=k["question"].strip().lower()
            if k["question"].startswith("how") or k["question"].startswith("how's") :
                if k["question"].startswith("how many"):
                    how_many+=1
                elif k["question"].startswith("how much"):
                    how_much+=1
                else:
                    how+=1
            elif k["question"].startswith("what") or k["question"].startswith("what's") or k["question"].startswith("whatare"):
                what+=1                
            elif k["question"].startswith("when") or k["question"].startswith("when's"):
                when+=1
            elif k["question"].startswith("where") or k["question"].startswith("where's"):
                where+=1
            elif k["question"].startswith("which") or k["question"].startswith("which's"):
                which+=1
            elif k["question"].startswith("who") or k["question"].startswith("who's") or k["question"].startswith("whose"):
                who+=1
            elif k["question"].startswith("whom"):
                whom+=1
doc={"how":how,"how many":how_many,"how much":how_much,"what":what,"when":when,"where":where,"which":which,"who":who,"whom":whom}

f_out_obj.write(json.dumps(doc))

