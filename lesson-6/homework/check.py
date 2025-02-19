def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper

@check
def div(a, b):
    return a / b
a = int(input("Enter numeration: ")) #bo'linuvchi
b = int(input("Enter the denominator")) #bo,luvchi
print(div(a, b))# bo'linma
