import io
import sys

_INPUT = """\
6
-13 3
1 -33
13 3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  A,B=map(int,input().split())
  print(max(A+B,A-B,A*B))