f = open("day_two/data.txt")

data = f.readline()
counter = 0

ranges = data.split(",")
for ids in ranges:
    ids = ids.split("-")
    first_id = int(ids[0])
    last_id = int(ids[1])
    for i in range(first_id, last_id + 1):
        s_num = str(i)
        length = len(s_num)
        for pattern_len in range(1, (length // 2) + 1):
            if length % pattern_len == 0:
                pattern = s_num[:pattern_len]
                multiplier = length // pattern_len
                if pattern * multiplier == s_num:
                    counter += i
                    break
print(counter)
