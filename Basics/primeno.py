import math
#Brute force Approach Time Complexity :- O(N)
# n = 8
# count = 0
# for i in range(2,n+1):
#     if n % i == 0:
#         count += 1
# if count== 2:
# print("prime")
# else:
#   print("not prime")

# Checking Prime no using functions
# def funcc(a):
#     count =  0
#     for i in range(1,n+1):
#         if a % i == 0:
#             count += 1
#     if count == 2:
#         return "Prime"
#     else:
#         return "Composite"
    
# n = 14
# result = funcc(n)
# print(result)



# # Optimized Approach Time Complexity :- O(sqrt(N))
n = 13
count = 0
for i in range(1,int(math.sqrt(n))+1):
    if n % i == 0:
        count += 1
    if (n / i) != i:
        count += 1
if count == 2:
    print("prime")
else:
    print("composite")

    #__________________________________________________________________
    
# First, we will take the input:  
lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
upper_value = int(input ("Please, Enter the Upper Range Value: "))  
  
print ("The Prime Numbers in the range are: ")  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  


