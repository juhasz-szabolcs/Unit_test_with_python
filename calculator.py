# sum(x, y) összeadja a két számot sum(2, 3) → 5
# subtract(x, y) kivonja y -t x -ből subtract(3, 2) → 1
# multiply(x, y) összeszorozza a két számot multiply(2, 3) → 6
# divide(x, y) elosztja x -et y -nal divide(6, 2) → 3.0

def sum(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: division by zero"

# print(sum(2, 3))
# print(subtract(3, 2))
# print(multiply(3, 2))
# print(divide(6, 2))
# print(divide(6, 0))
# print(divide(6, 3))