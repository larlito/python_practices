


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

