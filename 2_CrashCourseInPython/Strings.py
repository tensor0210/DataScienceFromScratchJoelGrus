single_quoted_string = 'data science'
double_quoted_string = "data science"

tab_string ="\t"
print(len(tab_string))

multi_line_string = """
This is the first line and this is the second line
and this is third line 
"""

print(multi_line_string)
first_name ="Joel"
last_name ="Grus"

full_name1 = first_name + " " + last_name #string addition
full_name2 = "{0} {1}".format(first_name,last_name) #string format
full_name3 = f"{first_name} {last_name}"
print(full_name3)