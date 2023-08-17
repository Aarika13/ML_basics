# from math import sqrt
# r = int(input("Enter the number:"))
# def fun(r):
#     while (r<r+5) :
#         if (math.sqrt(r)== int(math.sqrt(r))):
#             print(r,end = " ")
            
# # fun(r)
# r = int(input("Enter the number:"))
# def fun(r):
#     while (r>r+5) :
#         if (r**(0.5)== int(r**(0.5))):
#             print(r,end = " ")
#     # break
            
# fun(r)
# S=[]
# top=None
# def isEmpty(stk):
#     if stk==[]:
#         return True
#     else:
#         return False

# def push(stk,item):
#     stk.append(item)
#     top = len(stk) - 1
    
# def s_pop(stk):
#     if isEmpty(stk):
#         return('Underflow')
#     else:
#         i = stk.pop()
#         if (len(stk)==0):
#             top=0
#         else:
#             top = top-1
#     return i

# def peek(stk):
#     if isEmpty(stk):
#         return('Underflow')
#     else:
#         top = len(stk) - 1
#         return stk[top]
    
# def display(stk):
#     if isEmpty(stk):
#         print("Stack is empty")
#     else:
#         top = len(stk) - 1
#         print(stk[top],'<----top')
#         for i in range(top-1,-1,-1):
#             print(stk[i])
            
# while True:
#     print("Stack Implementation")
#     print("1. Push ")
#     print("2. Pop ")
#     print("3. Peek ")
#     print("4. Display ")
#     print("5. Exit")
    
#     ch = int(input("Enter the choice(1-5): "))
#     if(ch==1):
#         item = int(input("Enter the item you want to push: "))
#         push(S,item)
#         print('%d item added successfully'%item)
#         input("Press any key to continue..")
        
#     elif(ch==2):
#         item = s_pop(S)
#         if (item=='Underflow'):
#             print("Stack is empty")
#         else:
#             print('%d item popped successfully'%item)
#         input("Press any key to continue..")
       
#     elif ch==3:
#         item = peek(S)
#         if (item=='Underflow'):
#             print("Stack is empty")
#         else:
#             print('%d is at the top successfully'%item)
#         input("Press any key to continue..")
        
#     elif ch==4:
#         display(S)
#         input("Press any key to continue..")
        
#     elif ch==5:
#         print("You are exit now")
#         break
#     else:
#         print("Nothing can de done")
#         input("press any key to continue")

# def find_consecutive(N):
#     start = 1
#     end = (N+1)//2
#     while start < end:
#         sum = 0
#         for i in range(start,end+1):
#             sum = sum + i
#             if(sum==end):
#                 for j in range(start,i+1):
#                     print(j,end=" ")
                    
#             if(sum>N):
#                 break
#         sum = 0
#         start += 1
        
# N = int(input("Enter the number: "))
# find_consecutive(N)

# def findConsecutive(N):
 
#     start = 1
#     end = 1
#     sum = 1
     
#     while start <= N/2:
         
#         if sum < N:
#             end += 1
#             sum += end
         
#         if sum > N:
#             sum -= start
#             start += 1
             
#         if sum == N:
             
#             for i in range(start, end + 1):
#                 print(i, "+",end=' ')
#             print( )
#             sum -= start
#             start += 1
 
# N = int(input("Enter the number:"))
# findConsecutive(N)

# def fn(n):
#     for x in range(0,n):
#         for y in range(n-1,x,-1):
#             print(" ",end="")
#         for z in range(x,-(x+1),-1):
#             print(chr(x-abs(z)+65),end="")
#         print("")
        
# n = int(input("Enter the no. of rows"))
# fn(n)
#C pattern 
# def c_fun(n):
#     for x in range(1,n):
#         for y in range(1,n+1):
#             if x==1 or x==n or y==1:
#                 print(n,end="")
#         print()
        
# n = int(input("enter the no. of row:"))
# c_fun(n)
# rows = 5
# for i in range(0, rows + 1, -1):
#     for j in range(i + 1, rows + 1, 1):
#         print(j, end=' ')
#     print()
import matplotlib