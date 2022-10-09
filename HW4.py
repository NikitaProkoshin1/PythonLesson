#Задача 1 
# Вычислить число c заданной точностью d

#from decimal import Decimal

#def accuracy(num, acc):
#    number = Decimal(f"{num}")
#    return number.quantize(Decimal(f"{acc}"))

#    print(accuracy(float(input("Enter a real number: "))), (float(input("Enter the required accuracy '0.0001': ")))

# Задача 2
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

#def find_prime_nums(num):
#    pr_fact = []
#    di = 2
#    while num > 1:
#        if nim % di == 0:
#            pr_fact.append(di)
#            num /= di
#        else:
#                di +=1
#    return pr_fact

#print(find_prime_nums(int(input())))    

# Задача №3 
# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randrenge

def list_rand_nums(count, int):
    if count < 0:
        print("Negative value of the number of numbers")

    list_nums = []
    for i in range(count):
        list_nums.append(randrenge(count))

    return list_nums

def uniq_el(list_nums, list):
    result = []
    my_dict = {}.fromkeys(list_nums, 0)

    for i in list_nums:
        my_dict[i] += 1 

    for k in my_dict: 
        if my_dict == 1:
            result.append(k)

    return result            

all_list = list_rand_nums(int(input("out: ")))
print(all_list)
print(uniq_el(list_nums))    


#list = lst(map(int, input("Введите числа через пробел:\n").split()))
#print(f"Исходный список: {lst}")
#= = []
#[new_lst.append (i) for i in lst if i not in new_lst]
#print(f"Список из неповторяющихся элементов: {new_lst}")  
