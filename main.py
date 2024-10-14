

#
# k = 0
# def count_calls(func):
#
#
#     def wrapper(*args,**kwargs):
#         global k
#         k += 1
#         result = func(*args, **kwargs)
#         print(f'Функция greet вызвана {k} раз(а)')
#
#         return result
#
#     return wrapper
#
#
# @count_calls
# def greet(name):
#     print(f"Привет, {name}!")
#
# greet("Алексей")
# greet("Мария")
#
# # Вывод:
# # Функция 'greet' вызвана 1 раз(а)
# # Привет, Алексей!
# # Функция 'greet' вызвана 2 раз(а)
# # Привет, Мария!


# def type_check(func):
#
#     def wrapper(*args):
#
#         for i in args:
#             if not isinstance(i,(int)):
#
#                 raise TypeError(f"Неверный тип аргумента ({i}). Ожидался <class int>, получен {type(i)}")
#
#
#         result = func(*args)
#
#
#         return result
#     return wrapper
#
#
#
#
#
#
# @type_check
# def add(a, b):
#     return a + b
#
#
#
# print(add(2,3))   # 5
# print(add('3', '3'))   # TypeError: Неверный тип аргумента 'b'. Ожидался <class 'int'>, получен <class 'str'>





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




