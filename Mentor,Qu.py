# Max and Min---
# a=[4,5,6,7,8,9]
# i=0
# max=0
# min=a[0]
# while i<len(a):
#     if a[i]>max:
#          max=max+(a[i])
#     if a[i]<min:
#         min=min+(a[i])
#     i=i+1
# print(max)
# print(min)

# Add str value in list---
# a="223456"
# i=0
# sum=0
# while i<len(a):
#     sum+=int(a[i])
#     i+=1
# print(sum)

# Sum of List---  
# marks=[4,5,[6,7],8,2,[3,1],2]
# i=0
# sum=0
# while i<len(marks):
#     if type(marks[i])==list:
#         j=0
#         while j<len(marks[i]):
#             sum= sum+(marks[i][j])
#             j=j+1
#     else:
#         sum=sum+marks[i]
#     i=i+1
# print(sum) 
 
# Sum of List--
# a=["123","456","789"]
# i=0
# total=0
# while i<len(a):
#     sum=0
#     j=0
#     while j<3:
#         total=total+int(a[i][j])
#         sum=sum+int(a[i][j])
#         j=j+1
#     print(sum)
#     i+=1
# print(total)

# Removed same no and add different in list---
# a=int(input("enter the number : "))
# n=[4,6,3,4,5,6]
# i=0
# list1=[]
# while i<len(n):
#     if n[i] not in list1:
#         list1.append(n[i])
#     i=i+1
# print(list1)
# if a not in list1:
#     list1.append(a)
#     print(list1)

# Add "0" in the end of the list---
# a=[4,5,6,0,0,9,0,3]
# i=0
# s=[]
# b=[]
# while i<len(a):
#     if a[i]!=0:
#         s.append(a[i])
#     else:
#         b.append(a[i])
#     i=i+1
# print(s+b)

# Without used of slicing,for loop Rversed list---
# a=[9,3,6,4,7,2,1]
# i=0
# b=[]
# k=-1
# while i<len(a):
#     b.append(a[k])
#     k=k-1
#     i=i+1
# print(b)

# Get only alphabet in string---
# a=["4ef","6gh3","12ab"]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     n=a[i]
#     s=""
#     while j<len(n):
#         if n[j]>="a" and n[j]<="z":
#             s=s+n[j]
#         j=j+1
#     b.append(s)
#     i=i+1
# print(b)

# Calculate max lenght of string in list---
# a=["aa","aaa","aaaa"]
# i=-1
# for x in a:
#     if len(x) >i:
#         i=len(x)
#         y=x
# print("Maximum length string is : ",y)

# Calculate max lenght of string in list---
# a=["aa","aaa","aaaa"]
# i=0
# max=0
# while i<len(a):
#     if len(a[i])>max:
#         max=len(a[i])
#         c=a[i]
#     i=i+1
# print(c,max)  

# Separate int and chara----
# a=["4efs","6gh3","12ab"]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if (a[i][j])>str(0) and (a[i][j])<=str(9):
#             b.append(int(a[i][j]))
#         else:
#             c.append(a[i][j])
#         j=j+1
#     i=i+1
# print(b)
# print(c)

# How many s and r in list---
# a=["shivani","rupa","shaina","samiksha","pooja"]
# i=0
# c=0
# d=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if (a[i][j])=="s":
#             c+=1
#         if (a[i][j])=="r":
#             d+=1  
#         j+=1
#     i+=1
# print("in list a 's' is",c,"time")
# print("in list a 'r' is",d,"time")

# Even indexing prints even tables---
# b=int(input("enter ther number : "))
# a=[1,15,3,47,5,90,7,34,9]
# i=0
# d=1
# while i<len(a):
#     if i%2==0:
#         c=d*b
#         del(a[i])
#         a.insert(i, c)
#         d+=1
#     i+=1
# print(a)

# Do sum and min in simple one list----
# a=[4,8,10,9,2,3,1]
# i=0
# sum=0
# min=a[3]
# while i<len(a):
#     if i<=2:
#         sum=sum+(a[i])
#     else:
#         if a[i]<min:
#             min=a[i]
#     i=i+1
# print(sum)
# print(min)

# a=[4,[6,9],3,[4,5],9]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             sum=sum+(a[i][j])
#             j=j+1
#     else:
#         sum=sum+(a[i])
#     i=i+1
# print(sum)

# a=["456","692","148","967"]
# i=0
# sum=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         sum=sum+int(a[i][j])
#         j=j+1
#     i=i+1
# print(sum)

# n=int(input("enter the number"))
# c=0
# a=[]
# b=[]
# i=1
# while i<(n):
#     if n%1==0:
#         a.append(n[i])
#         c=c+1
#     else:
#         b.append(n[i])
#     i=i+1
# if c==2:
#     print("prime number")
# else:
#     print("not prime number")

# a=["456","78","48"]
# i=0
# sum=0
# while i<len(a):
#     sum=sum+int(a[i])
#     i=i+1
# print(sum)

# a=["father","mom","sis"]
# b=[]
# i=0
# while i<len(a): 
#     c=a[i][::-1]
#     if a[i]==c:
#         b.append(a[i])
#     i=i+1
# print(b)

# a=[4,5,6,0,0,9,0,3]
# i=0
# s=[]
# b=[]
# while i<len(a):
#     if a[i]!=0:
#         s.append(a[i])
#     else:
#         b.append(a[i])
#     i=i+1
# print(s+b)


# a=["Roopa","Shaina","Riya"]
# i=0
# c=[]
# while i<len(a):
#     j=0
#     g=[]
#     while j<len(a[i]):
#         g.append(a[i][j])
#         j+=1
#     c.append(g)
#     i+=1
# print(c) 

# a=12
# b=67
# c=45
# if a>b and a>c:
#     print(a,"bigger")
# elif b>c and b>a:
#     print(b,"bigger")
# elif c>a and c<b:
#     print(c,"bigger")
# else:
#     print("not")

# a=[1,1,3,3,2,2,3,4,4,4]
# i=0
# b=[]
# c=[]
# d=[]
# e=[]
# while i<len(a):
#     if a[i]==1:
#         b.append(a[i])
#     if a[i]==2:
#         c.append(a[i])
#     if a[i]==3:
#         d.append(a[i])
#     if a[i]==4:
#         e.append(a[i])
#     i+=1
# print(b)
# print(c)
# print(d)
# print(e)

# a="my name is tanu"
# # ['my','name','is','tanu']
# b= []
# c=''
# for d in a:
#     if d== ' ':
#         b.append(c)
#         c=''
#     else:
#         c+=d
# if c:
#     b.append(c)

# print(b)















    






































