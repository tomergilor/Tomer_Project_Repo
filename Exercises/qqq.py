list = [5, 2, 3, 1, 4, 9, 6, 7, 10, 8]

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

