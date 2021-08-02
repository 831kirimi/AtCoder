#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  NM = list(map(int, input().split()))
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))
  N = NM[0]
  M = NM[1]
  ans = min(abs(A[0]-B[0]),abs(A[0]-B[M-1]),abs(A[N-1]-B[0]),abs(A[N-1]-B[M-1]))
  for i in range(N):
    for j in range(ans):
      if (A[i] + j) in B:
        ans = min(ans,j)
      elif (A[i] - j) in B:
        ans = min(ans,j)
  print(ans)

if(__name__ == '__main__'):
  main()
