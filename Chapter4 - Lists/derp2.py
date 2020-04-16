cc = 4003600000000014

a = len(str(cc))

print(a)

for i in range(a):
    print(int(cc % 10), end='')
    cc = cc / 10
    # cc = cc / 10