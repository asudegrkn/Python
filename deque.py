# deque 

from collections import deque
dq = deque(maxlen = 3 )

dq.append(1)  #1 ekle sonuna 
print(dq)

dq.append(2)  #2 ekle sonuna 
print(dq)

dq.append(3)  #3 ekle sonuna 
print(dq)

dq.append(4)  #4 ekle sonuna [2,3,4]
print(dq)


dq = deque(maxlen = 3 )
dq.append(1)  #1 ekle sonuna 
print(dq)

dq.append(2)  #2 ekle sonuna 
print(dq)


dq.appendleft(3)  #3 ekle başına 
print(dq)


dq.clear()
print(dq)