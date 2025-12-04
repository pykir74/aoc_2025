f = open("day_two/data.txt")

data = f.readline()
counter = 0

ranges = data.split(",")
for ids in ranges:
    ids = ids.split("-")
    first_id = int(ids[0])
    last_id = int(ids[1])
    for i in range(first_id, last_id + 1):
        if len(str(i)) % 2 == 0:
            num = str(i)
            l = int(len(num)/2)
            left = num[:l]
            right = num[l:]
            if int(left) == int(right):
                counter += i
print(counter)