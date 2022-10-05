#Задача 1
#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

#def InputNumbers(inputText):
 #is_OK = False
 #while not is_OK:
 #try:
 #number = float(input(f"{inputText}"))
 #is_OK = True
 #except ValueError:
 #print("Данные введены не корректно")
 #return number


#def sumNums(num):
 #sum = 0
 #for i in str(num):
 #if i != ".":
 #sum += int(i)
 #return sum


#num = InputNumbers("Введите число: ")

#print(f"Сумма цифр = {sumNums(num)}")




# Задача2
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.



#def InputNumbers(inputText):
 #is_OK = False
 #while not is_OK:
 #try:
 #number = int(input(f"{inputText}"))
 #is_OK = True
 #except ValueError:
 #print("Число должно быть integer ")
 #return number


#def mult(n):
 #if n == 1:
 #return 1
 #else:
 #return n * mult(n - 1)


#num = InputNumbers("Введите число: ")

#list = []
#for e in range(1, num + 1):
    #list.append(mult(e))

#print(f"Произведения чисел от 1 до {num}:  {list}")

# Задача 3 
# задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

#int = n(input('Enter number: ')) 

#def (n):

#    return [round ((1  + 1 / x) **x, 2) for x in range (1, n  +  1)] 
        
#print(sequence (n))
#print(round(sum(sequence (n))))

