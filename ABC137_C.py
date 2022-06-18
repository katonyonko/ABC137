import io
import sys

_INPUT = """\
6
3
acornistnt
peanutbomb
constraint
2
oneplustwo
ninemodsix
5
abaaaaaaaa
oneplustwo
aaaaaaaaba
twoplusone
aaaabaaaaa
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  ans={}
  N=int(input())
  for i in range(N):
    tmp=[0]*26
    s=input()
    for j in range(10):
      tmp[ord(s[j])-ord('a')]+=1
    tmp=tuple(tmp)
    if tmp in ans:
      ans[tmp]+=1
    else:
      ans[tmp]=1
  ans2=0
  for x in ans:
    ans2+=ans[x]*(ans[x]-1)//2
  print(ans2)