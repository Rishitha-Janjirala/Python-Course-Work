# #1.butterfly
# # *           * 
# # * *       * * 
# # *   *   *   * 
# # *     *     * 
# # *   *   *   * 
# # * *       * * 
# # *           * 

# n=7
# for i in range(n):
#     for j in range(n):
#         if j==0 or j==n-1 or i==j or i+j==n-1:
#             print("*",end=' ')
#         else:
#             print(' ',end=" ")
        
#     print()

# #2.Square
# # * * * * * 
# # *       * 
# # *       * 
# # *       * 
# # * * * * * 
# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or  j==0 or i==n-1 or j==n-1:
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     print()

# #3.rectangle
# # * * * * * * * 
# # *           * 
# # * * * * * * * 
# r=3
# c=7

# for i in range(r):
#     for j in range(c):
#         if i==0 or j==0 or i==r-1 or j==c-1:
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     print()

# # 4.Hollow right triangle
# n=5
# for i in range(n):
#     for j in range(n):
#         if j==0 or i==n-1 or i==j:
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     print()

# #5.Hollow inverted right triangle
# # * * * * * 
# # *     *   
# # *   *     
# # * *       
# # *  
# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i+j==n-1:
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     print()

#6.Hollow pyramid
#     *
#    * *
#   *   *
#  *     *
# * * * * *
n=5
for i in range(n):
    for k in range(n-i-1):
        print(' ',end='')
    for j in range(i+1):
        if j==0 or i==j or i==n-1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print() 

# 7.Hollow inverted pyramid
n=5
for i in range(n):
    for k in range(i):
        print(' ',end='')
    for j in range(n-i):
        if i==0 or j==0 or i+j==n-1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print() 