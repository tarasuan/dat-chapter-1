def is_divisible_by33():
  bucket = range(1,1000)
  results = []
  for i in bucket:
    if i % 33 == 0:
      results.append(i)
  print results

is_divisible_by33()