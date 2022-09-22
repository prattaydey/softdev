# string times 
#--------------------------------------------------------
#Given a string and a non-negative int n, return a larger string that is n copies of the original string.
#--------------------------------------------------------
def string_times(str, n):
  return n * str

print(string_times('Hi', 2)) 
print(string_times('Hi', 3))
print(string_times('Hi', 1)) 

# front times
#--------------------------------------------------------
#Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;
#--------------------------------------------------------
def front_times(str, n):
  if len(str) > 2:
    return n * str[0:3]
  else:
    return n * str
  
print(front_times('Chocolate', 2)) 
print(front_times('Chocolate', 3))
print(front_times('Abc', 3))

 # string bits
#--------------------------------------------------------
#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
#--------------------------------------------------------
def string_bits(str):
  final = ""
  increment = 0
  while increment < len(str): 
    final += str[increment] 
    increment += 2
  return final

print(string_bits('Hello')) 
print(string_bits('Hi'))
print(string_bits('Heeololeo'))

 # string splosion 
#--------------------------------------------------------
#Given a non-empty string like "Code" return a string like "CCoCodCode".
#--------------------------------------------------------
def string_splosion(str):
  result = "" 
  counter = 1
  while counter <= len(str): 
    result += str[0:counter] 
    counter += 1
  return result 

print(string_splosion('Code')) 
print(string_splosion('abc'))
print(string_splosion('ab'))

# last2
#--------------------------------------------------------
#Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
#--------------------------------------------------------
def last2(str):
  last2 = str[-2:] 
  counter = 0
  result = 0 
  while counter < len(str)-2: 
    if str[counter: counter + 2] == last2: 
      result += 1
    counter += 1
  return result

print(last2('hixxhi')) 
print(last2('xaxxaxaxx'))
print(last2('axxxaaxx'))

# array count9 
#--------------------------------------------------------
#Given an array of ints, return the number of 9's in the array.
#--------------------------------------------------------
def array_count9(nums):
  counter = 0
  for x in nums: 
    if x == 9: 
      counter += 1
  return counter

print(array_count9([1, 2, 9])) 
print(array_count9([1, 9, 9]))
print(array_count9([1, 9, 9, 3, 9]))

# array front9
#--------------------------------------------------------
#Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
#--------------------------------------------------------
def array_front9(nums):
  index = 0
  counter = 0
  if len(nums) >= 4: 
    while index <= 3: 
      if nums[index] == 9:
        counter += 1
        index += 1
      else: 
        index += 1
  else: 
    while index <= len(nums)-1: 
      if nums[index] == 9:
        counter += 1
        index += 1
      else: 
        index += 1
  # after both cases run 
  if counter != 0:
      return True
  else: 
      return False

print(array_front9([1, 2, 9, 3, 4])) 
print(array_front9([1, 2, 3, 4, 9]))
print(array_front9([1, 2, 3, 4, 5]))

# array123
#--------------------------------------------------------
#Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
#--------------------------------------------------------
def array123(nums):
  index = 0
  while index <= len(nums)-3: 
    if nums[index: index + 3] == [1,2,3]: 
      return True
    else: 
      index += 1
  return False

print(array123([1, 1, 2, 3, 1])) 
print(array123([1, 1, 2, 4, 1]))
print(array123([1, 1, 2, 1, 2, 3]))

# string match
#--------------------------------------------------------
#Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
#--------------------------------------------------------
def string_match(a, b):
  index = 0
  counter = 0
  while index <= len(a)-2: 
    if a[index:index+2] == b[index:index+2]: 
      counter += 1
      index += 1
    else: 
      index += 1
  return counter

print(string_match('xxcaazz', 'xxbaaz')) 
print(string_match('abc', 'abc'))
print(string_match('abc', 'axc'))
