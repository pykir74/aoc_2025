f = open("day_one/data.txt")

MAX = 100 #0..99
pos = 50
counter = 0

for line in f:
    operation = line.strip()
    direction = operation[0]
    steps = int(operation[1:])

    old_pos = pos

    if direction == 'R':
        pos += steps
        counter += (pos // MAX) - (old_pos // MAX)

    elif direction == 'L':
        pos -= steps
        counter += ((old_pos - 1) // MAX) - ((pos - 1) // MAX)

    current_ring_pos = pos % MAX
print(f"result {counter}")