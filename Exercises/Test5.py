###### Sorting Arr

# list = [8,2,3,5,7]
# print list
#
# index = 0
# index2 = 1
# val = 0
#
# while index < len(list)-1:
#     while index < len(list)-1:
#         if list[index] > list[index2]:
#             val = list[index]
#             list[index] = list[index2]
#             list[index2] = val
#
#             index += 1
#             index2 += 1
#
# print list

#________________________________________________________________________________________________________________________

###### Enter number, if 2 folowing numbers equal to the number, print true

# list = [8,2,3,5,7]
# print "Your list is: " + str(list)
#
# num = int(raw_input("Please enter a number: "))
# print num
#
# index = 0
# while index < len(list)-1:
#     if list[index] + list[index+1] == num:
#         print "True"
#         break
#     index += 1

########################################################################################################################

# sum how much charakters in the string
###  a|a|a|b|b|c|c
###  a|a|a|b|b|b|c

# str_arr = raw_input("Please enter string: ")
#
# num = 1
# index = 0
#
# while index < len(str_arr)-1:
#     if index+1 == len(str_arr)-1: ## if last character
#           if str_arr[index] == str_arr[index + 1]:
#              num+=1
#              print str_arr[index] + str(num)
#           else:
#              print str_arr[index] + str(num)
#              print str_arr[index+1] + str(1)
#     elif str_arr[index] == str_arr[index+1]:
#         num+= 1
#     else:
#           print str_arr[index] + str(num)
#           num = 1
#     index+= 1
#
# Output:
# Please enter string: rrrffd
# r3
# f2
# d1

######################################################################
# ## enter port number and find if it appears in the file (text.file.txt) with all the ports and if existing print it
# text_file = open ("test.txt","r")
# print text_file.read()
# port = raw_input("For find specific port, Please enter the port number:")
#
# for i in text_file:
#     if port in str(i):
#         print i
#     else:
#         print "Can't find the specific port "
#         break
# text_file.close()
#######################################################################
# # Program to check if a string is palindrome or not
#
# my_str = []
#
# my_str = raw_input("Enter a string: ")
#
# rev_str = reversed(my_str)
#
# if list(my_str) == list(rev_str):
#    print("It is palindrome")
# else:
#    print("It is not palindrome")
########################################################################
# arr=[]
# arr = raw_input("please enter some words:")
#
# for i in range(len(arr)):
#     print i, arr[i]
######################################################################
# ## Open browser with url
#
# import webbrowser
#
# url = 'http://www.python.org/'
#
# webbrowser.open_new(url)















