def countdown(num):
    newlist = []
    for x in range(num, -1, -1):
        newlist.append(x)
    return newlist

NewYears = countdown(10)
print(NewYears)

def print_and_return(new_list):
    print(new_list[0])
    return new_list[1]

abc = print_and_return([34, 76])
print(abc)

def first_plus_length(new_list):
    x = len(new_list)
    answer = x + new_list[0]
    return answer

houses = [2, 7, 6]
print(first_plus_length(houses))

def values_greater_than_second(new_list):
    answer_list = []
    if (len(new_list) < 2):
        return False
    else:
        for x in range(0, len(new_list)):
            if(new_list[x] > new_list[1]):
                answer_list.append(new_list[x])
    print(len(answer_list))
    return answer_list

numbers = [6, 4, 8, 13, 15]
print(values_greater_than_second(numbers))

def length_and_value(size, value):
    new_list = []
    for x in range(0, size):
        new_list.append(value)
    return new_list

print(length_and_value(4,7))