

## get user inputs
def userInput():
    loop = True
    counter = 0

    list = []

    while (loop == True):
        var = raw_input("Please enter something: ")

        if var != "-1":
          print "you entered", var
          list.append(int(var))
        elif(var == "-1"):
            loop = False
    return list

## sort list and print
def minSort(length, *list):
    for j in range(0,length):
        min = 100000
        for i in range(j, length):
            if list[i] < min:
                min = list[i]
                index = i

        temp = list[j]
        list[j] = list[index]
        list[index] = temp

        print min


list = userInput()
minSort(len(list), list)

