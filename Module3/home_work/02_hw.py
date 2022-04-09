n=5
numbers = []
number = []
while len(numbers)<n:
    import random
    number = random.randint(-100, 100)
    numbers[len(numbers):] = [number]
print(numbers)
