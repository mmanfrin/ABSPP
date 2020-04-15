def dividebyzero(number):
    try:
        print(42 / number)
    except ZeroDivisionError:
        print('Error: Cannot divide by zero!')
    except TypeError:
        print('Error: Can only divide by a number!')
    return

dividebyzero(2)
dividebyzero('a')
dividebyzero(12)
dividebyzero(0)
dividebyzero(1)