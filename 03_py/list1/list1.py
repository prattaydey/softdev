# first last6
#--------------------------------------------------------
#Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.
#--------------------------------------------------------
def first_last6(nums):
  return nums[0] == 6 or nums[len(nums)-1] == 6

print(first_last6([1, 2, 6]))
print(first_last6([6, 1, 2, 3]))
print(first_last6([13, 6, 1, 2, 3]))

# same first last
#--------------------------------------------------------
#Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.
#--------------------------------------------------------
def same_first_last(nums):
  return len(nums) >= 1 and nums[0] == nums[len(nums)-1] 

print(same_first_last([1, 2, 3]))
print(same_first_last([1, 2, 3, 1]))
print(same_first_last([1, 2, 1]))

# make pi
#--------------------------------------------------------
#Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
#--------------------------------------------------------
def make_pi():
  pi = [3, 1, 4] 
  return pi 

print(make_pi())

# common end 
#--------------------------------------------------------
#Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.
#--------------------------------------------------------
def common_end(a, b):
  return a[0] == b[0] or a[len(a)-1] == b[len(b)-1] 

print(common_end([1, 2, 3], [7, 3]))
print(common_end([1, 2, 3], [7, 3, 2]))
print(common_end([1, 2, 3], [1, 3]))

# sum3
#--------------------------------------------------------
#Given an array of ints length 3, return the sum of all the elements.
#--------------------------------------------------------
def sum3(nums):
  sum = 0
  for x in nums: 
    sum += x
  return sum 

print(sum3([1, 2, 3]))
print(sum3([5, 11, 2]))
print(sum3([7, 0, 0]))

#rotate left3
#--------------------------------------------------------
#Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
#--------------------------------------------------------
def rotate_left3(nums):
  result = [ nums[1], nums[2], nums[0]]
  return result
 
print(rotate_left3([1, 2, 3]))
print(rotate_left3([5, 11, 9]))
print(rotate_left3([7, 0, 0]))

 # reverse 3
#--------------------------------------------------------
#Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.
#--------------------------------------------------------
def reverse3(nums):
  result = [ nums[2], nums[1], nums[0]]
  return result

print(reverse3([1, 2, 3]))
print(reverse3([5, 11, 9]))
print(reverse3([7, 0, 0]))

# max end3
#--------------------------------------------------------
#Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.
#--------------------------------------------------------
def max_end3(nums):
  counter = 0
  largest = 0
  if nums[0] > nums[len(nums)-1]: 
    largest = nums[0]
  else: 
    largest = nums[len(nums)-1]
   # replace !
   return [largest,largest,largest] 

print(max_end3([1, 2, 3]))
print(max_end3([11, 5, 9]))
print(max_end3([2, 11, 3]))

 # sum2
#--------------------------------------------------------
#Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.
#--------------------------------------------------------
def sum2(nums):
  counter = 0
  sum = 0
  if len(nums) == 0:
    return 0
  else: 
    if len(nums) < 2: 
      for x in nums: 
        sum += x
    else: 
      sum = sum + nums[0] + nums[1] 
  return sum 

print(sum2([1, 2, 3]))
print(sum2([1, 1]))
print(sum2([1, 1, 1, 1]))

#middle way
#--------------------------------------------------------
#Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
#--------------------------------------------------------
def middle_way(a, b):
  middle = [ a[1], b[1]]
  return middle

print(middle_way([1, 2, 3], [4, 5, 6]))
print(middle_way([7, 7, 7], [3, 8, 0]))
print(middle_way([5, 2, 9], [1, 4, 5]))

#make ends 
#--------------------------------------------------------
#Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.
#--------------------------------------------------------
def make_ends(nums):
  ends = [nums[0], nums[len(nums)-1]] 
  return ends

print(make_ends([1, 2, 3]))
print(make_ends([1, 2, 3, 4]))
print(make_ends([7, 4, 6, 2]))

# has23
#--------------------------------------------------------
#Given an int array length 2, return True if it contains a 2 or a 3.
#--------------------------------------------------------
def has23(nums):
  return (nums[0] == 2 or nums[0] == 3) or (nums[1] == 2 or nums[1] == 3)

print(has23([2, 5]))
print(has23([4, 3]))
print(has23([4, 5]))
