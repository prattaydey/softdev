# count evens 
#--------------------------------------------------------
#Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
#--------------------------------------------------------
def count_evens(nums):
  counter = 0; 
  index = 0; 
  while index < len(nums): 
    if nums[index] % 2 == 0:
      counter += 1
      index += 1
    else: 
      index += 1
  return counter

print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5])) 

#big diff 
#--------------------------------------------------------
#Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array.
#--------------------------------------------------------

def big_diff(nums):
  minVal = nums[0]
  maxVal = 0
  counter = 0
  while counter < len(nums):
    if ( nums[counter] < minVal ):
      minVal = nums[counter]
    elif ( nums[counter] > maxVal ):
      maxVal = nums[counter]
    counter += 1
  return maxVal - minVal

print(big_diff([10, 3, 5, 6])) 
print(big_diff([7, 2, 10, 9])) 
print(big_diff([2, 10, 7, 2]))

# centered average
#--------------------------------------------------------
#Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.
#--------------------------------------------------------

def centered_average(nums):
  minVal = nums[0]
  maxVal = 0
  counter = 0
  sum = 0
  while counter < len(nums):
    sum += nums[counter]
    if ( nums[counter] < minVal ):
      minVal = nums[counter]
    elif ( nums[counter] > maxVal ):
      maxVal = nums[counter]
    counter += 1
  return (sum - minVal - maxVal) / (len(nums) - 2)

print(centered_average([1, 2, 3, 4, 100])) 
print(centered_average([1, 1, 5, 5, 10, 8, 7])) 
print(centered_average([-10, -4, -2, -4, -2, 0])) 

#sum13
#--------------------------------------------------------
#Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
#--------------------------------------------------------

def sum13(nums):
  counter = 0;
  sum = 0;
  while ( counter < len(nums) ):
    if (nums[counter] != 13):
      sum += nums[counter]
    else:
      if ( counter != len(nums) - 1 ):
        counter += 1
    counter += 1;
  return sum

print(sum13([1, 2, 2, 1]))
print(sum13([1, 1])) 
print(sum13([1, 2, 2, 1, 13])) 

#has22
#--------------------------------------------------------
#Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
#--------------------------------------------------------

def has22(nums):
  isValid = False
  counter = 0
  while counter < len(nums) - 1:
    if ( nums[counter] != 2 ):
      counter += 1
    else:
      if ( nums[counter + 1] == 2 ):
        isValid = True
      counter += 1
  return isValid

print(has22([1, 2, 2])) 
print(has22([1, 2, 1, 2])) 
print(has22([2, 1, 2])) 

# sum 67 
#--------------------------------------------------------
#Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
#--------------------------------------------------------
def sum67(nums):
  total = 0
  #counter
  i = 0
  while i < len(nums):
    # if number not 6, add to total
    if nums[i] != 6:
      total += nums[i]
      i += 1
    # if number is 6
    else:
      # ignore it
      i += 1
      # keep ignoring numbers until u get to 7
      while nums[i] != 7:
        i += 1
      # ignore the 7
      i += 1
  return total

print(sum67([1, 2, 2]))
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 1, 6, 7, 2])) 

