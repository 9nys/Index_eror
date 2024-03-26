try:
    my_list = [1, 2, 3]
    index = int(input("Ввести індекс числа: "))
    print(my_list[index])
except ValueError as e:
    print("IndexError")
else:
    print("IndexCorrect")

