def fib_even(x, y):
  list = [x,y]
  sum_even = 0
  sum_all = 0
  n = 0

  while n < 3524578:
    i = list[(len(list)-1)] + list[(len(list)-2)]
    list.append(i)
    n = max(list)

  for z in list:
    if z % 2 == 0:
      sum_even += z

  print list
  print sum_even

fib_even(1,2)