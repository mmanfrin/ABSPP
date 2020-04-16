n = 8
space = ' '
sharp = '#'

for i in range(n):
    print(space*(n-i), end='') # Spaces before hash
    print(sharp*(i+1) + space*2, end='') # Hashes + space
    print(sharp*(i+1), end='') # Opposite pyramid
    print('') # New line