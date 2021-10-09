#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  LQ = list(map(int, input().split()))
  L = LQ[0]
  Q = LQ[1]
  cx = [[0]*2 for i in range(Q)]
  for i in range(Q):
    cx[i] = list(map(int, input().split()))

  cut = [0,L]
  for i in range(Q):
    if cx[i][0] == 1:
      cut.append(cx[i][1])
    else:
      cut.sort()
      for j in range(len(cut)):
        if cut[j] > cx[i][1]:
          print(cut[j] - cut[j-1])
          break

if(__name__ == '__main__'):
  main()
