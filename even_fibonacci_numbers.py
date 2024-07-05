a, b = 1,1
counter = 0
while a <= 4000000:
    if a % 2 == 0:
        counter += a
    a, b = b, a + b

print(counter)
