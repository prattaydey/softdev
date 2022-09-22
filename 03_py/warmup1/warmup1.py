# sleep in 
#--------------------------------------------------------
# The parameter weekday is True if it is a weekday, and the parameter vacation is #True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
#--------------------------------------------------------
def sleep_in(weekday, vacation):
  return (not weekday or vacation)

print(sleep_in(False, False)) 
print(sleep_in(True, False)) 
print(sleep_in(False, True)) 

#monkey trouble
#--------------------------------------------------------
#We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
#--------------------------------------------------------
def monkey_trouble(a_smile, b_smile):
  return (a_smile and b_smile or not a_smile and not b_smile)

print(monkey_trouble(True, True)) 
print(monkey_trouble(False, False)) 
print(monkey_trouble(True, False)) 

# sum double 
#--------------------------------------------------------
#Given two int values, return their sum. Unless the two values are the same, then return double their sum.
#--------------------------------------------------------
def sum_double(a, b):
  if a == b:
    return ((a+b)*2)
  else:
    return (a+b)
 
print(sum_double(1, 2)) 
print(sum_double(3, 2)) 
print(sum_double(2, 2)) 

# diff21 
#--------------------------------------------------------
#Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
#--------------------------------------------------------
def diff21(n):
  if n <= 21:
    return (abs(21-n))
  else:
    return (abs(21-n)*2)
  
print(diff21(19)) 
print(diff21(10)) 
print(diff21(21)) 

# parrot trouble 
#--------------------------------------------------------
#We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
#--------------------------------------------------------
def parrot_trouble(talking, hour):
  if (talking == True) and (hour < 7 or hour > 20):
    return True
  else:
    return False

print(parrot_trouble(True, 6)) 
print(parrot_trouble(True, 7)) 
print(parrot_trouble(False, 6)) 

#makes 10
#--------------------------------------------------------
#Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
#--------------------------------------------------------
def makes10(a, b):
  if (a == 10 or b == 10) or (a+b==10):
    return (True)
  else:
    return (False) 

print(makes10(9, 10)) 
print(makes10(9, 9)) 
print(makes10(1, 9)) 

# near hundred 
#--------------------------------------------------------
#Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
#--------------------------------------------------------
def near_hundred(n):
  return (abs(n-100)<=10) or (abs(n-200)<=10)

print(near_hundred(93)) 
print(near_hundred(90)) 
print(near_hundred(89)) 

# pos neg
#--------------------------------------------------------
#Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.
#--------------------------------------------------------
def pos_neg(a, b, negative):
  if (negative == False):
    return (a < 1 and b> 0) or (b < 1 and a > 0)
  if negative ==True:
    return (a < 1 and b < 1)

print(pos_neg(1, -1, False)) 
print(pos_neg(-1, 1, False)) 
print(pos_neg(-4, -5, True)) 

# not string
#--------------------------------------------------------
#Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.
#--------------------------------------------------------
def not_string(str):
  if len(str) >= 3:
    if(str[0:4] == "not "):
      return str
    else:
      return "not " + str
  return "not " + str

print(not_string('candy')) 
print(not_string('x'))
print(not_string('not bad')) 

# missing char 
#--------------------------------------------------------
#Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
#--------------------------------------------------------
def missing_char(str, n):
  return str[0:n] + str[n+1:len(str)]

print(missing_char('kitten', 1))
print(missing_char('kitten', 0))
print(missing_char('kitten', 4)) 

# front back 
#--------------------------------------------------------
#Given a string, return a new string where the first and last chars have been exchanged.
#--------------------------------------------------------
def front_back(str):
  if(len(str) > 1): 
    return str[len(str)-1] + str[1:len(str)-1] + str[0]
  else: 
    return str

print(front_back('code')) 
print(front_back('a')) 
print(front_back('ab'))

# front3
#--------------------------------------------------------
#Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
#--------------------------------------------------------
def front3(str):
  if len(str) > 2:
    return 3 * str[0:3]
  else:
    return str * 3

print(front3('Java')) 
print(front3('Chocolate'))
print(front3('abc')) 
