def double(x):
  """
  This is where you put an optional docstring that explains
  what function does .For example this function multiplies its input by 2  
  """
  return x *2

def apply_to_one(f):
  """Calls the function f with 1 as its argument"""
  return f(1)

my_double = double
x= apply_to_one(my_double)
print(x)

y = apply_to_one(lambda x:x+4) #equals 5
another_double = lambda  x: 2*x 

def another_double(x):
  """Do this instead"""
  return 2 * x

def my_print(message="my default message"):
  print(message)

my_print("hello")
my_print()

def full_name(first = "What's his name",last = "something"):
  return first + " " + last

full_name('Joel','Grus')
full_name("Joel")
print(full_name(last="Grus"))