#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Counter
def main():
  NK = list(map(int, input().split()))
  c = list(map(int, input().split()))
  N = NK[0]
  K = NK[1]
  ans = []
  for i in range(N-K+1):
    ans.append(len(Counter(c[i:i+K])))
  print(max(ans))

if(__name__ == '__main__'):
  main()
