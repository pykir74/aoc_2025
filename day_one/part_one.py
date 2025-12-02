f = open("day_one/data.txt")

MAX = 100 #0..99
pos = 50
counter = 0

for line in f:
    operation = line.strip()
    direction = operation[0]
    steps = int(operation[1:])

    if direction == 'L':
        pos = abs((pos - steps) % MAX)
    elif direction == 'R':
        pos = (pos + steps) % MAX
    if pos == 0:    
        counter += 1
    print(pos)
print(f"result {counter}")