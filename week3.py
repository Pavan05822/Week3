#write a program to print 1st n natural numbers till 50 
num=int(input("enter any number:"))
if num>50:
    print("Enter number less than 50")
else:
    for i in range(1,num+1):
        print(i)



#write a program to print numbers in reverse order
num=int(input("Enter a number:"))
while num>=1:
    print(num,end=' ')
    num-=1
   
    
#Armstrong number
num=int(input("Enter the number:"))
temp=num
n=len(str(num))
sum=0       
while temp>0:
    digit=temp%10
    sum+=digit ** n
    temp//=10
print("Latest value of sum:",sum)
print("Latest value of temp:",temp)
if sum==num:
    print(num,"is armstrong number")
else:
    print(num,"is not armstrong number")


#Niven's/Harshad:
num=int(input("Enter the number:"))
temp=num
sum=0
while temp>0:
    digit=temp%10
    sum+=digit 
    temp//=10
print("Latest value of sum:",sum)
print("Latest value of temp:",temp)
if num%sum==0:
    print(num,"is nivens number")
else:
    print(num,"is not nivens number")

#square of a number upto 10    
for i in range(1,11):
    print(f"Square of {i} is {i*i}")


#find the factorial of a given number
n=int(input("Enter a number:"))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)
