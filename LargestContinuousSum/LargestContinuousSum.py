def large_cont_sum(arr):
  """
  Finds the largest continuous sum of number in an iterable.

  Args:
  arr1: (list) a series of numbers.

  Returns:
  (int) Largest continuous sum of numbers found.
  """
  if len(arr) == 0:
    return 0
  largest = arr[0]
  res = largest
  for num in arr[1:]:
    if num < res * -2:
      return largest
    else:
      res += num
      if res > largest:
        largest = res
  return largest