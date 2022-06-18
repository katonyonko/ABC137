import io
import sys

_INPUT = """\
6
3 3 10
1 2 20
2 3 30
1 3 45
2 2 10
1 2 100
2 2 100
4 5 10
1 2 1
1 4 1
3 4 1
2 2 100
3 3 100
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M,P=map(int,input().split())
  G=[[] for _ in range(N)]
  R=[[] for _ in range(N)]
  for _ in range(M):
    A,B,C=list(map(int,input().split()))
    A-=1; B-=1
    G[A].append((P-C,B))
    R[B].append((P-C,A))
  #BellmanFord
  def BellmanFord(G,s=0):
    inf=10**20
    D=[inf]*len(G)
    D[s]=0
    for i in range(len(G)-1):
      for j in range(len(G)):
        for c,v in G[j]:
          if D[j]+c<D[v]:
            D[v]=D[j]+c
    cycle=[0]*len(G)
    for j in range(len(G)):
      for c,v in G[j]:
          if D[j]+c<D[v] and D[v]<inf//2: cycle[v]=1
    for i in range(len(G)-1):
      for j in range(len(G)):
        if cycle[j]==1:
          for c,v in G[j]:
            cycle[v]=1
    for i in range(len(G)):
      if cycle[i]==1: D[i]='-inf'
    return D
  D1, D2=BellmanFord(G,0), BellmanFord(R,N-1)
  if len(set([i for i in range(N) if D1[i]=='-inf'])&set([i for i in range(N) if D2[i]=='-inf']))>0: print(-1)
  else: print(max(0,-D1[-1]))