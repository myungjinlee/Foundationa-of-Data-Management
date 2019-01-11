#!/usr/bin/env python2.7

import sys
import numpy
import copy

f_obj=open(sys.argv[1],'r')

inmost=0
outmost=199

queue1_len=10
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
queue_bak=copy.copy(queue)

def create_queue1(curr_queue):
    queue1=[]
    if len(curr_queue)>queue1_len:
        for i in range(queue1_len):
            queue1.append(curr_queue[i])
    else:
        queue1=curr_queue
    return queue1

def get_closest(queue1_bak,loc):
    closest=None
    dislist=[]
    dist=outmost-inmost
    for q in queue1_bak:
        tmp=abs(loc-q)
        dislist.append(int(tmp))
    if dislist.count(min(dislist))>1:
        tmp=queue1_bak[dislist.index(min(dislist))]
        for i in range(len(dislist)):
            if dislist[i]==min(dislist) and queue1_bak[i]<=tmp:
                closest=queue1_bak[i]
    else:
        closest=queue1_bak[dislist.index(min(dislist))]
    queue1_bak.remove(closest)
    return closest

if (len(queue)%queue1_len)==0:
    num_loop=int(len(queue)/queue1_len)
else:
    num_loop=int(len(queue)/queue1_len)+1

sched=[]
total=0
pre=head
for k in xrange(num_loop):
    sched_tmp=[]
    queue1=create_queue1(queue_bak)
    bak=copy.copy(queue1)
    for i in queue1:
        curr=get_closest(bak,curr)
        sched.append(curr)
        sched_tmp.append(curr)
    del queue_bak[0:queue1_len]
    total+=abs(sched_tmp[0]-pre)
    for i in xrange(len(sched_tmp)-1):
        total+=abs(sched_tmp[i]-sched_tmp[i+1])
    i=0
    j=i+1
    sched_tmp.insert(0,pre)
    pre=sched_tmp[-1]
    if sched_tmp!=sorted(sched_tmp) and sched_tmp!=sorted(sched_tmp,reverse=True):
        if len(set(sched_tmp))!=len(sched_tmp):
            while len(set(sched_tmp))!=len(sched_tmp):
                if sched_tmp[i]==sched_tmp[j]:
                    sched_tmp.pop(j)
                else:
                    i+=1
                    j=i+1
        for i in xrange(len(sched_tmp)-2):
            if sched_tmp[i]>sched_tmp[i+1] and sched_tmp[i+1]<sched_tmp[i+2]:
                total+=abs((sched_tmp[i+1]-inmost))*2
            elif sched_tmp[i]<sched_tmp[i+1] and sched_tmp[i+1]>sched_tmp[i+2]:
                total+=(abs(sched_tmp[i+1]-outmost))*2

# print schedule,total cost,the maximum wait time request,and its time
str_var=''
for i in sched:
    str_var+=str(i)+','
str_var=str_var[:-1]
print str_var
print total
print str(sched[len(sched)-1])+','+str(total)


