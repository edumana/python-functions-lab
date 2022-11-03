
#----------------- 1 ----------------- 
n = int(input('Sum to n: '))

def sum_to(n):
  if n == 0:
    return 0
  return n + sum_to(n-1)

print(sum_to(n))

#----------------- 2 ----------------- 
def largest(x):
  max = x[0]
  for i in x:
    if i > max:
      max = i

  return max

x = [4,5,600,7,8,1,100,1,3]
print(largest(x))

#----------------- 3 ----------------- 

str1 = input('String 1: ')
str2 = input('String 2: ')

def occurrences(str1, str2):
  return str1.count(str2)

#----------------- 4 ----------------- 

def product(*args):
  product = 1
  for i in args:
    product *= args
  return product
