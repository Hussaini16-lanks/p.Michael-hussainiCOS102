# Start
# Input name1, age1
# Input name2, age2
# Display original ages
# swap = age1
# age1 = age2
# age2 = swap
# Display swapped ages
# End

name_1 = input('What is your name? ')
age_1 = input('How old are you? ')
name_2 = input('What is your name? ')
age_2 = input('How old are you? ')

#BEFORE SWAPPING
print(f'{name_1} is {age_1} and {name_2} is {age_2}')

#AFTER SWAPPING
swap = age_1
age_1 = age_2
age_2 = swap

print(f'{name_1} is {age_1} and {name_2} is {age_2}')