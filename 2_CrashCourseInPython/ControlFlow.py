if 1 >2 :
  message ="if only 1 were greater than two..."
elif 1>3:
  message = "elif stands for else if"
else:
  message = "When all else fails use lse(if you want to)"


x=0
parity = "even" if x%2 == 0 else "odd"

while x <10:
  print(f"{x} is less than 10")
  x +=1

for x in range(10):
  print(f"{x} is less than 10")

for x in range(10):
  if x==3:
    continue
  if x == 5:
    break