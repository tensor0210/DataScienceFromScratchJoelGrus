integer_list =[1,2,3]
hetrogeneous_list =["string",0.1,True]
list_of_list = [integer_list,hetrogeneous_list,[]]
list_length = len(integer_list)
list_length = sum(integer_list)

print(f"{list_length} {list_length}")
x =[0,1,2,3,4,5,6,7,8,9]
zero = x[0]
one =x[1]
nine = x[-1]
eight = x[-2]
x[0] = -1

first_three = x[:3]
three_to_end = x[3:]
one_to_four = x[1:5]
last_three = x[-3:]
without_first_and_last = x[1:-1]
copy_of_x =x[:]

every_third =x[::3]
five_to_three = x[5:2:-1]

c1 = 1 in [1,2,3]
c2 = 0 in [1,2,3]

x=[1,2,3]
x.extend([4,5,6]) #Changes X 

x=[1,2,3]
y = x + [4,5,6] #Changes Y

x =[1,2,3]
x.append(0)
y=x[-1]
z=len(x)
x,y=[1,2]
_,y =[1,2]