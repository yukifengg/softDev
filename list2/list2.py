def count_evens(nums):
  sum = 0
  for x in nums:
    if x % 2 == 0:
      sum += 1
  return sum

def big_diff(nums):
  return max(nums) - min(nums)

def centered_average(nums):
  nums.remove(min(nums))
  nums.remove(max(nums))
  sum = 0
  for x in nums:
    sum += x
  return sum / len(nums)

