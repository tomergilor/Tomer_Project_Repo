"""
print("Hello !!!")
num = input("please enter number:")
if num > 0:
    print "The number is greater than 0"
elif num ==0:
    print "The num is 0"
else:
    print "the numer is negative"

________________________________________________________________________________
num1 = input ("Enter number 1:")
num2 = input ("Enter number 2:")
num3 = input ("Enter number 3:")

print "your numbers are:" + str(num1) + " "  + str(num2) + " " +  str(num3)

______________________________________________________________________________

value = "abrakadabra"
print(len(value))
________________________________________________________________________________
a=0
while a<10:
    a = a+1
    print a
__________________________________________________________________________________
words = ['pu', 'window', 'dog']
for word in words:
    print word, len(word)
_____________________________________________________________________________________
word1 = raw_input ("Enter first word :")
word2 = raw_input ("Enter second word :")
word3 = raw_input ("Enter third word :")

print "all the words together:" + str(word1) + " " + str(word2) + " " + str(word3)
______________________________________________________________________________________


def sum(num1, num2):
    return num1+num2

x = input ("Enter first number:")
y = input ("Enter second number:")

result = sum(x,y)
print "The result is=" + str(result)
________________________________________________________________________________________

def sum(num1, num2):
    return num1+num2

def min(num1, num2):
    return num1-num2

def mult(num1, num2):
    return num1*num2

def div(num1, num2):
    return num1/num2

num1 = input ("Please enter the first number:")
num2 = input ("Please enter your second number:")
act = raw_input ("please choose your action:sum, min, mult, div : ")

if str(act) == 'sum':
    result = sum(num1,num2)
    print "The result is: " + str(result)
elif str(act) == 'min':
    result = min(num1,num2)
    print "The result is: " + str(result)
elif str(act) == 'mult':
    result = mult(num1,num2)
    print "The result is :" + str(result)
elif str(act) == 'div':
    result = div(num1,num2)
    print "The result is: " + str(result)
___________________________________________________________________________________________________________

num = input ("Please enter number:")
for i in range (1,num):
    for j in range (num,0):
        print (" ")
            for h in range (1,i):
                  print ("X")
                      for g in range (i,h):
                             print ("X")
                             print '\n'
____________________________________________________________________________________________________________

size = int(raw_input("Enter the size: "))
char = raw_input("Enter the character to draw: ")
for i in range(1, size+1):
    print char*i
_____________________________________________________________________________________________________________


size = input("Enter the size: ")
for i in range(1, size+1):
    print " " * (size+1) + "X" * i

size = int(raw_input("Enter the size: "))
temp = size-1
for i in range(1, size+1):
    print (" " * temp) + ("X" * (i*2 -1))
    temp = temp-1

_____________________________________________________________________________________________________________

size = int(raw_input("Enter the size: "))
temp = size-1
for i in range(1, size+1):
    print (" " * temp) + ("X" * (i*2 -1))
    temp = temp-1
________________________________________________________________________________________________________________

size = int(raw_input("Enter the size: "))
temp = size-1
for i in range(1, size+1):
    print (" " * temp) + ("X" * (i*2 -1))
    temp = temp-1
        for i in range(size+1, 1):
             print (" " * temp) + ("X" * (j*2 -1))
             temp = temp-1
_______________________________________________________________________________________________________________
a = [5, 2, 3, 1, 4]
a.sort()
print a
________________________________________________________________________________________________________________

list = [5, 2, 3, 1, 4, 9, 6]
small = list[0]
big = list[0]

for i in range(1,len(list)):

 if (list[i] > big):
    big = list[i]
 elif (list[i] < small):
    small = list[i]
print "The small number is: " + str(small)
print "The big number is: " + str(big)
___________________________________________________________________________________________________________________
"""
print("Hello !!!")
num = input("please enter number:")
if num > 0:
    print "The number is greater than 0"
elif num ==0:
    print "The num is 0"
else:
    print "the numer is negative"

