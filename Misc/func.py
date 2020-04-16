def hello(x):
    print("Hey")
    print("Howdy")
    print("Holla")
    print(x)
    x = x + x
    #print(x)
    return x

x = 5
print("Olá\n")
print(x)
x = hello(int(input()))
print(x)
