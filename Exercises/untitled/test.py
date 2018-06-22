# """
# loop = True
# counter = 0
#
# list = []
#
# while (loop == True):
#     var = raw_input("Please enter something: ")
#
#     if var != "-1":
#        list.append(int(var))
#     elif(var == "-1"):
#         loop = False
#
# print list
# =====================================================
#
# passwordFile = open('SecretPasswordFile.txt')
# secretPassword = passwordFile.read()
# print('Enter your password.')
# typedPassword = input()
# if typedPassword == secretPassword:
#     print('Access granted')
# if typedPassword == '12345':
#     print('That password is one that an idiot puts on their luggage.')
# else:
#      print('Access denied')
# _________________________________________________________________________
# # create new file named tttt
# # it's necessary to add permission
# # r=read , w=write, a=append, r+ = read+write
#
# my_file = open("tttt.file","w")
# #my_file.close()
#
# #to write to the file
#
# my_file.write(" this is test")
# my_file.close()
# _________________________________________________________________________________
# #to add(not  replace) to the text
# my_file = open("tttt.file","a")
# my_file.write(" this is test2")
# my_file.close()
# _________________________________________________________________________________
# #to read from file
# my_file = open("tttt.file","r")
# print my_file.read()
# my_file.close()
# _________________________________________________________________________________
# # to read from the file
# my_file = open("tttt.file","r")
# print my_file.read()
# my_file.close()
# _________________________________________________________________________________
# # to find word in the file and how much times
# count =0
# my_file = open("tttt.file","r")
# for line in my_file:
#     if("this" in line):
#         count = count + 1
#
# print "the word found " + str(count) + " times "
#
# _________________________________________________________________________________
# # to find any word(this) and print the line it shown
# my_file = open("tttt.file","r")
# for line in my_file:
#     if("this" in line):
#        print "found",line
#
# _________________________________________________________________________________
# # run loop from 1-50 and if find the number 20 stop the loop and write "found it"
# for number in range(1,50):
#     print number
#     if number == 20:
#         print "found it"
#         break
# _________________________________________________________________________________
# #enter numbers 1-100 to continue and 100-200 to stop the loop
# print ("press 1-100 to continue\n"
#       "press 100-200 to exit")
#
# while True:
#     number = int(raw_input("inset number: "))
#     if number >= 1 and number <= 100:
#         print "another loop"
#     elif number >100 and number < 200:
#         print "stop loop"
#         break
#     else:
#         print "wrong number"
# _________________________________________________________________________________
# # While loop counting 1 to 50
# number=1
# while number<51:
#     print number
#     number=number+1  #it's possible to write this line also: number+=1
# _________________________________________________________________________________
#
# #insert number while the number is not 0
# number = 1
# while number !=0:
#     number = int(raw_input("inset number:(to stop click 0):"))
#     if number >= 1:
#         print "The number bigger than 0"
#     elif number < 0:
#         print "The number smaller than 0"
# print "the number is 0"
# _________________________________________________________________________
#
# # list and array
# List = [22,55,32,66,89,5]
# print List
#
# #add number to the List
# List.append(465)
# print List
#
# # replace the first number to 1
# List [0] = 1
# print List
#
# #sort the list
# List.sort()
# print List
#
# #show the index of specific number
# print List.index(66)
#
# List = [22,55,32,66,89,5]
# print List
#
# #remove number 66 fron the list
# List.remove(66)
#
# #to show the List Length (6)
# print len(List)
#
# #go over all the port of the list
# for port in List:
#     print port
#
# # set arr - this is another type of list(array) that exist in python. this is list that each number can appears ones
# #it means that its impossible add the same number twice
# #set
#
# setlist = {1,5,7,22,55}
# print setlist
#
# #remove from set list
# setlist.remove(7)
# print setlist
#
# setlist.add(27)
# print setlist
#
#
# # dictenary
# # another type of lisr(array) that can define list with values.
# # f.e - A=1, B=2, C=3

#
# dict = {'ssh':22,'telnet':23,'ftp':21}
# print dict
#
# #print the ssh value
# print dict['ssh']
#
# #add value
# #dict ['http'] =80
#
# #delete value from dict
# #del list['telnet']
#
# #print all keys from dic
# print dict.keys()
#
# #print all values from dict
# print dict.values()
#
############################################################################

#Function: example for add and min functions with user input

# def add(num1,num2):
#     add=num1+num2
#     return add
#
# def min(num1,num2):
#     min=num1-num2
#     return min
#
#
# #use the functions with input from the user
# act = int(raw_input(" Please choose sum or min (1-for add and 2-for min: "))
# if act == 1:
#     num1 = int(raw_input("Please enter the first number: "))
#     num2 = int(raw_input("Please enter the second number: "))
#     sum = add(num1,num2)
#     print "The sum is: %d "% (sum)
#
# elif act==2:
#     num1 = int(raw_input("Please enter the first number: "))
#     num2 = int(raw_input("Please enter the second number: "))
#     sum = min(num1,num2)
#     print "The sum is: %d"% (sum)
###################################################################################

