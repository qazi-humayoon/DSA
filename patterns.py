n = 4     
for i in range(n):
    for j in range(n):
        print("*",end="") #end causes new line to print in the same line
    print()

#   O/P
#         ****
#         ****
#         ****
#         ****

n = 6
for i in range(n):
    for j in range(i):
        print("*",end="")
    print()

#   O/P
#         *
#         **
#         ***
#         ****
#         *****

n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#   O/p
#            1
#            1 2
#            1 2 3
#            1 2 3 4
#            1 2 3 4 5

n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

#   O/P

#           1
#           2 2
#           3 3 3
#           4 4 4 4
#           5 5 5 5 5

n = 5
for i in range(1,n+1):
    for j in range(n-i+1):
        print("*",end=" ")
    print()

#   O/P
#           *****
#           ****
#           ***
#           **
#           *

n = 5
for i in range(1,n+1):
    for j in range(1,(n - i + 1)+1):
        print(j,end=" ")
    print()

# O/P
#           1 2 3 4 5
#           1 2 3 4
#           1 2 3
#           1 2 
#           1
        
n = 5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    for l in range(n-i-1):
            print(" ",end="")
                
    print()

# O/P
#       *    
#      ***   
#     *****
#    *******
#   *********


n = 5
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range((2*n)-(2*i+1)):
        print("*",end="")
    for l in range(i):
        print(" ",end="")
                
    print()


#   O/P
#      *********
#       *******
#        *****
#         ***
#          *

n = 5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    for l in range(n-i-1):
            print(" ",end="")
                
    print()
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range((2*n)-(2*i+1)):
        print("*",end="")
    for l in range(i):
        print(" ",end="")
                
    print()

# O/P

#          *    
#         ***   
#        *****
#       *******
#      *********
#      *********
#       *******
#        *****
#         ***
#          *

n = 5
for i in range(n+1):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(n-i-1):
        print("*",end=" ")
    print()

#   O/P
#       * 
#       * * 
#       * * * 
#       * * * * 
#       * * * * * 
#       * * * * 
#       * * * 
#       * * 
#       *
