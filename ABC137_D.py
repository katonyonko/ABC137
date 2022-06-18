import io
import sys

_INPUT = """\
6
3 4
4 3
4 1
2 2
5 3
1 2
1 3
1 4
2 1
2 3
1 1
2 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from heapq import heappop,heappush
  N,M=map(int,input().split())
  work=[list(map(int,input().split())) for _ in range(N)]
  work.sort(reverse=True)
  ans=0
  cur=-1
  h=[]
  for i in reversed(range(M)):
    while cur>=-N and i+work[cur][0]<=M:
      heappush(h,[-work[cur][1],work[cur][0]])
      cur-=1
    if len(h)>0:
      x,y=heappop(h)
      if i+y<=M:
        ans+=-x
    # print(__,i,h,ans)
  print(ans)