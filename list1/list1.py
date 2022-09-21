def first_last6(nums):
  return(nums[0] == 6 or nums[-1] == 6)

def same_first_last(nums):
  return(len(nums) >= 1 and (nums[0] == nums[-1]))

def make_pi():
  piList = [3, 1, 4]
  return piList

def common_end(a, b):
  return(a[0] == b[0] or a[-1] == b[-1])

def sum3(nums):
  sum = 0
  for x in nums:
    sum += x
  return sum

