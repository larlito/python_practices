


k = 0
def count_calls(func):


    def wrapper(*args,**kwargs):
        global k
        k += 1
        result = func(*args, **kwargs)
        print(f'Функция greet вызвана {k} раз(а)')

        return result

    return wrapper


@count_calls
def greet(name):
    print(f"Привет, {name}!")

greet("Алексей")
greet("Мария")

# Вывод:
# Функция 'greet' вызвана 1 раз(а)
# Привет, Алексей!
# Функция 'greet' вызвана 2 раз(а)
# Привет, Мария!


def type_check(func):

    def wrapper(*args):

        for i in args:
            if not isinstance(i,(int)):

                raise TypeError(f"Неверный тип аргумента ({i}). Ожидался <class int>, получен {type(i)}")


        result = func(*args)


        return result
    return wrapper






@type_check
def add(a, b):
    return a + b



print(add(2,3))   # 5
print(add('3', '3'))   # TypeError: Неверный тип аргумента 'b'. Ожидался <class 'int'>, получен <class 'str'>





def validate_range(min_value, max_value):
    def decorator(func):

        def wrapper(*args,**kwargs):

            for i in range(0,len(args), 1):
                if args[i] > max_value or args[i] < min_value:
                    raise TypeError(f'Аргумент value имеет значение {args[i]}, что выходит за пределы [0,100]')


            for i in kwargs.keys():
                if kwargs[i] > max_value or kwargs[i] < min_value:
                    raise TypeError(f'Аргумент value имеет значние {kwargs[i]}, что выходит за пределы [0,100]')

            return func(*args,**kwargs)
        return wrapper

    return decorator








@validate_range(min_value=0, max_value=100)
def set_percentage(value):
    print(f"Установлено значение: {value}%")

set_percentage(50)     # Вывод: Установлено значение: 50%
set_percentage(150)    # ValueError: Аргумент 'value' имеет значение 150, что выходит за пределы [0, 100]







def trace(func):
    indent_count = 0

    def wrapper(*args, **kwargs):
        nonlocal indent_count
        indent = '  ' * indent_count

        print(f'{indent} --> Вход в функцию {func.__name__} с аргументами {args}')
        indent_count += 1

        result = func(*args,**kwargs)

        print(f'{indent} <-- Выход из функции {func.__name__} с результатом {result}')
        indent_count -= 1

        return result

    return wrapper



@trace
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

factorial(3)
# Вывод:
# --> Вход в функцию 'factorial' с аргументами (3,), {}
#     --> Вход в функцию 'factorial' с аргументами (2,), {}
#         --> Вход в функцию 'factorial' с аргументами (1,), {}
#             --> Вход в функцию 'factorial' с аргументами (0,), {}
#             <-- Выход из функции 'factorial' с результатом 1
#         <-- Выход из функции 'factorial' с результатом 1
#     <-- Выход из функции 'factorial' с результатом 2
# <-- Выход из функции 'factorial' с результатом 6
#




def uppercase_result(func):

    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)

        if isinstance(result,str):
            result = result.upper()

        return result

    return wrapper




@uppercase_result
def get_greeting(name):
    return f"Привет, {name}"

print(get_greeting("Алексей"))  # Вывод: ПРИВЕТ, АЛЕКСЕЙ

@uppercase_result
def add_numbers(a, b):
    return a + b

print(add_numbers(2, 3))  # Вывод: 5






def call_limit(func,max_calls = 3):
    call_count = 1

    def wrapper(*args):
        nonlocal  call_count

        if call_count > max_calls:
            raise RuntimeError('Превышено максимальное количество вызовов функции ')


        print(f'Вывод: {args}')
        call_count += 1



    return wrapper



@call_limit
def print_message(msg):
    print(msg)

print_message("Первый вызов")    # Вывод: Первый вызов
print_message("Второй вызов")    # Вывод: Второй вызов
print_message("Третий вызов")    # Вывод: Третий вызов
print_message("Четвертый вызов") # RuntimeError: Превышено максимальное количество вызовов функции '















