mport sys

n = int(raw_input().strip())
a = []
a_d1,a_d2=0,0
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
for i in xrange(n):
    a_d1+=a[i][i]
    a_d2+=a[i][n-i-1]
print abs(a_d1-a_d2)

