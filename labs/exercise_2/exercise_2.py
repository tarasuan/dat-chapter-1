def fib_even(x, y):
  list = [x,y]
  n = 0
  sum_even = 0

  while n < 3524578:
    i = list[(len(list)-1)] + list[(len(list)-2)]
    list.append(i)
    n = max(list)

  for n in list:
    if n % 2 == 0:
      sum_even += n

  print list
  print n
  print sum_even

fib_even(1,2)