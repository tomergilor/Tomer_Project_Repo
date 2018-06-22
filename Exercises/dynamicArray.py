
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


for j in range(0, len(list)):
    min = 100000
    for i in range(j, len(list)):
        if list[i] < min:
            min = list[i]
            index = i

    temp = list[j]
    list[j] = list[index]
    list[index] = temp


    print min
