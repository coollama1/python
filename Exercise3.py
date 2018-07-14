#Phurpa Sherpa
#CSC 11300- morning Section

def displayPrime(n):
    
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j==0:
                break
            else:
                print(i)
                break
 #this function given with input 3 gives following output
 #3
 #5
 #7
 #9
 #11
 #13



import math
n= int(input("Enter a number you want a prime factor of: "))
print("Prime factors are:")
while(n%2)==0:
    print(2)
    n=n//2

for i in range(3,n+1):
    while(n%i)==0:
        print(i)
        n=n//i

if n>2:
    print(n)
#this program will give following output for 45:
#3
#3
#5


def gradeConversion(n):
    if n>=0 and n<40:
        print(" Grade F")
    elif n>=40 and n<60:
        print("Grade D")
    elif n>=60 and n<80:
        print("Grade C")
    elif n>=80 and n<90:
        print("Grade B")
    else:
        print("Grade A")
gradeConversion(43)
#thi function gives output of Grade D for input 43 given in last line




import math
n= int(input("Enter a number you want The Collatz Conjeture Sequence of:"))
while (True):
    if n % 2==0:
        n=n//2
        print(n)
    else :
        n=3*n+1
        print(n)
    if(n==1):
        break
#when 3 was entererd the following sequence is produces as output
#10
#5
#16
#8
#4
#2
#1
