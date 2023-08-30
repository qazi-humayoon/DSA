# Pass by Value
def modify_value(x):
    x = x + 10
    print("Inside the function:", x)

value = 5
modify_value(value)
print("Outside the function:", value)

# Pass by Reference
def modify_list(lst):
    lst.append(10)
    print("Inside the function:", lst)

my_list = [1, 2, 3]
modify_list(my_list)
print("Outside the function:", my_list)
