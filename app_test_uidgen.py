from fakemail.fakemail import UidGen

u = UidGen()

for n in range(10):
    print(next(u))
print('******************')

b = 0
for i in u:
    b += 1
    if b == 10:
        break
    print(i)
print(i)
print('******************')

for n in range(10):
    print(next(u))
print('******************')
print(u)
print(u)
print(u)
print('******************')
