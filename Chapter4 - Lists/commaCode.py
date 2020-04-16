# Comma Code
# Say you have a list value like this:

# spam = ['apples', 'bananas', 'tofu', 'cats']

# Write a function that takes a list value as an argument and returns a string with all the items
# separated by a comma and a space, with and inserted before the last item. For example, passing the
# previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your
# function should be able to work with any list value passed to it. Be sure to test the case where
# an empty list [] is passed to your function.

def concatenate(spam):
    linked = ''
    if spam == []:
        return 'The list is empty.'

    for i in range(len(spam)):
        # print(i)
        if spam[i] == spam[-1]:
            linked = linked[0:-2]
            linked += ' and ' + spam[i]
        else:
            linked += spam[i] + ', '
    return linked

spam = ['apples', 'bananas', 'tofu', 'cats']
# spam = []

# print(spam)
print(concatenate(spam))