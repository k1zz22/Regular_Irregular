def get_number():
    try:
        num = int(input("Enter a number: "))
        return num
    except ValueError:
        return get_number()

def get_regular_irregular(n):
    regular_irregular_count = 0
    regular_irregular_list = []

    while regular_irregular_count < n:
        R_Ir = input("Enter R for Regular and I for Irregular: ")
        if R_Ir == 'R':
            regular_irregular_list.append("Regural")
            regular_irregular_count += 1
        elif R_Ir == 'I':
            regular_irregular_list.append("Irregural")
            regular_irregular_count += 1
        else:
            continue

    return regular_irregular_list


input_list = []
number = get_number()
input_list.append(number)


regular_irregular_list = get_regular_irregular(number)


if len(regular_irregular_list) == 1:
    print(f"You have {regular_irregular_list[0]} on your list.")
else:
    result = ""
    for i in range(len(regular_irregular_list)):
        if i == len(regular_irregular_list) - 1:
            result += f"and {regular_irregular_list[i]} on your list."
        else:
            result += f"{regular_irregular_list[i]}, "
    print(f"You have {result}")