# program that input from the user 10 numbers and calc and print the biggest number:
#
# str_num = []
# k = 1
# max = 0
#
# for i in range(0,10):
#     num = int(raw_input("Please enter a number: "))
#
#     str_num.append(int(num))
#
# for j in range(0,10):
#
#     if str_num[j] > str_num[k]:
#         max = str_num[j]
#         str_num[j] = str_num[k]
#         str_num[k] = max
#
# print "The biggest number is: %d" %(max)
#
###################################################################################
# # The program choose 7 numbers randomaly and sum all the numbers. if the sum devided by 7 print also BOOM!
#
# from random import randint
# num = 0
#
# list = []
#
# for i in range(0,7):
#     num = num + randint(0, 100)
#
# print num
# if num % 7 == 0:
#     print "BOOM !"
####################################################################################
# # Program that get rand number and return the sum of the numbers f.e = 34 return 7
# from random import randint
# sum=0
#
# num = randint(10, 100)
#
# num_str = str(num)
# print num_str
#
#
# for c in num_str:
#     sum = sum + int(c)
#
# print sum
########################################################################################
#
#
# Write a program that reads 10 numbers from
# the user and prints the largest one
#
#
# max_number = int(raw_input("Enter number:"))
#
# for X in range(9):
#     num = int(raw_input("Enter number:"))
#     if num > max_number:
#         max_number = num
#
# print "Max number = %d" % max_number
#
# ######################################################################################
#
# """
# Write a Python program that randomizes 7 numbers
# and prints their sum total.
# If the sum is divisable by 7, also print the word "Boom"
# """
#
# from random import randint
#
# total = 0
#
# for _ in range(7):
#     num = randint(1,100)
#     total += num
#
# print "Total sum is: %d" % total
# if total % 7 == 0: print "Boom!"
#########################################################################################
"""
Write a program that reads lines from the user until an empty line is inserted.
After the user typed in an empty line, print all previously inserted lines in reverse
order (from last to first)
"""
#
# text = ""
#
# while True:
#     line = raw_input("Enter text:")
#     text = line + "\n" + text
#     if len(line) == 0: break
#
# print text
#
#
#
# number = 0
# list = []
# loop = True
#
# while (loop == True):
#     number = raw_input("Please enter a number: ")
#
#     if number != "-1":
#        list.append(int(number))
#     elif number == "-1":
#        loop = False
#
# print list
###############################################################################
## Guess a random number from the computer
# from random import randint
#
# num = randint(1,100)
#
# while True:
#      guess = raw_input("Hi, please guess the number between 1-100:")
#      if int(guess) > num:
#          print " your number is too big"
#      elif int(guess) < num:
#          print " Your number is too small"
#      else:
#          print "BINGO !!!"
#          break
##################################################################################
#
# mil = {'a':1, 'b':2, 'c':3}
# print ['a' in mil]
# print mil['a']
# print ['d' in mil]
#
# print mil.get(1)
#
# mil =  {'d':4}
# print mil['b']

#################################################################################


#
#
# ##registration
# name = raw_input("Hi please enter your user name:")
# psw = raw_input("Please enter your password:")
# nick = raw_input("Please enter your nick name:")
# print """*************************************************************
#       Thank you, the registration process has completed !
# *************************************************************"""
# ## enter to the system
# user_check = raw_input("Please enter your user name:")
# psw_check = raw_input("Please enter your password:")
#
# if user_check == name and psw_check == psw:
#     print " you've passed the security check !!! "
# elif user_check != name:
#     print " your user name is incorrect !"
# elif psw_check != psw:
#     print " your password is incorrect !"
# ## nick name question
#     quest = raw_input("Do you want to answer the private question ? (yes/no) ")
#     if quest == "yes":
#         quest2 = raw_input("What is your nick name ? :")
#     if quest2 == nick:
#         print " Right !!!"
#     else:
#         print "Wrong !!!"
#     elif quest == "no":
#         print "Bye Bye !"
#
# data = {}
#
# data.items().append(name,psw)


# def add_name():
#     # global d1
#     print "Enter name"
#     name=raw_input()
#     print "Enter password"
#     psw=raw_input()
#     d1[name]=psw
#
# d1 = {}
# while 1:
#      print "Type name to search"
#      print "Type 'add' to add names or 'quit' to exit:"
#      x=raw_input()
#      if x=='quit':
#           break
#      if x in d1.keys():
#           print d1[x], x
#      if x=='add':
#           add_name()
#################################################################################
#
# str = [1,4,7,9]
#
# print str
# print max(str)      #print the higher number in the arr
# print min(str)      #PRINT THE LOWER NUMBER IN THE ARR.
#
################################################################################
# # counting how many times each letter appears in the arr
#
# from collections import Counter
#
# arr = ['a', 'a', 'a', 'b', 'c', 'b', 'a', 'c','d','c']
# dict = Counter(arr)
# print dict.items()

##################################################################################
# """
# Count how many letters in a word
# and print them sorted, using a Counter
# """
#
# from collections import Counter   #Counter it a fumction that count how many letters appers in a word or sentece
#
# print "Please type in a word"
# word = raw_input()
#
# freq = Counter(word)
#
# print freq
#
# for k in sorted(freq, key=freq.get, reverse=True):      #loop that runing and print how mant times each letter appers sorted ( like counter but different)
#     print "%s => %d" % (k, freq[k])
# ##################################################################################




