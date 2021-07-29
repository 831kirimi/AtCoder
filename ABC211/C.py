#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  S = str(input()) 
  c = []
  h = []
  o = []
  k = []
  u = []
  d = []
  a = []
  i = []
  for j in range(len(S)):
    if S[j] == 'c':
      c.append(j)
    elif S[j] == 'h':
      h.append(j)
    elif S[j] == 'o':
      o.append(j)
    elif S[j] == 'k':
      k.append(j)
    elif S[j] == 'u':
      u.append(j)
    elif S[j] == 'd':
      d.append(j)
    elif S[j] == 'a':
      a.append(j)
    elif S[j] == 'i':
      i.append(j)
  C = []
  C.append(c)
  C.append(h)
  C.append(o)
  C.append(k)
  C.append(u)
  C.append(d)
  C.append(a)
  C.append(i)
#  print(C)
  count = 0
  for i in range(len(C[0])):
    for j in range(len(C[1])):
      for k in range(len(C[2])):
        for l in range(len(C[3])):
          for m in range(len(C[4])):
            for n in range(len(C[5])):
              for o in range(len(C[6])):
                for p in range(len(C[7])):
                  if C[0][i] < C[1][j] and C[1][j] < C[2][k] and C[2][k] < C[3][l] and C[3][l] < C[4][m] and C[4][m] < C[5][n] and C[5][n] < C[6][o] and C[6][o] < C[7][p]:
                    count += 1 % (1000000007)


  print(count)
if(__name__ == '__main__'):
  main()
