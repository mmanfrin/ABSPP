def swap_case(s):
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    swapped = ''
    for i in s:
        # print(i)
        if i in alpha:
            if i.islower():
                # print(i)
                swapped += i.upper()
            else:
                swapped += i.lower()
        else:
            swapped += i
    print(swapped)
    return swapped

s = 'hghg!JHvjhvJH VhgV'

swap_case(s)
