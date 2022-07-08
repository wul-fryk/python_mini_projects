from random import sample
chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()_+=-}{[]|<>,./?'
user = int(input('Enter a nuber from 1 to 87: '))
res = ''.join(sample(chars, user))

print(res)
print(len('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()_+=-}{[]|<>,./?'))