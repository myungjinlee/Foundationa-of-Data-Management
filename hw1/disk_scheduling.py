# By greg temchenko for De Anza CIS 31
 
# Suppose that a disk drive has 5000 cylinders, numbered 0 to 4999. The drive is currently serving a request at cylinder 143, and the previous request was at cylinder 125. The queue of pending requests, in FIFO order, is
#         86, 1470, 913, 1774, 948, 1509, 1022, 1750, 130
# Starting from the current head position, what is the total distance (in cylinders) that the disk arm moves to satisfy all the pending requests, for each of the following disk-scheduling algorithms?
# a. FCFS
# b. SSTF
# c. SCAN
# d. LOOK
# e. C-SCAN
# f. C-LOOK
 
import copy
 
queue = [143, 86, 1470, 913, 1774, 948, 1509, 1022, 1750, 130]
 
# FCFS
prev = None
total = 0
for i in queue:
    if prev is not None:
        total += abs(i-prev)
        prev = i
    else:
        prev = i
print "a. FCFS:", total
 
 
# SSTF
q = copy.copy(queue)
def find_nearest(n):
    nearest = None
    for i in q:
        if nearest is None:
            nearest = i
        elif abs(i-n) < abs(nearest-n):
            nearest = i
    return nearest
 
curr = q.pop(0)
total = 0
seq = [curr]
while len(q)>0:
    nxt = find_nearest(curr)
    seq.append(nxt)
    total += abs(nxt - curr)
    q.remove(nxt)
    curr = nxt
print "b. SSTF:", total, seq
 
 
# SCAN
q = copy.copy(queue)
total = 0
direction = 1
curr = q.pop(0)
seq = [curr]
while len(q)>0:
    curr += direction
    total += 1
    if curr in q:
        q.remove(curr)
        seq.append(curr)
    if curr == 4999:
        direction = -1
    if curr == 0:
        direction = 1
print "c. SCAN:", total, seq
 
# LOOK
q = copy.copy(queue)
total = 0
direction = 1
curr = q.pop(0)
seq = [curr]
while len(q)>0:
    curr += direction
    total += 1
    if curr in q:
        q.remove(curr)
        seq.append(curr)
    if len(q) == 0:
        break
    if max(q) < curr:
        direction = -1
    if min(q) > curr:
        direction = 1
print "d. LOOK:", total, seq
 
 
# C-SCAN
q = copy.copy(queue)
total = 0
curr = q.pop(0)
seq = [curr]
while len(q)>0:
    curr += 1
    total += 1
    if curr in q:
        q.remove(curr)
        seq.append(curr)
    if curr == 4999:
        curr = 0
        total += 4999
print "e. C-SCAN:", total, seq
 
 
# C-LOOK
q = copy.copy(queue)
total = 0
curr = q.pop(0)
seq = [curr]
while len(q)>0:
    curr += 1
    total += 1
    if curr in q:
        q.remove(curr)
        seq.append(curr)
    if len(q) == 0:
        break
    if max(q) < curr:
        tmp = curr
        curr = min(q) -1
        total += abs(tmp - curr) -2
print "f. C-LOOK:", total, seq
 
 
# Prints:
# a. FCFS: 7081
# b. SSTF: 1745 [143, 130, 86, 913, 948, 1022, 1470, 1509, 1750, 1774]
# c. SCAN: 9769 [143, 913, 948, 1022, 1470, 1509, 1750, 1774, 130, 86]
# d. LOOK: 3319 [143, 913, 948, 1022, 1470, 1509, 1750, 1774, 130, 86]
# e. C-SCAN: 9985 [143, 913, 948, 1022, 1470, 1509, 1750, 1774, 86, 130]
# f. C-LOOK: 3363 [143, 913, 948, 1022, 1470, 1509, 1750, 1774, 86, 130]
