name = input('What is your name: ')
age = int(input('What is your age: '))

if name == 'Alice':
    print("Hi, Alice")

elif age < 12:
    print('You are not Alice, kiddo')

elif age > 2000:
    print('Unlike you, Alice is not an undead vampire')

elif age > 100:
    print('You are not Alice, granny')

else:
    print('You are not Alice, a vampire, or granny')