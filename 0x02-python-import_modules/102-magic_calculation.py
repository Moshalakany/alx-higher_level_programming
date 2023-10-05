#!/usr/bin/python3
def magic_calculation(a, b):
  add = magic_calculation_102.add
  sub = magic_calculation_102.sub
  if a < b:
    c = add(a, b)
  else:
    c = sub(a, b)
  for i in range(4, 6):
    c = add(c, i)
  return c
