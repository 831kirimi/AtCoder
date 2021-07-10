#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  import numpy
  N = int(input()) 
  C = list(map(int, input().split()))
  C.sort()
  sum = 1
  for i in range(N):
    sum *= C[i] - i
  print(sum % (10**9+7))
  

if(__name__ == '__main__'):
  main()
