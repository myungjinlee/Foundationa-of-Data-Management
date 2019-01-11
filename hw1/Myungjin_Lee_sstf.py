#!/usr/bin/env python2.7

import sys
import numpy
import copy

f_obj=open(sys.argv[1],'r')

inmost=0
outmost=199

queue=[]
curr=0
for line in f_obj:
    check=line.rstrip()
    if ',' not in check:
        head=int(check)
        curr=head
    else:
        check=check.split(',')
        queue=[int(i) for i in check]

bak=copy.copy(queue)
def get_closest(loc):
    closest=None
    dislist=[]
    dist=outmost-inmost
    for q in bak:
        tmp=abs(loc-q)
        dislist.append(int(tmp))
    if dislist.count(min(dislist))>1:
        tmp=bak[dislist.index(min(dislist))]
        for i in range(len(dislist)):
            if dislist[i]==min(dislist) and bak[i]<=tmp:
                closest=bak[i]
    else:
        closest=bak[dislist.index(min(dislist))]
    bak.remove(closest)
    return closest

sched=[]
for i in queue:
    curr=get_closest(curr)
    sched.append(curr)


# calculate the total cost
total=0
for i in xrange(len(sched)-1):
    tmp=abs(sched[i]-sched[i+1])
    total+=tmp
total+=abs(head-sched[0])

# print schedule,total cost,the maximum wait time request,and its time
str_var=''
for i in sched:
    str_var+=str(i)+','
str_var=str_var[:-1]
print str_var
print total
print str(sched[len(sched)-1])+','+str(total)


