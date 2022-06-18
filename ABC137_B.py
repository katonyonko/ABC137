import io
import sys

_INPUT = """\
6
3 7
4 0
1 100
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  K,X=map(int,input().split())
  for i in range(-(10**6),10**6+1):
    if abs(i-X)<K:
      print(i,end=' ')