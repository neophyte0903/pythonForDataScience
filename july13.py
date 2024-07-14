# for i in range(5):
#     print("Hello")


# for i in range(5):
#     print(i+1)

# print("python")


# ls=[1,2,3,4,5]

# for i in ls:
#     x=i+2
#     print(x)

# print(ls)

ls=[2,5,4,8,1,6,9]

# for i in ls:
#     if(i%2==0):
#         print("even")
#     else:
#         continue;

# sum=0
# for i in ls:
#     sum+=i

# print(sum)

# #inplace approach 

# s=ls[0]

# for i in range (1,len(ls)):
#     s=s+ls[i]

# print(s)

#odd sum 
s=0

for i in ls:
    if(i%2!=0):
        s=s+i
    else:
        continue

print(s)

#prime number


# if (n==0 or n==1):
#     print("not prime")

# count=0
# for i in range(1,n+1):
#     if(n%i==0):
#         count+=1

# if count==2:
#     print("prime")
# else:
#     print("not prime")

#primeNo in List brute force approach
#nested for loop

# for i in ls:
#     count=0
#     for j in range(1,i+1):
#         if(i%j==0):
#             count+=1

#     if(count==2):
#         print("prime")
#     else:
#         print("not prime")

# print (ls)





#list sepration
# o=[]
# e=[]
# esum=0
# osum=0
# for i in ls:
#     if(i%2==0):
#         e.append(i)
#         esum+=i
#     else:
#         o.append(i)
#         osum+=i

# print(e)
# print(o)
# print(esum,osum)
fact=1
for i in range(5,0,-1):
    fact=fact*i

print(fact)

