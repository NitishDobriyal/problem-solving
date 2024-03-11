from collections import deque
n=8
set={2,3}
print

q1 =  deque()
q1.append(2)
q1.append(3)

for i in range(n):
    s=str(q1.popleft())
    print(s)
    
    q1.append(s+'2')
    q1.append(s+'3')