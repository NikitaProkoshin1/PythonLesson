#Задача 1. 

#from random import sample


#def more_then(num):
#    my_list = sample(range(num * 3), num)
#    print(my_list)
#    return [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]

#print(more_then((int(input()))))


#Задача 2. 

#def uniq_list(num):
#    return [el for el in range(20, num + 1) if el % 20 == 0 or el % 21 == 0]

#print(uniq_list(num)((int(input()))))


#Задача 3. 

def thesaurus(*args):
    names_dict = {}
    for i in sorted(args):
        letter = i[0]
        if letter not in names_dict:
            names_dict[letter] = [i]
        names_dict[letter] += [i]

    return names_dict

    print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"))