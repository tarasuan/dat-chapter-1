def is_divisible_by33():
  bucket = range(1,1000)
  results = []
  for i in bucket:
    if i % 33 == 0:
      results.append(i)
  print results

  try:
    for i in results:
      i%33 == 0
    print "All checked out."
  except ValueError:
    print "Oops, %s is not divisible by 33. Must be a bug!" % i

is_divisible_by33()