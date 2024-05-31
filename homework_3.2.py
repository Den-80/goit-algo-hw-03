""" 
Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами, що випали випадковим чином і в певному діапазоні під час чергового тиражу. 
Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.

Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), 
яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей.

Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі випадкові числа в наборі повинні бути унікальні.

Вимоги до завдання:
1. Параметри функції:
    min - мінімальне можливе число у наборі (не менше 1).
    max - максимальне можливе число у наборі (не більше 1000).
    quantity - кількість чисел, які потрібно вибрати (значення між min і max).
2. Функція генерує вказану кількість унікальних чисел у заданому діапазоні.
3. Функція повертає список випадково вибраних, відсортованих чисел. 
Числа в наборі не повинні повторюватися. 
Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список.
 """
import random

#Варіант №1 функції
def get_numbers_ticket(min, max, quantity):
    numbers_list = []
    resulted_list = []
    if min < 1 or max > 1000 or (min > quantity or quantity > max):
       return print("Your parameters don't meet the requirements")
    else:   
        for i in range(min, max+1):
            numbers_list.append(i)
            i += 1

        for x in range(quantity):
            index = random.randint(0, len(numbers_list)-1)
            element = numbers_list[index]
            resulted_list.append(element)
            numbers_list.pop(index)
            x += 1

        sorted_numbers_list = sorted(resulted_list)
        return sorted_numbers_list

lottery_numbers = get_numbers_ticket(1, 36, 5)
print(f"Your lottery numbers: {lottery_numbers}")

#Варіант №2 функції
def get_numbers_ticket_2(min, max, quantity):
    numbers_set = set()
    if min < 1 or max > 1000 or (min > quantity or quantity > max):
        return print("Your parameters don't meet the requirements")
    else:
        while len(numbers_set) < quantity:
            element = random.randrange(min, max)
            numbers_set.add(element)

        numbers_list = sorted(list(numbers_set))
        return numbers_list

lottery_numbers_2 = get_numbers_ticket_2(1, 49, 6)
print(f"Your lottery numbers: {lottery_numbers_2}")
